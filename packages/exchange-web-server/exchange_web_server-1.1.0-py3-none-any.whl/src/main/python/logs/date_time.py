import pytz
import datetime

from cached_property import cached_property_ttl
from exchangelib import EWSDateTime
from python.io_operations.month_mapping import MONTH_FOLDER_MAPPING


class CurrentDate:
    def __init__(self):
        self._today = None
        self._now = None
        self._yesterday = None
        self._current_month: str = ''
        self._today_as_ews_datetime = EWSDateTime

    @cached_property_ttl(ttl=15)
    def today(self) -> datetime.date:
        """:return: datetime.date.today()"""
        return datetime.date.today()

    @cached_property_ttl(ttl=15)
    def now(self) -> datetime.datetime:
        """:return: datetime.datetime.now()"""
        return datetime.datetime.now()

    @cached_property_ttl(ttl=15)
    def yesterday(self) -> datetime.date:
        """:return: datetime.date.today() -1"""
        return datetime.date.today() + datetime.timedelta(-1)

    @cached_property_ttl(ttl=15)
    def current_month(self) -> str:
        """:return: e.g. 01. Januar"""
        return MONTH_FOLDER_MAPPING.get(f"{self.yesterday.month:02}")

    @cached_property_ttl(ttl=15)
    def today_as_ews_datetime(self) -> EWSDateTime:
        pytz_tz = pytz.timezone('Europe/Berlin')
        py_dt = pytz_tz.localize(datetime.datetime(self.today.year, self.today.month, self.today.day))
        return EWSDateTime.from_datetime(py_dt)

    @cached_property_ttl(ttl=15)
    def yesterday_as_ews_datetime(self) -> EWSDateTime:
        pytz_tz = pytz.timezone('Europe/Berlin')
        py_dt = pytz_tz.localize(datetime.datetime(self.yesterday.year, self.yesterday.month, self.yesterday.day))
        return EWSDateTime.from_datetime(py_dt)
