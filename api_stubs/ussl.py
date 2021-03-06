"""
|see_cpython_module| :mod:`python:ssl`.
This module provides access to Transport Layer Security (previously and
widely known as “Secure Sockets Layer”) encryption and peer authentication
facilities for network sockets, both client-side and server-side.
"""

def ussl.wrap_socket(sock, server_side=False, keyfile=None, certfile=None, cert_reqs=CERT_NONE, ca_certs=None):
    """
    Takes a `stream` *sock* (usually usocket.socket instance of ``SOCK_STREAM`` type),
    and returns an instance of ssl.SSLSocket, which wraps the underlying stream in
    an SSL context. Returned object has the usual `stream` interface methods like
    ``read()``, ``write()``, etc. In MicroPython, the returned object does not expose
    socket interface and methods like ``recv()``, ``send()``. In particular, a
    server-side SSL socket should be created from a normal socket returned from
    :meth:`~usocket.socket.accept()` on a non-SSL listening server socket.
    Depending on the underlying module implementation in a particular
    `MicroPython port`, some or all keyword arguments above may be not supported.
    """
    pass

