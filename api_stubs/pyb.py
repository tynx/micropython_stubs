"""
The ``pyb`` module contains specific functions related to the board.
"""

def delay(ms):
    """
    Delay for the given number of milliseconds.
    """
    pass

def udelay(us):
    """
    Delay for the given number of microseconds.
    """
    pass

def millis():
    """
    Returns the number of milliseconds since the board was last reset.
    The result is always a MicroPython smallint (31-bit signed number), so
    after 2^30 milliseconds (about 12.4 days) this will start to return
    negative numbers.
    Note that if :meth:`pyb.stop()` is issued the hardware counter supporting this
    function will pause for the duration of the "sleeping" state. This
    will affect the outcome of :meth:`pyb.elapsed_millis()`.
    """
    pass

def micros():
    """
    Returns the number of microseconds since the board was last reset.
    The result is always a MicroPython smallint (31-bit signed number), so
    after 2^30 microseconds (about 17.8 minutes) this will start to return
    negative numbers.
    Note that if :meth:`pyb.stop()` is issued the hardware counter supporting this
    function will pause for the duration of the "sleeping" state. This
    will affect the outcome of :meth:`pyb.elapsed_micros()`.
    """
    pass

def elapsed_millis(start):
    """
    Returns the number of milliseconds which have elapsed since ``start``.
    This function takes care of counter wrap, and always returns a positive
    number. This means it can be used to measure periods up to about 12.4 days.
    Example::
        start = pyb.millis()
        while pyb.elapsed_millis(start) < 1000:
            # Perform some operation
    """
    pass

def elapsed_micros(start):
    """
    Returns the number of microseconds which have elapsed since ``start``.
    This function takes care of counter wrap, and always returns a positive
    number. This means it can be used to measure periods up to about 17.8 minutes.
    Example::
        start = pyb.micros()
        while pyb.elapsed_micros(start) < 1000:
            # Perform some operation
            pass
    """
    pass

def hard_reset():
    """
    Resets the pyboard in a manner similar to pushing the external RESET
    button.
    """
    pass

def bootloader():
    """
    Activate the bootloader without BOOT\* pins.
    """
    pass

def fault_debug(value):
    """
    Enable or disable hard-fault debugging.  A hard-fault is when there is a fatal
    error in the underlying system, like an invalid memory access.
    If the *value* argument is ``False`` then the board will automatically reset if
    there is a hard fault.
    If *value* is ``True`` then, when the board has a hard fault, it will print the
    registers and the stack trace, and then cycle the LEDs indefinitely.
    The default value is disabled, i.e. to automatically reset.
    """
    pass

def disable_irq():
    """
    Disable interrupt requests.
    Returns the previous IRQ state: ``False``/``True`` for disabled/enabled IRQs
    respectively.  This return value can be passed to enable_irq to restore
    the IRQ to its original state.
    """
    pass

def enable_irq(state=True):
    """
    Enable interrupt requests.
    If ``state`` is ``True`` (the default value) then IRQs are enabled.
    If ``state`` is ``False`` then IRQs are disabled.  The most common use of
    this function is to pass it the value returned by ``disable_irq`` to
    exit a critical section.
    """
    pass

def freq([sysclk[, hclk[, pclk1[, pclk2]]]]):
    """
    If given no arguments, returns a tuple of clock frequencies:
    (sysclk, hclk, pclk1, pclk2).
    These correspond to:
     - sysclk: frequency of the CPU
     - hclk: frequency of the AHB bus, core memory and DMA
     - pclk1: frequency of the APB1 bus
     - pclk2: frequency of the APB2 bus
    If given any arguments then the function sets the frequency of the CPU,
    and the busses if additional arguments are given.  Frequencies are given in
    Hz.  Eg freq(120000000) sets sysclk (the CPU frequency) to 120MHz.  Note that
    not all values are supported and the largest supported frequency not greater
    than the given value will be selected.
    Supported sysclk frequencies are (in MHz): 8, 16, 24, 30, 32, 36, 40, 42, 48,
    54, 56, 60, 64, 72, 84, 96, 108, 120, 144, 168.
    The maximum frequency of hclk is 168MHz, of pclk1 is 42MHz, and of pclk2 is
    84MHz.  Be sure not to set frequencies above these values.
    The hclk, pclk1 and pclk2 frequencies are derived from the sysclk frequency
    using a prescaler (divider).  Supported prescalers for hclk are: 1, 2, 4, 8,
    16, 64, 128, 256, 512.  Supported prescalers for pclk1 and pclk2 are: 1, 2,
    4, 8.  A prescaler will be chosen to best match the requested frequency.
    A sysclk frequency of
    8MHz uses the HSE (external crystal) directly and 16MHz uses the HSI
    (internal oscillator) directly.  The higher frequencies use the HSE to
    drive the PLL (phase locked loop), and then use the output of the PLL.
    Note that if you change the frequency while the USB is enabled then
    the USB may become unreliable.  It is best to change the frequency
    in boot.py, before the USB peripheral is started.  Also note that sysclk
    frequencies below 36MHz do not allow the USB to function correctly.
    """
    pass

def wfi():
    """
    Wait for an internal or external interrupt.
    This executes a ``wfi`` instruction which reduces power consumption
    of the MCU until any interrupt occurs (be it internal or external),
    at which point execution continues.  Note that the system-tick interrupt
    occurs once every millisecond (1000Hz) so this function will block for
    at most 1ms.
    """
    pass

def stop():
    """
    Put the pyboard in a "sleeping" state.
    This reduces power consumption to less than 500 uA.  To wake from this
    sleep state requires an external interrupt or a real-time-clock event.
    Upon waking execution continues where it left off.
    See :meth:`rtc.wakeup` to configure a real-time-clock wakeup event.
    """
    pass

def standby():
    """
    Put the pyboard into a "deep sleep" state.
    This reduces power consumption to less than 50 uA.  To wake from this
    sleep state requires a real-time-clock event, or an external interrupt
    on X1 (PA0=WKUP) or X18 (PC13=TAMP1).
    Upon waking the system undergoes a hard reset.
    See :meth:`rtc.wakeup` to configure a real-time-clock wakeup event.
    """
    pass

def have_cdc():
    """
    Return True if USB is connected as a serial device, False otherwise.
    .. note:: This function is deprecated.  Use pyb.USB_VCP().isconnected() instead.
    """
    pass

def hid((buttons, x, y, z)):
    """
    Takes a 4-tuple (or list) and sends it to the USB host (the PC) to
    signal a HID mouse-motion event.
    .. note:: This function is deprecated.  Use :meth:`pyb.USB_HID.send()` instead.
    """
    pass

def info([dump_alloc_table]):
    """
    Print out lots of information about the board.
    """
    pass

def main(filename):
    """
    Set the filename of the main script to run after boot.py is finished.  If
    this function is not called then the default file main.py will be executed.
    It only makes sense to call this function from within boot.py.
    """
    pass

def mount(device, mountpoint, \*, readonly=False, mkfs=False):
    """
    .. note:: This function is deprecated. Mounting and unmounting devices should
       be performed by :meth:`uos.mount` and :meth:`uos.umount` instead.
    Mount a block device and make it available as part of the filesystem.
    ``device`` must be an object that provides the block protocol. (The
    following is also deprecated. See :class:`uos.AbstractBlockDev` for the
    correct way to create a block device.)
     - ``readblocks(self, blocknum, buf)``
     - ``writeblocks(self, blocknum, buf)`` (optional)
     - ``count(self)``
     - ``sync(self)`` (optional)
    ``readblocks`` and ``writeblocks`` should copy data between ``buf`` and
    the block device, starting from block number ``blocknum`` on the device.
    ``buf`` will be a bytearray with length a multiple of 512.  If
    ``writeblocks`` is not defined then the device is mounted read-only.
    The return value of these two functions is ignored.
    ``count`` should return the number of blocks available on the device.
    ``sync``, if implemented, should sync the data on the device.
    The parameter ``mountpoint`` is the location in the root of the filesystem
    to mount the device.  It must begin with a forward-slash.
    If ``readonly`` is ``True``, then the device is mounted read-only,
    otherwise it is mounted read-write.
    If ``mkfs`` is ``True``, then a new filesystem is created if one does not
    already exist.
    """
    pass

def repl_uart(uart):
    """
    Get or set the UART object where the REPL is repeated on.
    """
    pass

def rng():
    """
    Return a 30-bit hardware generated random number.
    """
    pass

def sync():
    """
    Sync all file systems.
    """
    pass

def unique_id():
    """
    Returns a string of 12 bytes (96 bits), which is the unique ID of the MCU.
    """
    pass

def usb_mode([modestr], port=-1, vid=0xf055, pid=-1, msc=(), hid=pyb.hid_mouse, high_speed=False):
    """
    If called with no arguments, return the current USB mode as a string.
    If called with *modestr* provided, attempts to configure the USB mode.
    The following values of *modestr* are understood:
    - ``None``: disables USB
    - ``'VCP'``: enable with VCP (Virtual COM Port) interface
    - ``'MSC'``: enable with MSC (mass storage device class) interface
    - ``'VCP+MSC'``: enable with VCP and MSC
    - ``'VCP+HID'``: enable with VCP and HID (human interface device)
    - ``'VCP+MSC+HID'``: enabled with VCP, MSC and HID (only available on PYBD boards)
    For backwards compatibility, ``'CDC'`` is understood to mean
    ``'VCP'`` (and similarly for ``'CDC+MSC'`` and ``'CDC+HID'``).
    The *port* parameter should be an integer (0, 1, ...) and selects which
    USB port to use if the board supports multiple ports.  A value of -1 uses
    the default or automatically selected port.
    The *vid* and *pid* parameters allow you to specify the VID (vendor id)
    and PID (product id).  A *pid* value of -1 will select a PID based on the
    value of *modestr*.
    If enabling MSC mode, the *msc* parameter can be used to specify a list
    of SCSI LUNs to expose on the mass storage interface.  For example
    ``msc=(pyb.Flash(), pyb.SDCard())``.
    If enabling HID mode, you may also specify the HID details by
    passing the *hid* keyword parameter.  It takes a tuple of
    (subclass, protocol, max packet length, polling interval, report
    descriptor).  By default it will set appropriate values for a USB
    mouse.  There is also a ``pyb.hid_keyboard`` constant, which is an
    appropriate tuple for a USB keyboard.
    The *high_speed* parameter, when set to ``True``, enables USB HS mode if
    it is supported by the hardware.
    """
    pass


class ADC:
    """
    Usage::
     import pyb
     adc = pyb.ADC(pin)                  # create an analog object from a pin
     val = adc.read()                    # read an analog value
     adc = pyb.ADCAll(resolution)        # create an ADCAll object
     adc = pyb.ADCAll(resolution, mask)  # create an ADCAll object for selected analog channels
     val = adc.read_channel(channel)     # read the given channel
     val = adc.read_core_temp()          # read MCU temperature
     val = adc.read_core_vbat()          # read MCU VBAT
     val = adc.read_core_vref()          # read MCU VREF
     val = adc.read_vref()               # read MCU supply voltage
    """

    def read(self, )
        """
        Read the value on the analog pin and return it.  The returned value
        will be between 0 and 4095.
        """
         pass

    def read_timed(self, buf, timer)
        """
        Read analog values into ``buf`` at a rate set by the ``timer`` object.
        ``buf`` can be bytearray or array.array for example.  The ADC values have
        12-bit resolution and are stored directly into ``buf`` if its element size is
        16 bits or greater.  If ``buf`` has only 8-bit elements (eg a bytearray) then
        the sample resolution will be reduced to 8 bits.
        ``timer`` should be a Timer object, and a sample is read each time the timer
        triggers.  The timer must already be initialised and running at the desired
        sampling frequency.
        To support previous behaviour of this function, ``timer`` can also be an
        integer which specifies the frequency (in Hz) to sample at.  In this case
        Timer(6) will be automatically configured to run at the given frequency.
        Example using a Timer object (preferred way)::
            adc = pyb.ADC(pyb.Pin.board.X19)    # create an ADC on pin X19
            tim = pyb.Timer(6, freq=10)         # create a timer running at 10Hz
            buf = bytearray(100)                # creat a buffer to store the samples
            adc.read_timed(buf, tim)            # sample 100 values, taking 10s
        Example using an integer for the frequency::
            adc = pyb.ADC(pyb.Pin.board.X19)    # create an ADC on pin X19
            buf = bytearray(100)                # create a buffer of 100 bytes
            adc.read_timed(buf, 10)             # read analog values into buf at 10Hz
                                                #   this will take 10 seconds to finish
            for val in buf:                     # loop over all values
                print(val)                      # print the value out
        This function does not allocate any heap memory. It has blocking behaviour:
        it does not return to the calling program until the buffer is full.
        """
         pass

    def read_timed_multi(self, (self, adcx, adcy, ...), (self, bufx, bufy, ...), timer)
        """
        This is a static method. It can be used to extract relative timing or
        phase data from multiple ADC's.
        It reads analog values from multiple ADC's into buffers at a rate set by
        the *timer* object. Each time the timer triggers a sample is rapidly
        read from each ADC in turn.
        ADC and buffer instances are passed in tuples with each ADC having an
        associated buffer. All buffers must be of the same type and length and
        the number of buffers must equal the number of ADC's.
        Buffers can be ``bytearray`` or ``array.array`` for example. The ADC values
        have 12-bit resolution and are stored directly into the buffer if its element
        size is 16 bits or greater.  If buffers have only 8-bit elements (eg a
        ``bytearray``) then the sample resolution will be reduced to 8 bits.
        *timer* must be a Timer object. The timer must already be initialised
        and running at the desired sampling frequency.
        Example reading 3 ADC's::
            adc0 = pyb.ADC(pyb.Pin.board.X1)    # Create ADC's
            adc1 = pyb.ADC(pyb.Pin.board.X2)
            adc2 = pyb.ADC(pyb.Pin.board.X3)
            tim = pyb.Timer(8, freq=100)        # Create timer
            rx0 = array.array('H', (0 for i in range(100))) # ADC buffers of
            rx1 = array.array('H', (0 for i in range(100))) # 100 16-bit words
            rx2 = array.array('H', (0 for i in range(100)))
            # read analog values into buffers at 100Hz (takes one second)
            pyb.ADC.read_timed_multi((adc0, adc1, adc2), (rx0, rx1, rx2), tim)
            for n in range(len(rx0)):
                print(rx0[n], rx1[n], rx2[n])
        This function does not allocate any heap memory. It has blocking behaviour:
        it does not return to the calling program until the buffers are full.
        The function returns ``True`` if all samples were acquired with correct
        timing. At high sample rates the time taken to acquire a set of samples
        can exceed the timer period. In this case the function returns ``False``,
        indicating a loss of precision in the sample interval. In extreme cases
        samples may be missed.
        The maximum rate depends on factors including the data width and the
        number of ADC's being read. In testing two ADC's were sampled at a timer
        rate of 210kHz without overrun. Samples were missed at 215kHz.  For three
        ADC's the limit is around 140kHz, and for four it is around 110kHz.
        At high sample rates disabling interrupts for the duration can reduce the
        risk of sporadic data loss.
        """
         pass


class Accel:
    """
    Accel is an object that controls the accelerometer.  Example usage::
     accel = pyb.Accel()
     for i in range(10):
         print(accel.x(), accel.y(), accel.z())
    Raw values are between -32 and 31.
    """

    def filtered_xyz(self, )
        """
        Get a 3-tuple of filtered x, y and z values.
        Implementation note: this method is currently implemented as taking the
        sum of 4 samples, sampled from the 3 previous calls to this function along
        with the sample from the current call.  Returned values are therefore 4
        times the size of what they would be from the raw x(), y() and z() calls.
        """
         pass

    def tilt(self, )
        """
        Get the tilt register.
        """
         pass

    def x(self, )
        """
        Get the x-axis value.
        """
         pass

    def y(self, )
        """
        Get the y-axis value.
        """
         pass

    def z(self, )
        """
        Get the z-axis value.
        """
         pass


class CAN:
    """
    CAN implements the standard CAN communications protocol.  At
    the physical level it consists of 2 lines: RX and TX.  Note that
    to connect the pyboard to a CAN bus you must use a CAN transceiver
    to convert the CAN logic signals from the pyboard to the correct
    voltage levels on the bus.
    Example usage (works without anything connected)::
     from pyb import CAN
     can = CAN(1, CAN.LOOPBACK)
     can.setfilter(0, CAN.LIST16, 0, (123, 124, 125, 126))  # set a filter to receive messages with id=123, 124, 125 and 126
     can.send('message!', 123)   # send a message with id 123
     can.recv(0)                 # receive message on FIFO 0
    """

    def init(self, mode, extframe=False, prescaler=100, sjw=1, bs1=6, bs2=8, auto_restart=False)
        """
        Initialise the CAN bus with the given parameters:
          - *mode* is one of:  NORMAL, LOOPBACK, SILENT, SILENT_LOOPBACK
          - if *extframe* is True then the bus uses extended identifiers in the frames
            (29 bits); otherwise it uses standard 11 bit identifiers
          - *prescaler* is used to set the duration of 1 time quanta; the time quanta
            will be the input clock (PCLK1, see :meth:`pyb.freq()`) divided by the prescaler
          - *sjw* is the resynchronisation jump width in units of the time quanta;
            it can be 1, 2, 3, 4
          - *bs1* defines the location of the sample point in units of the time quanta;
            it can be between 1 and 1024 inclusive
          - *bs2* defines the location of the transmit point in units of the time quanta;
            it can be between 1 and 16 inclusive
          - *auto_restart* sets whether the controller will automatically try and restart
            communications after entering the bus-off state; if this is disabled then
            :meth:`~CAN.restart()` can be used to leave the bus-off state
        The time quanta tq is the basic unit of time for the CAN bus.  tq is the CAN
        prescaler value divided by PCLK1 (the frequency of internal peripheral bus 1);
        see :meth:`pyb.freq()` to determine PCLK1.
        A single bit is made up of the synchronisation segment, which is always 1 tq.
        Then follows bit segment 1, then bit segment 2.  The sample point is after bit
        segment 1 finishes.  The transmit point is after bit segment 2 finishes.
        The baud rate will be 1/bittime, where the bittime is 1 + BS1 + BS2 multiplied
        by the time quanta tq.
        For example, with PCLK1=42MHz, prescaler=100, sjw=1, bs1=6, bs2=8, the value of
        tq is 2.38 microseconds.  The bittime is 35.7 microseconds, and the baudrate
        is 28kHz.
        See page 680 of the STM32F405 datasheet for more details.
        """
         pass

    def deinit(self, )
        """
        Turn off the CAN bus.
        """
         pass

    def restart(self, )
        """
        Force a software restart of the CAN controller without resetting its
        configuration.
        If the controller enters the bus-off state then it will no longer participate
        in bus activity.  If the controller is not configured to automatically restart
        (see :meth:`~CAN.init()`) then this method can be used to trigger a restart,
        and the controller will follow the CAN protocol to leave the bus-off state and
        go into the error active state.
        """
         pass

    def state(self, )
        """
        Return the state of the controller.  The return value can be one of:
        - ``CAN.STOPPED`` -- the controller is completely off and reset;
        - ``CAN.ERROR_ACTIVE`` -- the controller is on and in the Error Active state
          (both TEC and REC are less than 96);
        - ``CAN.ERROR_WARNING`` -- the controller is on and in the Error Warning state
          (at least one of TEC or REC is 96 or greater);
        - ``CAN.ERROR_PASSIVE`` -- the controller is on and in the Error Passive state
          (at least one of TEC or REC is 128 or greater);
        - ``CAN.BUS_OFF`` -- the controller is on but not participating in bus activity
          (TEC overflowed beyond 255).
        """
         pass

    def info(self, [list])
        """
        Get information about the controller's error states and TX and RX buffers.
        If *list* is provided then it should be a list object with at least 8 entries,
        which will be filled in with the information.  Otherwise a new list will be
        created and filled in.  In both cases the return value of the method is the
        populated list.
        The values in the list are:
        - TEC value
        - REC value
        - number of times the controller enterted the Error Warning state (wrapped
          around to 0 after 65535)
        - number of times the controller enterted the Error Passive state (wrapped
          around to 0 after 65535)
        - number of times the controller enterted the Bus Off state (wrapped
          around to 0 after 65535)
        - number of pending TX messages
        - number of pending RX messages on fifo 0
        - number of pending RX messages on fifo 1
        """
         pass

    def setfilter(self, bank, mode, fifo, params, rtr)
        """
        Configure a filter bank:
        - *bank* is the filter bank that is to be configured.
        - *mode* is the mode the filter should operate in.
        - *fifo* is which fifo (0 or 1) a message should be stored in, if it is accepted by this filter.
        - *params* is an array of values the defines the filter. The contents of the array depends on the *mode* argument.
        +-----------+---------------------------------------------------------+
        |*mode*     |contents of *params* array                               |
        +===========+=========================================================+
        |CAN.LIST16 |Four 16 bit ids that will be accepted                    |
        +-----------+---------------------------------------------------------+
        |CAN.LIST32 |Two 32 bit ids that will be accepted                     |
        +-----------+---------------------------------------------------------+
        |CAN.MASK16 |Two 16 bit id/mask pairs. E.g. (1, 3, 4, 4)              |
        |           | | The first pair, 1 and 3 will accept all ids           |
        |           | | that have bit 0 = 1 and bit 1 = 0.                    |
        |           | | The second pair, 4 and 4, will accept all ids         |
        |           | | that have bit 2 = 1.                                  |
        +-----------+---------------------------------------------------------+
        |CAN.MASK32 |As with CAN.MASK16 but with only one 32 bit id/mask pair.|
        +-----------+---------------------------------------------------------+
        - *rtr* is an array of booleans that states if a filter should accept a
          remote transmission request message.  If this argument is not given
          then it defaults to ``False`` for all entries.  The length of the array
          depends on the *mode* argument.
        +-----------+----------------------+
        |*mode*     |length of *rtr* array |
        +===========+======================+
        |CAN.LIST16 |4                     |
        +-----------+----------------------+
        |CAN.LIST32 |2                     |
        +-----------+----------------------+
        |CAN.MASK16 |2                     |
        +-----------+----------------------+
        |CAN.MASK32 |1                     |
        +-----------+----------------------+
        """
         pass

    def clearfilter(self, bank)
        """
        Clear and disables a filter bank:
        - *bank* is the filter bank that is to be cleared.
        """
         pass

    def any(self, fifo)
        """
        Return ``True`` if any message waiting on the FIFO, else ``False``.
        """
         pass

    def recv(self, fifo, list=None, timeout=5000)
        """
        Receive data on the bus:
          - *fifo* is an integer, which is the FIFO to receive on
          - *list* is an optional list object to be used as the return value
          - *timeout* is the timeout in milliseconds to wait for the receive.
        Return value: A tuple containing four values.
          - The id of the message.
          - A boolean that indicates if the message is an RTR message.
          - The FMI (Filter Match Index) value.
          - An array containing the data.
        If *list* is ``None`` then a new tuple will be allocated, as well as a new
        bytes object to contain the data (as the fourth element in the tuple).
        If *list* is not ``None`` then it should be a list object with a least four
        elements.  The fourth element should be a memoryview object which is created
        from either a bytearray or an array of type 'B' or 'b', and this array must
        have enough room for at least 8 bytes.  The list object will then be
        populated with the first three return values above, and the memoryview object
        will be resized inplace to the size of the data and filled in with that data.
        The same list and memoryview objects can be reused in subsequent calls to
        this method, providing a way of receiving data without using the heap.
        For example::
             buf = bytearray(8)
             lst = [0, 0, 0, memoryview(buf)]
             # No heap memory is allocated in the following call
             can.recv(0, lst)
        """
         pass

    def send(self, data, id, timeout=0, rtr=False)
        """
        Send a message on the bus:
          - *data* is the data to send (an integer to send, or a buffer object).
          - *id* is the id of the message to be sent.
          - *timeout* is the timeout in milliseconds to wait for the send.
          - *rtr* is a boolean that specifies if the message shall be sent as
            a remote transmission request.  If *rtr* is True then only the length
            of *data* is used to fill in the DLC slot of the frame; the actual
            bytes in *data* are unused.
          If timeout is 0 the message is placed in a buffer in one of three hardware
          buffers and the method returns immediately. If all three buffers are in use
          an exception is thrown. If timeout is not 0, the method waits until the
          message is transmitted. If the message can't be transmitted within the
          specified time an exception is thrown.
        Return value: ``None``.
        """
         pass

    def rxcallback(self, fifo, fun)
        """
        Register a function to be called when a message is accepted into a empty fifo:
        - *fifo* is the receiving fifo.
        - *fun* is the function to be called when the fifo becomes non empty.
        The callback function takes two arguments the first is the can object it self the second is
        a integer that indicates the reason for the callback.
        +--------+------------------------------------------------+
        | Reason |                                                |
        +========+================================================+
        | 0      | A message has been accepted into a empty FIFO. |
        +--------+------------------------------------------------+
        | 1      | The FIFO is full                               |
        +--------+------------------------------------------------+
        | 2      | A message has been lost due to a full FIFO     |
        +--------+------------------------------------------------+
        Example use of rxcallback::
          def cb0(bus, reason):
            print('cb0')
            if reason == 0:
                print('pending')
            if reason == 1:
                print('full')
            if reason == 2:
                print('overflow')
          can = CAN(1, CAN.LOOPBACK)
          can.rxcallback(0, cb0)
        """
         pass


class DAC:
    """
    The DAC is used to output analog values (a specific voltage) on pin X5 or pin X6.
    The voltage will be between 0 and 3.3V.
    *This module will undergo changes to the API.*
    Example usage::
     from pyb import DAC
     dac = DAC(1)            # create DAC 1 on pin X5
     dac.write(128)          # write a value to the DAC (makes X5 1.65V)
     dac = DAC(1, bits=12)   # use 12 bit resolution
     dac.write(4095)         # output maximum value, 3.3V
    To output a continuous sine-wave::
     import math
     from pyb import DAC
     # create a buffer containing a sine-wave
     buf = bytearray(100)
     for i in range(len(buf)):
         buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))
     # output the sine-wave at 400Hz
     dac = DAC(1)
     dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
    To output a continuous sine-wave at 12-bit resolution::
     import math
     from array import array
     from pyb import DAC
     # create a buffer containing a sine-wave, using half-word samples
     buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i / 128)) for i in range(128))
     # output the sine-wave at 400Hz
     dac = DAC(1, bits=12)
     dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)
    """

    def init(self, bits=8, buffering=None)
        """
        Reinitialise the DAC.  *bits* can be 8 or 12.  *buffering* can be
        ``None``, ``False`` or ``True``; see above constructor for the meaning
        of this parameter.
        """
         pass

    def deinit(self, )
        """
        De-initialise the DAC making its pin available for other uses.
        """
         pass

    def noise(self, freq)
        """
        Generate a pseudo-random noise signal.  A new random sample is written
        to the DAC output at the given frequency.
        """
         pass

    def triangle(self, freq)
        """
        Generate a triangle wave.  The value on the DAC output changes at the given
        frequency and ramps through the full 12-bit range (up and down). Therefore
        the frequency of the repeating triangle wave itself is 8192 times smaller.
        """
         pass

    def write(self, value)
        """
        Direct access to the DAC output.  The minimum value is 0.  The maximum
        value is 2\*\*``bits``-1, where ``bits`` is set when creating the DAC
        object or by using the ``init`` method.
        """
         pass

    def write_timed(self, data, freq, mode=
        """
        Initiates a burst of RAM to DAC using a DMA transfer.
        The input data is treated as an array of bytes in 8-bit mode, and
        an array of unsigned half-words (array typecode 'H') in 12-bit mode.
        ``freq`` can be an integer specifying the frequency to write the DAC
        samples at, using Timer(6).  Or it can be an already-initialised
        Timer object which is used to trigger the DAC sample.  Valid timers
        are 2, 4, 5, 6, 7 and 8.
        ``mode`` can be ``DAC.NORMAL`` or ``DAC.CIRCULAR``.
        Example using both DACs at the same time::
          dac1 = DAC(1)
          dac2 = DAC(2)
          dac1.write_timed(buf1, pyb.Timer(6, freq=100), mode=DAC.CIRCULAR)
          dac2.write_timed(buf2, pyb.Timer(7, freq=200), mode=DAC.CIRCULAR)
        """
         pass


class ExtInt:
    """
    There are a total of 22 interrupt lines. 16 of these can come from GPIO pins
    and the remaining 6 are from internal sources.
    For lines 0 through 15, a given line can map to the corresponding line from an
    arbitrary port. So line 0 can map to Px0 where x is A, B, C, ... and
    line 1 can map to Px1 where x is A, B, C, ... ::
     def callback(line):
         print("line =", line)
    Note: ExtInt will automatically configure the gpio line as an input. ::
     extint = pyb.ExtInt(pin, pyb.ExtInt.IRQ_FALLING, pyb.Pin.PULL_UP, callback)
    Now every time a falling edge is seen on the X1 pin, the callback will be
    called. Caution: mechanical pushbuttons have "bounce" and pushing or
    releasing a switch will often generate multiple edges.
    See: http://www.eng.utah.edu/~cs5780/debouncing.pdf for a detailed
    explanation, along with various techniques for debouncing.
    Trying to register 2 callbacks onto the same pin will throw an exception.
    If pin is passed as an integer, then it is assumed to map to one of the
    internal interrupt sources, and must be in the range 16 through 22.
    All other pin objects go through the pin mapper to come up with one of the
    gpio pins. ::
     extint = pyb.ExtInt(pin, mode, pull, callback)
    Valid modes are pyb.ExtInt.IRQ_RISING, pyb.ExtInt.IRQ_FALLING,
    pyb.ExtInt.IRQ_RISING_FALLING, pyb.ExtInt.EVT_RISING,
    pyb.ExtInt.EVT_FALLING, and pyb.ExtInt.EVT_RISING_FALLING.
    Only the IRQ_xxx modes have been tested. The EVT_xxx modes have
    something to do with sleep mode and the WFE instruction.
    Valid pull values are pyb.Pin.PULL_UP, pyb.Pin.PULL_DOWN, pyb.Pin.PULL_NONE.
    There is also a C API, so that drivers which require EXTI interrupt lines
    can also use this code. See extint.h for the available functions and
    usrsw.h for an example of using this.
    """

    def disable(self, )
        """
        Disable the interrupt associated with the ExtInt object.
        This could be useful for debouncing.
        """
         pass

    def enable(self, )
        """
        Enable a disabled interrupt.
        """
         pass

    def line(self, )
        """
        Return the line number that the pin is mapped to.
        """
         pass

    def swint(self, )
        """
        Trigger the callback from software.
        """
         pass


class Flash:
    """
    The Flash class allows direct access to the primary flash device on the pyboard.
    In most cases, to store persistent data on the device, you'll want to use a
    higher-level abstraction, for example the filesystem via Python's standard file
    API, but this interface is useful to :ref:`customise the filesystem
    configuration <filesystem>` or implement a low-level storage system for your
    application.
    """

    def readblocks(self, block_num, buf)
        """
         These methods implement the simple and :ref:`extended
         <block-device-interface>` block protocol defined by
         :class:`uos.AbstractBlockDev`.
        """
         pass

    def readblocks(self, block_num, buf, offset)
        """
         These methods implement the simple and :ref:`extended
         <block-device-interface>` block protocol defined by
         :class:`uos.AbstractBlockDev`.
        """
         pass

    def writeblocks(self, block_num, buf)
        """
         These methods implement the simple and :ref:`extended
         <block-device-interface>` block protocol defined by
         :class:`uos.AbstractBlockDev`.
        """
         pass

    def writeblocks(self, block_num, buf, offset)
        """
         These methods implement the simple and :ref:`extended
         <block-device-interface>` block protocol defined by
         :class:`uos.AbstractBlockDev`.
        """
         pass

    def ioctl(self, cmd, arg)
        """
         These methods implement the simple and :ref:`extended
         <block-device-interface>` block protocol defined by
         :class:`uos.AbstractBlockDev`.
        """
         pass


class I2C:
    """
    I2C is a two-wire protocol for communicating between devices.  At the physical
    level it consists of 2 wires: SCL and SDA, the clock and data lines respectively.
    I2C objects are created attached to a specific bus.  They can be initialised
    when created, or initialised later on.
    Example::
     from pyb import I2C
     i2c = I2C(1)                         # create on bus 1
     i2c = I2C(1, I2C.MASTER)             # create and init as a master
     i2c.init(I2C.MASTER, baudrate=20000) # init as a master
     i2c.init(I2C.SLAVE, addr=0x42)       # init as a slave with given address
     i2c.deinit()                         # turn off the peripheral
    Printing the i2c object gives you information about its configuration.
    The basic methods are send and recv::
     i2c.send('abc')      # send 3 bytes
     i2c.send(0x42)       # send a single byte, given by the number
     data = i2c.recv(3)   # receive 3 bytes
    To receive inplace, first create a bytearray::
     data = bytearray(3)  # create a buffer
     i2c.recv(data)       # receive 3 bytes, writing them into data
    You can specify a timeout (in ms)::
     i2c.send(b'123', timeout=2000)   # timeout after 2 seconds
    A master must specify the recipient's address::
     i2c.init(I2C.MASTER)
     i2c.send('123', 0x42)        # send 3 bytes to slave with address 0x42
     i2c.send(b'456', addr=0x42)  # keyword for address
    Master also has other methods::
     i2c.is_ready(0x42)           # check if slave 0x42 is ready
     i2c.scan()                   # scan for slaves on the bus, returning
                                  #   a list of valid addresses
     i2c.mem_read(3, 0x42, 2)     # read 3 bytes from memory of slave 0x42,
                                  #   starting at address 2 in the slave
     i2c.mem_write('abc', 0x42, 2, timeout=1000) # write 'abc' (3 bytes) to memory of slave 0x42
                                                 # starting at address 2 in the slave, timeout after 1 second
    """

    def deinit(self, )
        """
        Turn off the I2C bus.
        """
         pass

    def init(self, mode, addr=0x12, baudrate=400000, gencall=False, dma=False)
        """
          Initialise the I2C bus with the given parameters:
          - ``mode`` must be either ``I2C.MASTER`` or ``I2C.SLAVE``
          - ``addr`` is the 7-bit address (only sensible for a slave)
          - ``baudrate`` is the SCL clock rate (only sensible for a master)
          - ``gencall`` is whether to support general call mode
          - ``dma`` is whether to allow the use of DMA for the I2C transfers (note
            that DMA transfers have more precise timing but currently do not handle bus
            errors properly)
        """
         pass

    def is_ready(self, addr)
        """
        Check if an I2C device responds to the given address.  Only valid when in master mode.
        """
         pass

    def mem_read(self, data, addr, memaddr, timeout=5000, addr_size=8)
        """
        Read from the memory of an I2C device:
          - ``data`` can be an integer (number of bytes to read) or a buffer to read into
          - ``addr`` is the I2C device address
          - ``memaddr`` is the memory location within the I2C device
          - ``timeout`` is the timeout in milliseconds to wait for the read
          - ``addr_size`` selects width of memaddr: 8 or 16 bits
        Returns the read data.
        This is only valid in master mode.
        """
         pass

    def mem_write(self, data, addr, memaddr, timeout=5000, addr_size=8)
        """
        Write to the memory of an I2C device:
          - ``data`` can be an integer or a buffer to write from
          - ``addr`` is the I2C device address
          - ``memaddr`` is the memory location within the I2C device
          - ``timeout`` is the timeout in milliseconds to wait for the write
          - ``addr_size`` selects width of memaddr: 8 or 16 bits
        Returns ``None``.
        This is only valid in master mode.
        """
         pass

    def recv(self, recv, addr=0x00, timeout=5000)
        """
        Receive data on the bus:
          - ``recv`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes
          - ``addr`` is the address to receive from (only required in master mode)
          - ``timeout`` is the timeout in milliseconds to wait for the receive
        Return value: if ``recv`` is an integer then a new buffer of the bytes received,
        otherwise the same buffer that was passed in to ``recv``.
        """
         pass

    def send(self, send, addr=0x00, timeout=5000)
        """
        Send data on the bus:
          - ``send`` is the data to send (an integer to send, or a buffer object)
          - ``addr`` is the address to send to (only required in master mode)
          - ``timeout`` is the timeout in milliseconds to wait for the send
        Return value: ``None``.
        """
         pass

    def scan(self, )
        """
        Scan all I2C addresses from 0x01 to 0x7f and return a list of those that respond.
        Only valid when in master mode.
        """
         pass


class LCD:
    """
    The LCD class is used to control the LCD on the LCD touch-sensor pyskin,
    LCD32MKv1.0.  The LCD is a 128x32 pixel monochrome screen, part NHD-C12832A1Z.
    The pyskin must be connected in either the X or Y positions, and then
    an LCD object is made using::
     lcd = pyb.LCD('X')      # if pyskin is in the X position
     lcd = pyb.LCD('Y')      # if pyskin is in the Y position
    Then you can use::
     lcd.light(True)                 # turn the backlight on
     lcd.write('Hello world!\n')     # print text to the screen
    This driver implements a double buffer for setting/getting pixels.
    For example, to make a bouncing dot, try::
     x = y = 0
     dx = dy = 1
     while True:
         # update the dot's position
         x += dx
         y += dy
         # make the dot bounce of the edges of the screen
         if x <= 0 or x >= 127: dx = -dx
         if y <= 0 or y >= 31: dy = -dy
         lcd.fill(0)                 # clear the buffer
         lcd.pixel(x, y, 1)          # draw the dot
         lcd.show()                  # show the buffer
         pyb.delay(50)               # pause for 50ms
    """

    def command(self, instr_data, buf)
        """
        Send an arbitrary command to the LCD.  Pass 0 for ``instr_data`` to send an
        instruction, otherwise pass 1 to send data.  ``buf`` is a buffer with the
        instructions/data to send.
        """
         pass

    def contrast(self, value)
        """
        Set the contrast of the LCD.  Valid values are between 0 and 47.
        """
         pass

    def fill(self, colour)
        """
        Fill the screen with the given colour (0 or 1 for white or black).
        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
         pass

    def get(self, x, y)
        """
        Get the pixel at the position ``(x, y)``.  Returns 0 or 1.
        This method reads from the visible buffer.
        """
         pass

    def light(self, value)
        """
        Turn the backlight on/off.  True or 1 turns it on, False or 0 turns it off.
        """
         pass

    def pixel(self, x, y, colour)
        """
        Set the pixel at ``(x, y)`` to the given colour (0 or 1).
        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
         pass

    def show(self, )
        """
        Show the hidden buffer on the screen.
        """
         pass

    def text(self, str, x, y, colour)
        """
        Draw the given text to the position ``(x, y)`` using the given colour (0 or 1).
        This method writes to the hidden buffer.  Use ``show()`` to show the buffer.
        """
         pass

    def write(self, str)
        """
        Write the string ``str`` to the screen.  It will appear immediately.
        """
         pass


class LED:
    """
    The LED object controls an individual LED (Light Emitting Diode).
    """

    def intensity(self, [value])
        """
        Get or set the LED intensity.  Intensity ranges between 0 (off) and 255 (full on).
        If no argument is given, return the LED intensity.
        If an argument is given, set the LED intensity and return ``None``.
        *Note:* Only LED(3) and LED(4) can have a smoothly varying intensity, and
        they use timer PWM to implement it.  LED(3) uses Timer(2) and LED(4) uses
        Timer(3).  These timers are only configured for PWM if the intensity of the
        relevant LED is set to a value between 1 and 254.  Otherwise the timers are
        free for general purpose use.
        """
         pass

    def off(self, )
        """
        Turn the LED off.
        """
         pass

    def on(self, )
        """
        Turn the LED on, to maximum intensity.
        """
         pass

    def toggle(self, )
        """
        Toggle the LED between on (maximum intensity) and off.  If the LED is at
        non-zero intensity then it is considered "on" and toggle will turn it off.
        """
         pass


class Pin:
    """
    A pin is the basic object to control I/O pins.  It has methods to set
    the mode of the pin (input, output, etc) and methods to get and set the
    digital logic level. For analog control of a pin, see the ADC class.
    Usage Model:
    All Board Pins are predefined as pyb.Pin.board.Name::
     x1_pin = pyb.Pin.board.X1
     g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN)
    CPU pins which correspond to the board pins are available
    as ``pyb.Pin.cpu.Name``. For the CPU pins, the names are the port letter
    followed by the pin number. On the PYBv1.0, ``pyb.Pin.board.X1`` and
    ``pyb.Pin.cpu.A0`` are the same pin.
    You can also use strings::
     g = pyb.Pin('X1', pyb.Pin.OUT_PP)
    Users can add their own names::
     MyMapperDict = { 'LeftMotorDir' : pyb.Pin.cpu.C12 }
     pyb.Pin.dict(MyMapperDict)
     g = pyb.Pin("LeftMotorDir", pyb.Pin.OUT_OD)
    and can query mappings::
     pin = pyb.Pin("LeftMotorDir")
    Users can also add their own mapping function::
     def MyMapper(pin_name):
        if pin_name == "LeftMotorDir":
            return pyb.Pin.cpu.A0
     pyb.Pin.mapper(MyMapper)
    So, if you were to call: ``pyb.Pin("LeftMotorDir", pyb.Pin.OUT_PP)``
    then ``"LeftMotorDir"`` is passed directly to the mapper function.
    To summarise, the following order determines how things get mapped into
    an ordinal pin number:
    1. Directly specify a pin object
    2. User supplied mapping function
    3. User supplied mapping (object must be usable as a dictionary key)
    4. Supply a string which matches a board pin
    5. Supply a string which matches a CPU port/pin
    You can set ``pyb.Pin.debug(True)`` to get some debug information about
    how a particular object gets mapped to a pin.
    When a pin has the ``Pin.PULL_UP`` or ``Pin.PULL_DOWN`` pull-mode enabled,
    that pin has an effective 40k Ohm resistor pulling it to 3V3 or GND
    respectively (except pin Y5 which has 11k Ohm resistors).
    Now every time a falling edge is seen on the gpio pin, the callback will be
    executed. Caution: mechanical push buttons have "bounce" and pushing or
    releasing a switch will often generate multiple edges.
    See: http://www.eng.utah.edu/~cs5780/debouncing.pdf for a detailed
    explanation, along with various techniques for debouncing.
    All pin objects go through the pin mapper to come up with one of the
    gpio pins.
    """

    def init(self, mode, pull=
        """
        Initialise the pin:
          - ``mode`` can be one of:
             - ``Pin.IN`` - configure the pin for input;
             - ``Pin.OUT_PP`` - configure the pin for output, with push-pull control;
             - ``Pin.OUT_OD`` - configure the pin for output, with open-drain control;
             - ``Pin.AF_PP`` - configure the pin for alternate function, pull-pull;
             - ``Pin.AF_OD`` - configure the pin for alternate function, open-drain;
             - ``Pin.ANALOG`` - configure the pin for analog.
          - ``pull`` can be one of:
             - ``Pin.PULL_NONE`` - no pull up or down resistors;
             - ``Pin.PULL_UP`` - enable the pull-up resistor;
             - ``Pin.PULL_DOWN`` - enable the pull-down resistor.
          - when mode is ``Pin.AF_PP`` or ``Pin.AF_OD``, then af can be the index or name
            of one of the alternate functions associated with a pin.
        Returns: ``None``.
        """
         pass

    def value(self, [value])
        """
        Get or set the digital logic level of the pin:
          - With no argument, return 0 or 1 depending on the logic level of the pin.
          - With ``value`` given, set the logic level of the pin.  ``value`` can be
            anything that converts to a boolean.  If it converts to ``True``, the pin
            is set high, otherwise it is set low.
        """
         pass

    def __str__(self, )
        """
        Return a string describing the pin object.
        """
         pass

    def af(self, )
        """
        Returns the currently configured alternate-function of the pin. The
        integer returned will match one of the allowed constants for the af
        argument to the init function.
        """
         pass

    def af_list(self, )
        """
        Returns an array of alternate functions available for this pin.
        """
         pass

    def gpio(self, )
        """
        Returns the base address of the GPIO block associated with this pin.
        """
         pass

    def mode(self, )
        """
        Returns the currently configured mode of the pin. The integer returned
        will match one of the allowed constants for the mode argument to the init
        function.
        """
         pass

    def name(self, )
        """
        Get the pin name.
        """
         pass

    def names(self, )
        """
        Returns the cpu and board names for this pin.
        """
         pass

    def pin(self, )
        """
        Get the pin number.
        """
         pass

    def port(self, )
        """
        Get the pin port.
        """
         pass

    def pull(self, )
        """
         Returns the currently configured pull of the pin. The integer returned
         will match one of the allowed constants for the pull argument to the init
         function.
        """
         pass


class PinAF:
    """
    A Pin represents a physical pin on the microprocessor. Each pin
    can have a variety of functions (GPIO, I2C SDA, etc). Each PinAF
    object represents a particular function for a pin.
    Usage Model::
     x3 = pyb.Pin.board.X3
     x3_af = x3.af_list()
    x3_af will now contain an array of PinAF objects which are available on
    pin X3.
    For the pyboard, x3_af would contain:
     [Pin.AF1_TIM2, Pin.AF2_TIM5, Pin.AF3_TIM9, Pin.AF7_USART2]
    Normally, each peripheral would configure the af automatically, but sometimes
    the same function is available on multiple pins, and having more control
    is desired.
    To configure X3 to expose TIM2_CH3, you could use::
    pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.AF_PP, af=pyb.Pin.AF1_TIM2)
    or::
    pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.AF_PP, af=1)
    """


class RTC:
    """
    The RTC is and independent clock that keeps track of the date
    and time.
    Example usage::
     rtc = pyb.RTC()
     rtc.datetime((2014, 5, 1, 4, 13, 0, 0, 0))
     print(rtc.datetime())
    """

    def datetime(self, [datetimetuple])
        """
        Get or set the date and time of the RTC.
        With no arguments, this method returns an 8-tuple with the current
        date and time.  With 1 argument (being an 8-tuple) it sets the date
        and time (and ``subseconds`` is reset to 255).
        The 8-tuple has the following format:
            (year, month, day, weekday, hours, minutes, seconds, subseconds)
        ``weekday`` is 1-7 for Monday through Sunday.
        ``subseconds`` counts down from 255 to 0
        """
         pass

    def wakeup(self, timeout, callback=None)
        """
        Set the RTC wakeup timer to trigger repeatedly at every ``timeout``
        milliseconds.  This trigger can wake the pyboard from both the sleep
        states: :meth:`pyb.stop` and :meth:`pyb.standby`.
        If ``timeout`` is ``None`` then the wakeup timer is disabled.
        If ``callback`` is given then it is executed at every trigger of the
        wakeup timer.  ``callback`` must take exactly one argument.
        """
         pass

    def info(self, )
        """
        Get information about the startup time and reset source.
         - The lower 0xffff are the number of milliseconds the RTC took to
           start up.
         - Bit 0x10000 is set if a power-on reset occurred.
         - Bit 0x20000 is set if an external reset occurred
        """
         pass

    def calibration(self, cal)
        """
        Get or set RTC calibration.
        With no arguments, ``calibration()`` returns the current calibration
        value, which is an integer in the range [-511 : 512].  With one
        argument it sets the RTC calibration.
        The RTC Smooth Calibration mechanism adjusts the RTC clock rate by
        adding or subtracting the given number of ticks from the 32768 Hz
        clock over a 32 second period (corresponding to 2^20 clock ticks.)
        Each tick added will speed up the clock by 1 part in 2^20, or 0.954
        ppm; likewise the RTC clock it slowed by negative values. The
        usable calibration range is:
        (-511 * 0.954) ~= -487.5 ppm up to (512 * 0.954) ~= 488.5 ppm
        """
         pass


class SPI:
    """
    SPI is a serial protocol that is driven by a master.  At the physical level
    there are 3 lines: SCK, MOSI, MISO.
    See usage model of I2C; SPI is very similar.  Main difference is
    parameters to init the SPI bus::
     from pyb import SPI
     spi = SPI(1, SPI.MASTER, baudrate=600000, polarity=1, phase=0, crc=0x7)
    Only required parameter is mode, SPI.MASTER or SPI.SLAVE.  Polarity can be
    0 or 1, and is the level the idle clock line sits at.  Phase can be 0 or 1
    to sample data on the first or second clock edge respectively.  Crc can be
    None for no CRC, or a polynomial specifier.
    Additional methods for SPI::
     data = spi.send_recv(b'1234')        # send 4 bytes and receive 4 bytes
     buf = bytearray(4)
     spi.send_recv(b'1234', buf)          # send 4 bytes and receive 4 into buf
     spi.send_recv(buf, buf)              # send/recv 4 bytes from/to buf
    """

    def deinit(self, )
        """
        Turn off the SPI bus.
        """
         pass

    def init(self, mode, baudrate=328125, prescaler, polarity=1, phase=0, bits=8, firstbit=
        """
        Initialise the SPI bus with the given parameters:
          - ``mode`` must be either ``SPI.MASTER`` or ``SPI.SLAVE``.
          - ``baudrate`` is the SCK clock rate (only sensible for a master).
          - ``prescaler`` is the prescaler to use to derive SCK from the APB bus frequency;
            use of ``prescaler`` overrides ``baudrate``.
          - ``polarity`` can be 0 or 1, and is the level the idle clock line sits at.
          - ``phase`` can be 0 or 1 to sample data on the first or second clock edge
            respectively.
          - ``bits`` can be 8 or 16, and is the number of bits in each transferred word.
          - ``firstbit`` can be ``SPI.MSB`` or ``SPI.LSB``.
          - ``crc`` can be None for no CRC, or a polynomial specifier.
        Note that the SPI clock frequency will not always be the requested baudrate.
        The hardware only supports baudrates that are the APB bus frequency
        (see :meth:`pyb.freq`) divided by a prescaler, which can be 2, 4, 8, 16, 32,
        64, 128 or 256.  SPI(1) is on AHB2, and SPI(2) is on AHB1.  For precise
        control over the SPI clock frequency, specify ``prescaler`` instead of
        ``baudrate``.
        Printing the SPI object will show you the computed baudrate and the chosen
        prescaler.
        """
         pass

    def recv(self, recv, timeout=5000)
        """
        Receive data on the bus:
          - ``recv`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.
        Return value: if ``recv`` is an integer then a new buffer of the bytes received,
        otherwise the same buffer that was passed in to ``recv``.
        """
         pass

    def send(self, send, timeout=5000)
        """
        Send data on the bus:
          - ``send`` is the data to send (an integer to send, or a buffer object).
          - ``timeout`` is the timeout in milliseconds to wait for the send.
        Return value: ``None``.
        """
         pass

    def send_recv(self, send, recv=None, timeout=5000)
        """
        Send and receive data on the bus at the same time:
          - ``send`` is the data to send (an integer to send, or a buffer object).
          - ``recv`` is a mutable buffer which will be filled with received bytes.
            It can be the same as ``send``, or omitted.  If omitted, a new buffer will
            be created.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.
        Return value: the buffer with the received bytes.
        """
         pass


class Servo:
    """
    Servo objects control standard hobby servo motors with 3-wires (ground, power,
    signal).  There are 4 positions on the pyboard where these motors can be plugged
    in: pins X1 through X4 are the signal pins, and next to them are 4 sets of power
    and ground pins.
    Example usage::
     import pyb
     s1 = pyb.Servo(1)   # create a servo object on position X1
     s2 = pyb.Servo(2)   # create a servo object on position X2
     s1.angle(45)        # move servo 1 to 45 degrees
     s2.angle(0)         # move servo 2 to 0 degrees
     # move servo1 and servo2 synchronously, taking 1500ms
     s1.angle(-60, 1500)
     s2.angle(30, 1500)
    """

    def angle(self, [angle, time=0])
        """
        If no arguments are given, this function returns the current angle.
        If arguments are given, this function sets the angle of the servo:
          - ``angle`` is the angle to move to in degrees.
          - ``time`` is the number of milliseconds to take to get to the specified
            angle.  If omitted, then the servo moves as quickly as possible to its
            new position.
        """
         pass

    def speed(self, [speed, time=0])
        """
        If no arguments are given, this function returns the current speed.
        If arguments are given, this function sets the speed of the servo:
          - ``speed`` is the speed to change to, between -100 and 100.
          - ``time`` is the number of milliseconds to take to get to the specified
            speed.  If omitted, then the servo accelerates as quickly as possible.
        """
         pass

    def pulse_width(self, [value])
        """
        If no arguments are given, this function returns the current raw pulse-width
        value.
        If an argument is given, this function sets the raw pulse-width value.
        """
         pass

    def calibration(self, [pulse_min, pulse_max, pulse_centre, [pulse_angle_90, pulse_speed_100]])
        """
        If no arguments are given, this function returns the current calibration
        data, as a 5-tuple.
        If arguments are given, this function sets the timing calibration:
          - ``pulse_min`` is the minimum allowed pulse width.
          - ``pulse_max`` is the maximum allowed pulse width.
          - ``pulse_centre`` is the pulse width corresponding to the centre/zero position.
          - ``pulse_angle_90`` is the pulse width corresponding to 90 degrees.
          - ``pulse_speed_100`` is the pulse width corresponding to a speed of 100.
        """
         pass


class Switch:
    """
    A Switch object is used to control a push-button switch.
    Usage::
      sw = pyb.Switch()       # create a switch object
      sw.value()              # get state (True if pressed, False otherwise)
      sw()                    # shorthand notation to get the switch state
      sw.callback(f)          # register a callback to be called when the
                              #   switch is pressed down
      sw.callback(None)       # remove the callback
    Example::
      pyb.Switch().callback(lambda: pyb.LED(1).toggle())
    """

    def __call__(self, )
        """
        Call switch object directly to get its state: ``True`` if pressed down,
        ``False`` otherwise.
        """
         pass

    def value(self, )
        """
        Get the switch state.  Returns ``True`` if pressed down, otherwise ``False``.
        """
         pass

    def callback(self, fun)
        """
        Register the given function to be called when the switch is pressed down.
        If ``fun`` is ``None``, then it disables the callback.
        """
         pass


class Timer:
    """
    Timers can be used for a great variety of tasks.  At the moment, only
    the simplest case is implemented: that of calling a function periodically.
    Each timer consists of a counter that counts up at a certain rate.  The rate
    at which it counts is the peripheral clock frequency (in Hz) divided by the
    timer prescaler.  When the counter reaches the timer period it triggers an
    event, and the counter resets back to zero.  By using the callback method,
    the timer event can call a Python function.
    Example usage to toggle an LED at a fixed frequency::
     tim = pyb.Timer(4)              # create a timer object using timer 4
     tim.init(freq=2)                # trigger at 2Hz
     tim.callback(lambda t:pyb.LED(1).toggle())
    Example using named function for the callback::
     def tick(timer):                # we will receive the timer object when being called
         print(timer.counter())      # show current timer's counter value
     tim = pyb.Timer(4, freq=1)      # create a timer object using timer 4 - trigger at 1Hz
     tim.callback(tick)              # set the callback to our tick function
    Further examples::
     tim = pyb.Timer(4, freq=100)    # freq in Hz
     tim = pyb.Timer(4, prescaler=0, period=99)
     tim.counter()                   # get counter (can also set)
     tim.prescaler(2)                # set prescaler (can also get)
     tim.period(199)                 # set period (can also get)
     tim.callback(lambda t: ...)     # set callback for update interrupt (t=tim instance)
     tim.callback(None)              # clear callback
    *Note:* Timer(2) and Timer(3) are used for PWM to set the intensity of LED(3)
    and LED(4) respectively.  But these timers are only configured for PWM if
    the intensity of the relevant LED is set to a value between 1 and 254.  If
    the intensity feature of the LEDs is not used then these timers are free for
    general purpose use.  Similarly, Timer(5) controls the servo driver, and
    Timer(6) is used for timed ADC/DAC reading/writing.  It is recommended to
    use the other timers in your programs.
    *Note:* Memory can't be allocated during a callback (an interrupt) and so
    exceptions raised within a callback don't give much information.  See
    :func:`micropython.alloc_emergency_exception_buf` for how to get around this
    limitation.
    """

    def init(self, \*, freq, prescaler, period)
        """
        Initialise the timer.  Initialisation must be either by frequency (in Hz)
        or by prescaler and period::
            tim.init(freq=100)                  # set the timer to trigger at 100Hz
            tim.init(prescaler=83, period=999)  # set the prescaler and period directly
        Keyword arguments:
          - ``freq`` --- specifies the periodic frequency of the timer. You might also
            view this as the frequency with which the timer goes through one complete cycle.
          - ``prescaler`` [0-0xffff] - specifies the value to be loaded into the
            timer's Prescaler Register (PSC). The timer clock source is divided by
            (``prescaler + 1``) to arrive at the timer clock. Timers 2-7 and 12-14
            have a clock source of 84 MHz (pyb.freq()[2] \* 2), and Timers 1, and 8-11
            have a clock source of 168 MHz (pyb.freq()[3] \* 2).
          - ``period`` [0-0xffff] for timers 1, 3, 4, and 6-15. [0-0x3fffffff] for timers 2 & 5.
            Specifies the value to be loaded into the timer's AutoReload
            Register (ARR). This determines the period of the timer (i.e. when the
            counter cycles). The timer counter will roll-over after ``period + 1``
            timer clock cycles.
          - ``mode`` can be one of:
            - ``Timer.UP`` - configures the timer to count from 0 to ARR (default)
            - ``Timer.DOWN`` - configures the timer to count from ARR down to 0.
            - ``Timer.CENTER`` - configures the timer to count from 0 to ARR and
              then back down to 0.
          - ``div`` can be one of 1, 2, or 4. Divides the timer clock to determine
            the sampling clock used by the digital filters.
          - ``callback`` - as per Timer.callback()
          - ``deadtime`` - specifies the amount of "dead" or inactive time between
            transitions on complimentary channels (both channels will be inactive)
            for this time). ``deadtime`` may be an integer between 0 and 1008, with
            the following restrictions: 0-128 in steps of 1. 128-256 in steps of
            2, 256-512 in steps of 8, and 512-1008 in steps of 16. ``deadtime``
            measures ticks of ``source_freq`` divided by ``div`` clock ticks.
            ``deadtime`` is only available on timers 1 and 8.
         You must either specify freq or both of period and prescaler.
        """
         pass

    def deinit(self, )
        """
        Deinitialises the timer.
        Disables the callback (and the associated irq).
        Disables any channel callbacks (and the associated irq).
        Stops the timer, and disables the timer peripheral.
        """
         pass

    def callback(self, fun)
        """
        Set the function to be called when the timer triggers.
        ``fun`` is passed 1 argument, the timer object.
        If ``fun`` is ``None`` then the callback will be disabled.
        """
         pass

    def channel(self, channel, mode, ...)
        """
        If only a channel number is passed, then a previously initialized channel
        object is returned (or ``None`` if there is no previous channel).
        Otherwise, a TimerChannel object is initialized and returned.
        Each channel can be configured to perform pwm, output compare, or
        input capture. All channels share the same underlying timer, which means
        that they share the same timer clock.
        Keyword arguments:
          - ``mode`` can be one of:
            - ``Timer.PWM`` --- configure the timer in PWM mode (active high).
            - ``Timer.PWM_INVERTED`` --- configure the timer in PWM mode (active low).
            - ``Timer.OC_TIMING`` --- indicates that no pin is driven.
            - ``Timer.OC_ACTIVE`` --- the pin will be made active when a compare match occurs (active is determined by polarity)
            - ``Timer.OC_INACTIVE`` --- the pin will be made inactive when a compare match occurs.
            - ``Timer.OC_TOGGLE`` --- the pin will be toggled when an compare match occurs.
            - ``Timer.OC_FORCED_ACTIVE`` --- the pin is forced active (compare match is ignored).
            - ``Timer.OC_FORCED_INACTIVE`` --- the pin is forced inactive (compare match is ignored).
            - ``Timer.IC`` --- configure the timer in Input Capture mode.
            - ``Timer.ENC_A`` --- configure the timer in Encoder mode. The counter only changes when CH1 changes.
            - ``Timer.ENC_B`` --- configure the timer in Encoder mode. The counter only changes when CH2 changes.
            - ``Timer.ENC_AB`` --- configure the timer in Encoder mode. The counter changes when CH1 or CH2 changes.
          - ``callback`` - as per TimerChannel.callback()
          - ``pin`` None (the default) or a Pin object. If specified (and not None)
            this will cause the alternate function of the the indicated pin
            to be configured for this timer channel. An error will be raised if
            the pin doesn't support any alternate functions for this timer channel.
        Keyword arguments for Timer.PWM modes:
          - ``pulse_width`` - determines the initial pulse width value to use.
          - ``pulse_width_percent`` - determines the initial pulse width percentage to use.
        Keyword arguments for Timer.OC modes:
          - ``compare`` - determines the initial value of the compare register.
          - ``polarity`` can be one of:
            - ``Timer.HIGH`` - output is active high
            - ``Timer.LOW`` - output is active low
        Optional keyword arguments for Timer.IC modes:
          - ``polarity`` can be one of:
            - ``Timer.RISING`` - captures on rising edge.
            - ``Timer.FALLING`` - captures on falling edge.
            - ``Timer.BOTH`` - captures on both edges.
          Note that capture only works on the primary channel, and not on the
          complimentary channels.
        Notes for Timer.ENC modes:
          - Requires 2 pins, so one or both pins will need to be configured to use
            the appropriate timer AF using the Pin API.
          - Read the encoder value using the timer.counter() method.
          - Only works on CH1 and CH2 (and not on CH1N or CH2N)
          - The channel number is ignored when setting the encoder mode.
        PWM Example::
            timer = pyb.Timer(2, freq=1000)
            ch2 = timer.channel(2, pyb.Timer.PWM, pin=pyb.Pin.board.X2, pulse_width=8000)
            ch3 = timer.channel(3, pyb.Timer.PWM, pin=pyb.Pin.board.X3, pulse_width=16000)
        """
         pass

    def counter(self, [value])
        """
        Get or set the timer counter.
        """
         pass

    def freq(self, [value])
        """
        Get or set the frequency for the timer (changes prescaler and period if set).
        """
         pass

    def period(self, [value])
        """
        Get or set the period of the timer.
        """
         pass

    def prescaler(self, [value])
        """
        Get or set the prescaler for the timer.
        """
         pass

    def source_freq(self, )
        """
        Get the frequency of the source of the timer.
        class TimerChannel --- setup a channel for a timer
        ==================================================
        Timer channels are used to generate/capture a signal using a timer.
        TimerChannel objects are created using the Timer.channel() method.
        """
         pass


class TimerChannel:
    """
    Timer channels are used to generate/capture a signal using a timer.
    TimerChannel objects are created using the Timer.channel() method.
    """


class UART:
    """
    UART implements the standard UART/USART duplex serial communications protocol.  At
    the physical level it consists of 2 lines: RX and TX.  The unit of communication
    is a character (not to be confused with a string character) which can be 8 or 9
    bits wide.
    UART objects can be created and initialised using::
     from pyb import UART
     uart = UART(1, 9600)                         # init with given baudrate
     uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters
    Bits can be 7, 8 or 9.  Parity can be None, 0 (even) or 1 (odd).  Stop can be 1 or 2.
    *Note:* with parity=None, only 8 and 9 bits are supported.  With parity enabled,
    only 7 and 8 bits are supported.
    A UART object acts like a `stream` object and reading and writing is done
    using the standard stream methods::
     uart.read(10)       # read 10 characters, returns a bytes object
     uart.read()         # read all available characters
     uart.readline()     # read a line
     uart.readinto(buf)  # read and store into the given buffer
     uart.write('abc')   # write the 3 characters
    Individual characters can be read/written using::
     uart.readchar()     # read 1 character and returns it as an integer
     uart.writechar(42)  # write 1 character
    To check if there is anything to be read, use::
     uart.any()          # returns the number of characters waiting
    *Note:* The stream functions ``read``, ``write``, etc. are new in MicroPython v1.3.4.
    Earlier versions use ``uart.send`` and ``uart.recv``.
    """

    def init(self, baudrate, bits=8, parity=None, stop=1, timeout=0, flow=0, timeout_char=0, read_buf_len=64)
        """
        Initialise the UART bus with the given parameters:
          - ``baudrate`` is the clock rate.
          - ``bits`` is the number of bits per character, 7, 8 or 9.
          - ``parity`` is the parity, ``None``, 0 (even) or 1 (odd).
          - ``stop`` is the number of stop bits, 1 or 2.
          - ``flow`` sets the flow control type. Can be 0, ``UART.RTS``, ``UART.CTS``
            or ``UART.RTS | UART.CTS``.
          - ``timeout`` is the timeout in milliseconds to wait for writing/reading the first character.
          - ``timeout_char`` is the timeout in milliseconds to wait between characters while writing or reading.
          - ``read_buf_len`` is the character length of the read buffer (0 to disable).
        This method will raise an exception if the baudrate could not be set within
        5% of the desired value.  The minimum baudrate is dictated by the frequency
        of the bus that the UART is on; UART(1) and UART(6) are APB2, the rest are on
        APB1.  The default bus frequencies give a minimum baudrate of 1300 for
        UART(1) and UART(6) and 650 for the others.  Use :func:`pyb.freq <pyb.freq>`
        to reduce the bus frequencies to get lower baudrates.
        *Note:* with parity=None, only 8 and 9 bits are supported.  With parity enabled,
        only 7 and 8 bits are supported.
        """
         pass

    def deinit(self, )
        """
        Turn off the UART bus.
        """
         pass

    def any(self, )
        """
        Returns the number of bytes waiting (may be 0).
        """
         pass

    def read(self, [nbytes])
        """
        Read characters.  If ``nbytes`` is specified then read at most that many bytes.
        If ``nbytes`` are available in the buffer, returns immediately, otherwise returns
        when sufficient characters arrive or the timeout elapses.
        If ``nbytes`` is not given then the method reads as much data as possible.  It
        returns after the timeout has elapsed.
        *Note:* for 9 bit characters each character takes two bytes, ``nbytes`` must
        be even, and the number of characters is ``nbytes/2``.
        Return value: a bytes object containing the bytes read in.  Returns ``None``
        on timeout.
        """
         pass

    def readchar(self, )
        """
        Receive a single character on the bus.
        Return value: The character read, as an integer.  Returns -1 on timeout.
        """
         pass

    def readinto(self, buf[, nbytes])
        """
        Read bytes into the ``buf``.  If ``nbytes`` is specified then read at most
        that many bytes.  Otherwise, read at most ``len(buf)`` bytes.
        Return value: number of bytes read and stored into ``buf`` or ``None`` on
        timeout.
        """
         pass

    def readline(self, )
        """
        Read a line, ending in a newline character. If such a line exists, return is
        immediate. If the timeout elapses, all available data is returned regardless
        of whether a newline exists.
        Return value: the line read or ``None`` on timeout if no data is available.
        """
         pass

    def write(self, buf)
        """
        Write the buffer of bytes to the bus.  If characters are 7 or 8 bits wide
        then each byte is one character.  If characters are 9 bits wide then two
        bytes are used for each character (little endian), and ``buf`` must contain
        an even number of bytes.
        Return value: number of bytes written. If a timeout occurs and no bytes
        were written returns ``None``.
        """
         pass

    def writechar(self, char)
        """
        Write a single character on the bus.  ``char`` is an integer to write.
        Return value: ``None``. See note below if CTS flow control is used.
        """
         pass

    def sendbreak(self, )
        """
        Send a break condition on the bus.  This drives the bus low for a duration
        of 13 bits.
        Return value: ``None``.
        """
         pass


class USB_HID:
    """
    The USB_HID class allows creation of an object representing the USB
    Human Interface Device (HID) interface.  It can be used to emulate
    a peripheral such as a mouse or keyboard.
    Before you can use this class, you need to use :meth:`pyb.usb_mode()` to set the USB mode to include the HID interface.
    """

    def recv(self, data, timeout=5000)
        """
        Receive data on the bus:
          - ``data`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.
        Return value: if ``data`` is an integer then a new buffer of the bytes received,
        otherwise the number of bytes read into ``data`` is returned.
        """
         pass

    def send(self, data)
        """
        Send data over the USB HID interface:
          - ``data`` is the data to send (a tuple/list of integers, or a
            bytearray).
        """
         pass


class USB_VCP:
    """
    The USB_VCP class allows creation of a `stream`-like object representing the USB
    virtual comm port.  It can be used to read and write data over USB to
    the connected host.
    """

    def init(self, \*, flow=-1)
        """
        Configure the USB VCP port.  If the *flow* argument is not -1 then the value sets
        the flow control, which can be a bitwise-or of ``USB_VCP.RTS`` and ``USB_VCP.CTS``.
        RTS is used to control read behaviour and CTS, to control write behaviour.
        """
         pass

    def setinterrupt(self, chr)
        """
        Set the character which interrupts running Python code.  This is set
        to 3 (CTRL-C) by default, and when a CTRL-C character is received over
        the USB VCP port, a KeyboardInterrupt exception is raised.
        Set to -1 to disable this interrupt feature.  This is useful when you
        want to send raw bytes over the USB VCP port.
        """
         pass

    def isconnected(self, )
        """
        Return ``True`` if USB is connected as a serial device, else ``False``.
        """
         pass

    def any(self, )
        """
        Return ``True`` if any characters waiting, else ``False``.
        """
         pass

    def close(self, )
        """
        This method does nothing.  It exists so the USB_VCP object can act as
        a file.
        """
         pass

    def read(self, [nbytes])
        """
        Read at most ``nbytes`` from the serial device and return them as a
        bytes object.  If ``nbytes`` is not specified then the method reads
        all available bytes from the serial device.
        USB_VCP `stream` implicitly works in non-blocking mode,
        so if no pending data available, this method will return immediately
        with ``None`` value.
        """
         pass

    def readinto(self, buf, [maxlen])
        """
        Read bytes from the serial device and store them into ``buf``, which
        should be a buffer-like object.  At most ``len(buf)`` bytes are read.
        If ``maxlen`` is given and then at most ``min(maxlen, len(buf))`` bytes
        are read.
        Returns the number of bytes read and stored into ``buf`` or ``None``
        if no pending data available.
        """
         pass

    def readline(self, )
        """
        Read a whole line from the serial device.
        Returns a bytes object containing the data, including the trailing
        newline character or ``None`` if no pending data available.
        """
         pass

    def readlines(self, )
        """
        Read as much data as possible from the serial device, breaking it into
        lines.
        Returns a list of bytes objects, each object being one of the lines.
        Each line will include the newline character.
        """
         pass

    def write(self, buf)
        """
        Write the bytes from ``buf`` to the serial device.
        Returns the number of bytes written.
        """
         pass

    def recv(self, data, timeout=5000)
        """
        Receive data on the bus:
          - ``data`` can be an integer, which is the number of bytes to receive,
            or a mutable buffer, which will be filled with received bytes.
          - ``timeout`` is the timeout in milliseconds to wait for the receive.
        Return value: if ``data`` is an integer then a new buffer of the bytes received,
        otherwise the number of bytes read into ``data`` is returned.
        """
         pass

    def send(self, data, timeout=5000)
        """
        Send data over the USB VCP:
          - ``data`` is the data to send (an integer to send, or a buffer object).
          - ``timeout`` is the timeout in milliseconds to wait for the send.
        Return value: number of bytes sent.
        """
         pass

