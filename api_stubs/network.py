"""
This module provides network drivers and routing configuration. To use this
module, a MicroPython variant/build with network capabilities must be installed.
Network drivers for specific hardware are available within this module and are
used to configure hardware network interface(s). Network services provided
by configured interfaces are then available for use via the :mod:`usocket`
module.
For example::
 # connect/ show IP config a specific network interface
 # see below for examples of specific drivers
 import network
 import utime
 nic = network.Driver(...)
 if not nic.isconnected():
     nic.connect()
     print("Waiting for connection...")
     while not nic.isconnected():
         utime.sleep(1)
 print(nic.ifconfig())
 # now use usocket as usual
 import usocket as socket
 addr = socket.getaddrinfo('micropython.org', 80)[0][-1]
 s = socket.socket()
 s.connect(addr)
 s.send(b'GET / HTTP/1.1\r\nHost: micropython.org\r\n\r\n')
 data = s.recv(1000)
 s.close()
Common network adapter interface
================================
This section describes an (implied) abstract base class for all network
interface classes implemented by `MicroPython ports <MicroPython port>`
for different hardware. This means that MicroPython does not actually
provide ``AbstractNIC`` class, but any actual NIC class, as described
in the following sections, implements methods as described here.

"""

def phy_mode([mode]):
    """
     Get or set the PHY mode.
     If the *mode* parameter is provided, sets the mode to its value. If
     the function is called without parameters, returns the current mode.
     The possible modes are defined as constants:
         * ``MODE_11B`` -- IEEE 802.11b,
         * ``MODE_11G`` -- IEEE 802.11g,
         * ``MODE_11N`` -- IEEE 802.11n.
     Availability: ESP8266.
    """
    pass


class CC3K:
    """
    This class provides a driver for CC3000 WiFi modules.  Example usage::
     import network
     nic = network.CC3K(pyb.SPI(2), pyb.Pin.board.Y5, pyb.Pin.board.Y4, pyb.Pin.board.Y3)
     nic.connect('your-ssid', 'your-password')
     while not nic.isconnected():
         pyb.delay(50)
     print(nic.ifconfig())
     # now use socket as usual
     ...
    For this example to work the CC3000 module must have the following connections:
     - MOSI connected to Y8
     - MISO connected to Y7
     - CLK connected to Y6
     - CS connected to Y5
     - VBEN connected to Y4
     - IRQ connected to Y3
    It is possible to use other SPI busses and other pins for CS, VBEN and IRQ.
    """

    def __init__(self, spi, pin_cs, pin_en, pin_irq):
        """
        Create a CC3K driver object, initialise the CC3000 module using the given SPI bus
        and pins, and return the CC3K object.
        Arguments are:
          - *spi* is an :ref:`SPI object <pyb.SPI>` which is the SPI bus that the CC3000 is
            connected to (the MOSI, MISO and CLK pins).
          - *pin_cs* is a :ref:`Pin object <pyb.Pin>` which is connected to the CC3000 CS pin.
          - *pin_en* is a :ref:`Pin object <pyb.Pin>` which is connected to the CC3000 VBEN pin.
          - *pin_irq* is a :ref:`Pin object <pyb.Pin>` which is connected to the CC3000 IRQ pin.
        All of these objects will be initialised by the driver, so there is no need to
        initialise them yourself.  For example, you can use::
          nic = network.CC3K(pyb.SPI(2), pyb.Pin.board.Y5, pyb.Pin.board.Y4, pyb.Pin.board.Y3)
        """
         pass

    def connect(self, ssid, key=None, security=WPA2, bssid=None)
        """
        Connect to a WiFi access point using the given SSID, and other security
        parameters.
        """
         pass

    def disconnect(self, )
        """
        Disconnect from the WiFi access point.
        """
         pass

    def isconnected(self, )
        """
        Returns True if connected to a WiFi access point and has a valid IP address,
        False otherwise.
        """
         pass

    def ifconfig(self, )
        """
        Returns a 7-tuple with (ip, subnet mask, gateway, DNS server, DHCP server,
        MAC address, SSID).
        """
         pass

    def patch_version(self, )
        """
        Return the version of the patch program (firmware) on the CC3000.
        """
         pass

    def patch_program(self, 'pgm')
        """
        Upload the current firmware to the CC3000.  You must pass 'pgm' as the first
        argument in order for the upload to proceed.
        """
         pass


class WIZNET5K:
    """
    This class allows you to control WIZnet5x00 Ethernet adaptors based on
    the W5200 and W5500 chipsets.  The particular chipset that is supported
    by the firmware is selected at compile-time via the MICROPY_PY_WIZNET5K
    option.
    Example usage::
     import network
     nic = network.WIZNET5K(pyb.SPI(1), pyb.Pin.board.X5, pyb.Pin.board.X4)
     print(nic.ifconfig())
     # now use socket as usual
     ...
    For this example to work the WIZnet5x00 module must have the following connections:
     - MOSI connected to X8
     - MISO connected to X7
     - SCLK connected to X6
     - nSS connected to X5
     - nRESET connected to X4
    It is possible to use other SPI busses and other pins for nSS and nRESET.
    """

    def __init__(self, spi, pin_cs, pin_rst):
        """
        Create a WIZNET5K driver object, initialise the WIZnet5x00 module using the given
        SPI bus and pins, and return the WIZNET5K object.
        Arguments are:
          - *spi* is an :ref:`SPI object <pyb.SPI>` which is the SPI bus that the WIZnet5x00 is
            connected to (the MOSI, MISO and SCLK pins).
          - *pin_cs* is a :ref:`Pin object <pyb.Pin>` which is connected to the WIZnet5x00 nSS pin.
          - *pin_rst* is a :ref:`Pin object <pyb.Pin>` which is connected to the WIZnet5x00 nRESET pin.
        All of these objects will be initialised by the driver, so there is no need to
        initialise them yourself.  For example, you can use::
          nic = network.WIZNET5K(pyb.SPI(1), pyb.Pin.board.X5, pyb.Pin.board.X4)
        """
         pass

    def isconnected(self, )
        """
        Returns ``True`` if the physical Ethernet link is connected and up.
        Returns ``False`` otherwise.
        """
         pass

    def ifconfig(self, [(self, ip, subnet, gateway, dns)])
        """
        Get/set IP address, subnet mask, gateway and DNS.
        When called with no arguments, this method returns a 4-tuple with the above information.
        To set the above values, pass a 4-tuple with the required information.  For example::
         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
         pass

    def regs(self, )
        """
        Dump the WIZnet5x00 registers.  Useful for debugging.
        """
         pass


class WLAN:
    """
    This class provides a driver for WiFi network processors.  Example usage::
     import network
     # enable station interface and connect to WiFi access point
     nic = network.WLAN(network.STA_IF)
     nic.active(True)
     nic.connect('your-ssid', 'your-password')
     # now use sockets as usual
    """

    def __init__(self, interface_id):
        """
        Create a WLAN network interface object. Supported interfaces are
        ``network.STA_IF`` (station aka client, connects to upstream WiFi access
        points) and ``network.AP_IF`` (access point, allows other WiFi clients to
        connect). Availability of the methods below depends on interface type.
        For example, only STA interface may `WLAN.connect()` to an access point.
        """
         pass

    def active(self, [is_active])
        """
         Activate ("up") or deactivate ("down") network interface, if boolean
         argument is passed. Otherwise, query current state if no argument is
         provided. Most other methods require active interface.
        """
         pass

    def connect(self, ssid=None, password=None, bssid=None)
        """
         Connect to the specified wireless network, using the specified password.
         If *bssid* is given then the connection will be restricted to the
         access-point with that MAC address (the *ssid* must also be specified
         in this case).
        """
         pass

    def disconnect(self, )
        """
         Disconnect from the currently connected wireless network.
        """
         pass

    def scan(self, )
        """
         Scan for the available wireless networks.
         Scanning is only possible on STA interface. Returns list of tuples with
         the information about WiFi access points:
             (ssid, bssid, channel, RSSI, authmode, hidden)
         *bssid* is hardware address of an access point, in binary form, returned as
         bytes object. You can use `ubinascii.hexlify()` to convert it to ASCII form.
         There are five values for authmode:
             * 0 -- open
             * 1 -- WEP
             * 2 -- WPA-PSK
             * 3 -- WPA2-PSK
             * 4 -- WPA/WPA2-PSK
         and two for hidden:
             * 0 -- visible
             * 1 -- hidden
        """
         pass

    def status(self, [param])
        """
         Return the current status of the wireless connection.
         When called with no argument the return value describes the network link status.
         The possible statuses are defined as constants:
             * ``STAT_IDLE`` -- no connection and no activity,
             * ``STAT_CONNECTING`` -- connecting in progress,
             * ``STAT_WRONG_PASSWORD`` -- failed due to incorrect password,
             * ``STAT_NO_AP_FOUND`` -- failed because no access point replied,
             * ``STAT_CONNECT_FAIL`` -- failed due to other problems,
             * ``STAT_GOT_IP`` -- connection successful.
         When called with one argument *param* should be a string naming the status
         parameter to retrieve.  Supported parameters in WiFI STA mode are: ``'rssi'``.
        """
         pass

    def isconnected(self, )
        """
         In case of STA mode, returns ``True`` if connected to a WiFi access
         point and has a valid IP address.  In AP mode returns ``True`` when a
         station is connected. Returns ``False`` otherwise.
        """
         pass

    def ifconfig(self, [(self, ip, subnet, gateway, dns)])
        """
        Get/set IP-level network interface parameters: IP address, subnet mask,
        gateway and DNS server. When called with no arguments, this method returns
        a 4-tuple with the above information. To set the above values, pass a
        4-tuple with the required information.  For example::
         nic.ifconfig(('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
         pass

    def config(self, 'param')
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `WLAN.ifconfig()`). These include network-specific and hardware-specific
        parameters. For setting parameters, keyword argument syntax should be used,
        multiple parameters can be set at once. For querying, parameters name should
        be quoted as a string, and only one parameter can be queries at time::
         # Set WiFi access point name (formally known as ESSID) and WiFi channel
         ap.config(essid='My AP', channel=11)
         # Query params one by one
         print(ap.config('essid'))
         print(ap.config('channel'))
        Following are commonly supported parameters (availability of a specific parameter
        depends on network technology type, driver, and `MicroPython port`).
        =============  ===========
        Parameter      Description
        =============  ===========
        mac            MAC address (bytes)
        essid          WiFi access point name (string)
        channel        WiFi channel (integer)
        hidden         Whether ESSID is hidden (boolean)
        authmode       Authentication mode supported (enumeration, see module constants)
        password       Access password (string)
        dhcp_hostname  The DHCP hostname to use
        =============  ===========
        """
         pass

    def config(self, param=value, ...)
        """
        Get or set general network interface parameters. These methods allow to work
        with additional parameters beyond standard IP configuration (as dealt with by
        `WLAN.ifconfig()`). These include network-specific and hardware-specific
        parameters. For setting parameters, keyword argument syntax should be used,
        multiple parameters can be set at once. For querying, parameters name should
        be quoted as a string, and only one parameter can be queries at time::
         # Set WiFi access point name (formally known as ESSID) and WiFi channel
         ap.config(essid='My AP', channel=11)
         # Query params one by one
         print(ap.config('essid'))
         print(ap.config('channel'))
        Following are commonly supported parameters (availability of a specific parameter
        depends on network technology type, driver, and `MicroPython port`).
        =============  ===========
        Parameter      Description
        =============  ===========
        mac            MAC address (bytes)
        essid          WiFi access point name (string)
        channel        WiFi channel (integer)
        hidden         Whether ESSID is hidden (boolean)
        authmode       Authentication mode supported (enumeration, see module constants)
        password       Access password (string)
        dhcp_hostname  The DHCP hostname to use
        =============  ===========
        """
         pass


class WLANWiPy:
    """
    .. note::
     This class is a non-standard WLAN implementation for the WiPy.
     It is available simply as ``network.WLAN`` on the WiPy but is named in the
     documentation below as ``network.WLANWiPy`` to distinguish it from the
     more general :ref:`network.WLAN <network.WLAN>` class.
    This class provides a driver for the WiFi network processor in the WiPy. Example usage::
     import network
     import time
     # setup as a station
     wlan = network.WLAN(mode=WLAN.STA)
     wlan.connect('your-ssid', auth=(WLAN.WPA2, 'your-key'))
     while not wlan.isconnected():
         time.sleep_ms(50)
     print(wlan.ifconfig())
     # now use socket as usual
     ...
    """

    def __init__(self, id=0, ...):
        """
        Create a WLAN object, and optionally configure it. See `init()` for params of configuration.
        """
         pass

    def init(self, mode, ssid, auth, channel, antenna)
        """
        Set or get the WiFi network processor configuration.
        Arguments are:
          - *mode* can be either ``WLAN.STA`` or ``WLAN.AP``.
          - *ssid* is a string with the ssid name. Only needed when mode is ``WLAN.AP``.
          - *auth* is a tuple with (sec, key). Security can be ``None``, ``WLAN.WEP``,
            ``WLAN.WPA`` or ``WLAN.WPA2``. The key is a string with the network password.
            If ``sec`` is ``WLAN.WEP`` the key must be a string representing hexadecimal
            values (e.g. 'ABC1DE45BF'). Only needed when mode is ``WLAN.AP``.
          - *channel* a number in the range 1-11. Only needed when mode is ``WLAN.AP``.
          - *antenna* selects between the internal and the external antenna. Can be either
            ``WLAN.INT_ANT`` or ``WLAN.EXT_ANT``.
        For example, you can do::
           # create and configure as an access point
           wlan.init(mode=WLAN.AP, ssid='wipy-wlan', auth=(WLAN.WPA2,'www.wipy.io'), channel=7, antenna=WLAN.INT_ANT)
        or::
           # configure as an station
           wlan.init(mode=WLAN.STA)
        """
         pass

    def connect(self, ssid, auth=None, bssid=None, timeout=None)
        """
        Connect to a WiFi access point using the given SSID, and other security
        parameters.
           - *auth* is a tuple with (sec, key). Security can be ``None``, ``WLAN.WEP``,
             ``WLAN.WPA`` or ``WLAN.WPA2``. The key is a string with the network password.
             If ``sec`` is ``WLAN.WEP`` the key must be a string representing hexadecimal
             values (e.g. 'ABC1DE45BF').
           - *bssid* is the MAC address of the AP to connect to. Useful when there are several
             APs with the same ssid.
           - *timeout* is the maximum time in milliseconds to wait for the connection to succeed.
        """
         pass

    def scan(self, )
        """
        Performs a network scan and returns a list of named tuples with (ssid, bssid, sec, channel, rssi).
        Note that channel is always ``None`` since this info is not provided by the WiPy.
        """
         pass

    def disconnect(self, )
        """
        Disconnect from the WiFi access point.
        """
         pass

    def isconnected(self, )
        """
        In case of STA mode, returns ``True`` if connected to a WiFi access point and has a valid IP address.
        In AP mode returns ``True`` when a station is connected, ``False`` otherwise.
        """
         pass

    def ifconfig(self, if_id=0, config=['dhcp' or configtuple])
        """
        With no parameters given returns a 4-tuple of *(ip, subnet_mask, gateway, DNS_server)*.
        if ``'dhcp'`` is passed as a parameter then the DHCP client is enabled and the IP params
        are negotiated with the AP.
        If the 4-tuple config is given then a static IP is configured. For instance::
           wlan.ifconfig(config=('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))
        """
         pass

    def mode(self, [mode])
        """
        Get or set the WLAN mode.
        """
         pass

    def ssid(self, [ssid])
        """
        Get or set the SSID when in AP mode.
        """
         pass

    def auth(self, [auth])
        """
        Get or set the authentication type when in AP mode.
        """
         pass

    def channel(self, [channel])
        """
        Get or set the channel (only applicable in AP mode).
        """
         pass

    def antenna(self, [antenna])
        """
        Get or set the antenna type (external or internal).
        """
         pass

    def mac(self, [mac_addr])
        """
        Get or set a 6-byte long bytes object with the MAC address.
        """
         pass

    def irq(self, \*, handler, wake)
        """
         Create a callback to be triggered when a WLAN event occurs during ``machine.SLEEP``
         mode. Events are triggered by socket activity or by WLAN connection/disconnection.
             - *handler* is the function that gets called when the IRQ is triggered.
             - *wake* must be ``machine.SLEEP``.
         Returns an IRQ object.
        """
         pass

