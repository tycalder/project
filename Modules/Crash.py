crashTrigger = 21

def set_crash_trigger(pin: int):
   crashTrigger = pin

def ping_pin(pin: int):
    button = Button(pin, pull_up = False)
    if button.is_pressed:
        return True
    else:
        return False

def crash_detected():
    """Pings Crash Trigger, returns true if a crash has been detected"""
    ping_pin(crashTrigger)
    if ping_pin(crashTrigger == True):
        return True
    else:
        return False

#def run_crash_protocol():

        