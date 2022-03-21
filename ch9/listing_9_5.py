# 擴展到其他範圍
def test_turn_on_cooler_and_blower_if_too_hot():
    too_hot()
    assert "hBChl" == hw.get_state()

def test_turn_on_heater_and_blower_if_too_cold():
    too_cold()
    assert "HBchl" == hw.get_state()

def test_turn_on_hi_temp_alarm_at_threshold():
    way_too_hot()
    assert "hBCHl" == hw.get_state()

def test_turn_on_lo_temp_alarm_at_threshold():
    way_too_cold()
    assert "HBchL" == hw.get_state()