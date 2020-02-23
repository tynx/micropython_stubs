"""
The ``esp32`` module contains functions and classes specifically aimed at
controlling ESP32 modules.
"""

def wake_on_touch(wake):
    """
     Configure whether or not a touch will wake the device from sleep.
     *wake* should be a boolean value.
    """
    pass

def wake_on_ext0(pin, level):
    """
     Configure how EXT0 wakes the device from sleep.  *pin* can be ``None``
     or a valid Pin object.  *level* should be ``esp32.WAKEUP_ALL_LOW`` or
     ``esp32.WAKEUP_ANY_HIGH``.
    """
    pass

def wake_on_ext1(pins, level):
    """
     Configure how EXT1 wakes the device from sleep.  *pins* can be ``None``
     or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
     or ``esp32.WAKEUP_ANY_HIGH``.
    """
    pass

def raw_temperature():
    """
     Read the raw value of the internal temperature sensor, returning an integer.
    """
    pass

def hall_sensor():
    """
     Read the raw value of the internal Hall sensor, returning an integer.
    """
    pass

