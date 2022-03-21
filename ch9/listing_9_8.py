import calendar
from datetime import datetime as dt
from datetime import timedelta as td

# 如果要使用 pytest 測試只需要將該檔名前面加上 test => test_listing_9_8.py
# 原本月份有 31 天，加一個月，但這個月只有 30 天，那麼新的日期是該月第 30 天
# 原本月份有 31 天，加兩個月，這個月有 31 天，那麼新的日期是該月第 31 天
# 原本月分只有 30 天，加一個月，但這個月有 31 天，那麼新的日期是該月第 30 天
def test_add_months():
    date1 = dt(2004, 5, 31)

    date2 = add_months(date1, 1)
    assert 30 == date2.day
    assert 6 == date2.month
    assert 2004 == date2.year

    date3 = add_months(date1, 2)
    assert 31 == date3.day
    assert 7 == date3.month
    assert 2004 == date3.year

    date4 = add_months(add_months(date1, 1), 1)
    assert 30 == date4.day
    assert 7 == date4.month
    assert 2004 == date4.year

def add_months(date, months):
    month = date.month - 1 + months
    year = date.year + month // 12
    month = month % 12 + 1
    # monthrange 會回傳當月第一天的工作日數(星期幾)與該月天數的 tuple
    day = min(date.day, calendar.monthrange(year, month)[1])
    return dt(year, month, day)