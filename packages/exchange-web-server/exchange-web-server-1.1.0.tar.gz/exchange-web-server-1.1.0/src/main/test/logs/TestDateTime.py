import datetime
import time
import unittest

from python.logs.date_time import CurrentDate

classUnderTest = CurrentDate()


class TestDateTime(unittest.TestCase):

    def test_a_property_today(self):
        assert_today = datetime.date.today()
        self.assertEqual(classUnderTest.today, assert_today)

    def test_b_property_now(self):
        time_1 = classUnderTest.now
        time.sleep(0.01)
        time_2 = classUnderTest.now

        self.assertEqual(time_2, time_1)

    def test_c_instance_variables(self):
        assert_yesterday = datetime.date.today() + datetime.timedelta(-1)
        ytd = classUnderTest.yesterday
        self.assertEqual(ytd, assert_yesterday)

    def test_d_get_current_month(self):
        assert_string = f'{classUnderTest.today.month:02}'
        self.assertEqual(classUnderTest.current_month[:2], assert_string)

    def test_e_data_types(self):
        a = datetime.datetime.today()
        b = datetime.date.today()
        td = datetime.timedelta(days=1)
        yesterday: datetime.date = b + td

        self.assertEqual(type(a), datetime.datetime)
        self.assertEqual(type(b), datetime.date)
        self.assertEqual(type(yesterday), datetime.date)

    def test_e_scheduled_time_within_germany(self):
        local_date_time_cet: datetime.datetime = datetime.datetime(2022, 11, 8, 23, 45, 0)
        local_date_time_cest: datetime.datetime = datetime.datetime(2022, 6, 17, 23, 45, 0)

        self.assertEqual(f'{local_date_time_cet.hour}:{local_date_time_cet.minute}', '23:45')
        self.assertEqual(f'{local_date_time_cest.hour}:{local_date_time_cest.minute}', '23:45')
