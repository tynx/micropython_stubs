"""
|see_cpython_module| :mod:`python:hashlib`.
This module implements binary data hashing algorithms. The exact inventory
of available algorithms depends on a board. Among the algorithms which may
be implemented:
* SHA256 - The current generation, modern hashing algorithm (of SHA2 series).
  It is suitable for cryptographically-secure purposes. Included in the
  MicroPython core and any board is recommended to provide this, unless
  it has particular code size constraints.
* SHA1 - A previous generation algorithm. Not recommended for new usages,
  but SHA1 is a part of number of Internet standards and existing
  applications, so boards targeting network connectivity and
  interoperability will try to provide this.
* MD5 - A legacy algorithm, not considered cryptographically secure. Only
  selected boards, targeting interoperability with legacy applications,
  will offer this.
"""

