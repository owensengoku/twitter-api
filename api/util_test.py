from .util import *
from datetime import datetime, timezone


def test_strptime():
    date_obj = strptime('Sun Oct 28 09:35:42 +0000 2018')
    assert date_obj == datetime(2018, 10, 28, 9, 35, 42, tzinfo=timezone.utc)

def test_strftime():
    date_obj = datetime(2018, 3, 7, 15, 57, 33)
    assert strftime(date_obj) == '3:57 PM - 7 Mar 2018'
