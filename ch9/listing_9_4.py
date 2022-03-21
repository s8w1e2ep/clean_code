# 增加可讀性
# 大寫字母代表開啟，小寫字母代表關閉
def test_turn_on_lo_temp_alarm_at_threshold():
    way_too_cold()
    assert "HBchL" == hw.get_state()