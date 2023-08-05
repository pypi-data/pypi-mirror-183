import io
from datetime import time, datetime, timedelta, timezone
from PySide6.QtCore import QCoreApplication, QBuffer
from PySide6.QtGui import QImage
try:
    from pyzbar import pyzbar
except ImportError:
    pass  # Helpers that use this imports shouldn't be called if imports are absent
try:
    from PIL import Image, UnidentifiedImageError
except ImportError:
    pass   # Helpers that use this imports shouldn't be called if imports are absent


def decodeError(orginal_msg):
    messages = {
        'JAL_SQL_MSG_0001': QCoreApplication.translate("Error",
                                                       "Investment account should have associated broker assigned"),
        'JAL_SQL_MSG_0002': QCoreApplication.translate("Error", "Can't delete predefined category")
    }

    if orginal_msg[:4] != 'JAL_':
        return orginal_msg
    code = orginal_msg[:16]
    return messages[code]


# -----------------------------------------------------------------------------------------------------------------------
# Returns True if all modules from module_list are present in the system
def dependency_present(module_list):
    result = True
    for module in module_list:
        try:
            __import__(module)
        except ImportError:
            result = False
    return result


# -----------------------------------------------------------------------------------------------------------------------
# converts given unix-timestamp into string that represents date and time
def ts2dt(timestamp: int) -> str:
    return datetime.utcfromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')


# -----------------------------------------------------------------------------------------------------------------------
# converts given unix-timestamp into string that represents date
def ts2d(timestamp: int) -> str:
    return datetime.utcfromtimestamp(timestamp).strftime('%d/%m/%Y')


# ----------------------------------------------------------------------------------------------------------------------
# Converts QImage class input into PIL.Image output
# (save QImage into the buffer and then read PIL.Image out from the buffer)
# Raises ValueError if image format isn't supported
def QImage2Image(image: QImage) -> Image:
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    image.save(buffer, "BMP")
    try:
        pillow_image = Image.open(io.BytesIO(buffer.data()))
    except UnidentifiedImageError:
        raise ValueError
    return pillow_image

# ----------------------------------------------------------------------------------------------------------------------
# Function takes PIL image and searches for QR in it. Content of first found QR is returned. Otherwise - empty string.
def decodeQR(qr_image: Image) -> str:
    barcodes = pyzbar.decode(qr_image, symbols=[pyzbar.ZBarSymbol.QRCODE])
    if barcodes:
        return barcodes[0].data.decode('utf-8')
    return ''


# -----------------------------------------------------------------------------------------------------------------------
# Helpers to work with datetime
class ManipulateDate:
    @staticmethod
    def toTimestamp(date_value):
        time_value = time(0, 0, 0)
        dt_value = datetime.combine(date_value, time_value)
        return int(dt_value.replace(tzinfo=timezone.utc).timestamp())

    @staticmethod
    def PreviousWeek(day=datetime.today()):
        end = day + timedelta(days=1)
        prev_week = day - timedelta(days=7)
        start_of_week = prev_week - timedelta(days=prev_week.weekday())
        return ManipulateDate.toTimestamp(start_of_week), ManipulateDate.toTimestamp(end)

    @staticmethod
    def PreviousMonth(day=datetime.today()):
        end = day + timedelta(days=1)
        first_day_of_month = day.replace(day=1)
        last_day_of_prev_month = first_day_of_month - timedelta(days=1)
        first_day_of_prev_month = last_day_of_prev_month.replace(day=1)
        return ManipulateDate.toTimestamp(first_day_of_prev_month), ManipulateDate.toTimestamp(end)

    @staticmethod
    def PreviousQuarter(day=datetime.today()):
        end = day + timedelta(days=1)
        prev_quarter_month = day.month - day.month % 3 - 3
        if prev_quarter_month > 0:
            quarter_back = day.replace(month=prev_quarter_month)
        else:
            quarter_back = day.replace(month=(prev_quarter_month + 12), year=(day.year - 1))
        first_day_of_prev_quarter = quarter_back.replace(day=1)
        return ManipulateDate.toTimestamp(first_day_of_prev_quarter), ManipulateDate.toTimestamp(end)

    @staticmethod
    def PreviousYear(day=datetime.today()):
        end = day + timedelta(days=1)
        first_day_of_year = day.replace(day=1, month=1)
        last_day_of_prev_year = first_day_of_year - timedelta(days=1)
        first_day_of_prev_year = last_day_of_prev_year.replace(day=1, month=1)
        return ManipulateDate.toTimestamp(first_day_of_prev_year), ManipulateDate.toTimestamp(end)

    @staticmethod
    def QuarterToDate(day=datetime.today()):
        end = day + timedelta(days=1)
        begin_month = day.month - 3
        if begin_month > 0:
            begin = day.replace(month=begin_month)
        else:
            begin = day.replace(month=(begin_month + 12), year=(day.year - 1))
        begin = begin.replace(day=1)
        return ManipulateDate.toTimestamp(begin), ManipulateDate.toTimestamp(end)

    @staticmethod
    def YearToDate(day=datetime.today()):
        end = day + timedelta(days=1)
        begin = day.replace(day=1, year=(day.year - 1))
        return ManipulateDate.toTimestamp(begin), ManipulateDate.toTimestamp(end)

    @staticmethod
    def ThisYear(day=datetime.today()):
        end = day + timedelta(days=1)
        begin = day.replace(day=1, month=1)
        return ManipulateDate.toTimestamp(begin), ManipulateDate.toTimestamp(end)

    @staticmethod
    def LastYear(day=datetime.today()):
        end = day.replace(day=1, month=1)
        begin = end.replace(year=(day.year - 1))
        return ManipulateDate.toTimestamp(begin), ManipulateDate.toTimestamp(end)

    @staticmethod
    def AllDates(day=datetime.today()):
        end = day.replace(day=1, month=1)
        return 0, ManipulateDate.toTimestamp(end)
