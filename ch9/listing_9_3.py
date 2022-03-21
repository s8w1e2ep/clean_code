# 檢查在溫度過冷的情況下，低溫的警示器、暖驢、抽風機是否會全部打開
def test_turn_on_lo_temp_alarm_at_threshold():
    hw.set_temp(WAY_TOO_COLD)
    controller.tic()

    assert hw.heater_state() == True
    assert hw.blower_state() == True
    assert hw.cooler_state() == False
    assert hw.hi_temp_alarm() == False
    assert hw.lo_temp_alarm() == True