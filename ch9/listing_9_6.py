def get_state():
    state = ''
    state += 'H' if heater else 'h'
    state += 'B' if heater else 'b'
    state += 'C' if heater else 'c'
    state += 'H' if heater else 'h'
    state += 'L' if heater else 'l'
    return state