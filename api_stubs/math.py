"""
|see_cpython_module| :mod:`python:math`.
The ``math`` module provides some basic mathematical functions for
working with floating-point numbers.
*Note:* On the pyboard, floating-point numbers have 32-bit precision.
Availability: not available on WiPy. Floating point support required
for this module.
"""

def acos(x):
    """
    Return the inverse cosine of ``x``.
    """
    pass

def acosh(x):
    """
    Return the inverse hyperbolic cosine of ``x``.
    """
    pass

def asin(x):
    """
    Return the inverse sine of ``x``.
    """
    pass

def asinh(x):
    """
    Return the inverse hyperbolic sine of ``x``.
    """
    pass

def atan(x):
    """
    Return the inverse tangent of ``x``.
    """
    pass

def atan2(y, x):
    """
    Return the principal value of the inverse tangent of ``y/x``.
    """
    pass

def atanh(x):
    """
    Return the inverse hyperbolic tangent of ``x``.
    """
    pass

def ceil(x):
    """
    Return an integer, being ``x`` rounded towards positive infinity.
    """
    pass

def copysign(x, y):
    """
    Return ``x`` with the sign of ``y``.
    """
    pass

def cos(x):
    """
    Return the cosine of ``x``.
    """
    pass

def cosh(x):
    """
    Return the hyperbolic cosine of ``x``.
    """
    pass

def degrees(x):
    """
    Return radians ``x`` converted to degrees.
    """
    pass

def erf(x):
    """
    Return the error function of ``x``.
    """
    pass

def erfc(x):
    """
    Return the complementary error function of ``x``.
    """
    pass

def exp(x):
    """
    Return the exponential of ``x``.
    """
    pass

def expm1(x):
    """
    Return ``exp(x) - 1``.
    """
    pass

def fabs(x):
    """
    Return the absolute value of ``x``.
    """
    pass

def floor(x):
    """
    Return an integer, being ``x`` rounded towards negative infinity.
    """
    pass

def fmod(x, y):
    """
    Return the remainder of ``x/y``.
    """
    pass

def frexp(x):
    """
    Decomposes a floating-point number into its mantissa and exponent.
    The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
    exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
    the relation ``0.5 <= abs(m) < 1`` holds.
    """
    pass

def gamma(x):
    """
    Return the gamma function of ``x``.
    """
    pass

def isfinite(x):
    """
    Return ``True`` if ``x`` is finite.
    """
    pass

def isinf(x):
    """
    Return ``True`` if ``x`` is infinite.
    """
    pass

def isnan(x):
    """
    Return ``True`` if ``x`` is not-a-number
    """
    pass

def ldexp(x, exp):
    """
    Return ``x * (2**exp)``.
    """
    pass

def lgamma(x):
    """
    Return the natural logarithm of the gamma function of ``x``.
    """
    pass

def log(x):
    """
    Return the natural logarithm of ``x``.
    """
    pass

def log10(x):
    """
    Return the base-10 logarithm of ``x``.
    """
    pass

def log2(x):
    """
    Return the base-2 logarithm of ``x``.
    """
    pass

def modf(x):
    """
    Return a tuple of two floats, being the fractional and integral parts of
    ``x``.  Both return values have the same sign as ``x``.
    """
    pass

def pow(x, y):
    """
    Returns ``x`` to the power of ``y``.
    """
    pass

def radians(x):
    """
    Return degrees ``x`` converted to radians.
    """
    pass

def sin(x):
    """
    Return the sine of ``x``.
    """
    pass

def sinh(x):
    """
    Return the hyperbolic sine of ``x``.
    """
    pass

def sqrt(x):
    """
    Return the square root of ``x``.
    """
    pass

def tan(x):
    """
    Return the tangent of ``x``.
    """
    pass

def tanh(x):
    """
    Return the hyperbolic tangent of ``x``.
    """
    pass

def trunc(x):
    """
    Return an integer, being ``x`` rounded towards 0.
    """
    pass

