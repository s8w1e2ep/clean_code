def get_state():
    state = ''
    state += 'H' if heater else 'h'
    state += 'B' if blower else 'b'
    state += 'C' if cooler else 'c'
    state += 'H' if hi_temp_alarm else 'h'
    state += 'L' if lo_temp_alarm else 'l'
    return state