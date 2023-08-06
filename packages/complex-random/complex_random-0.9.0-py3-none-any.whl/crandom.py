import numpy as np



def crandomu(size=None, dtype=np.complex128, out=None):
    """
    crandomu(size=None, dtype=np.complex128, out=None)

    Returns uniformly distributed random complex numbers on the complex unit circle.

    Parameters
    ----------
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.
    dtype : dtype, optional
        Desired dtype of the result, only `complex128` and `complex64` are supported.
        Byteorder must be native. The default value is np.complex128.
    out : ndarray, optional
        Alternative output array in which to place the result. If size is not None,
        it must have the same shape as the provided size and must match the type of
        the output values.

    Returns
    -------
    out : complex number or ndarray of complex numbers
        Array of random complex numbers of shape `size` (unless ``size=None``, in which
        case a single complex number is returned).
    """
    return np.exp(2j*np.pi * np.random.default_rng().random(size=size), dtype=dtype, out=out)



def crandom(size=None, dtype=np.complex128, out=None):
    """
    crandom(size=None, dtype=np.complex128, out=None)

    Returns uniformly distributed random complex numbers within the open complex unit circle.

    Parameters
    ----------
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.
    dtype : dtype, optional
        Desired dtype of the result, only `complex128` and `complex64` are supported.
        Byteorder must be native. The default value is np.complex128.
    out : ndarray, optional
        Alternative output array in which to place the result. If size is not None,
        it must have the same shape as the provided size and must match the type of
        the output values.

    Returns
    -------
    out : complex number or ndarray of complex numbers
        Array of random complex numbers of shape `size` (unless ``size=None``, in which
        case a single complex number is returned).
    """
    rng = np.random.default_rng()
    return np.multiply(np.sqrt(rng.random(size=size)), np.exp(2j*np.pi * rng.random(size=size)), dtype=dtype, out=out)



def crandomn(loc=0j, scale=((1, 0), (0, 1)), size=None, dtype=np.complex128, out=None):
    """
    crandomn(loc=0j, scale=((1, 0), (0, 1)), size=None, dtype=np.complex128, out=None)

    Returns normal distributed random complex numbers.

    Parameters
    ----------
    loc : complex number, optional
        Mean (“centre”) of the distribution. Default is 0.
    scale: 2-D array_like of shape (2, 2), optional
        Covariance matrix of the distribution.
        It must be symmetric and positive-semidefinite for proper sampling. Default is ``((1, 0), (0, 1))``.
    size : int or tuple of ints, optional
        Output shape.  If the given shape is, e.g., ``(m, n, k)``, then
        ``m * n * k`` samples are drawn.  Default is None, in which case a
        single value is returned.
    dtype : dtype, optional
        Desired dtype of the result, only `complex128` and `complex64` are supported.
        Byteorder must be native. The default value is np.complex128.
    out : ndarray, optional
        Alternative output array in which to place the result. If size is not None,
        it must have the same shape as the provided size and must match the type of
        the output values.

    Returns
    -------
    out : complex number or ndarray of complex numbers
        Array of random complex numbers of shape `size` (unless ``size=None``, in which
        case a single complex number is returned).
    """
    rng = np.random.default_rng()
    M = rng.multivariate_normal((loc.real, loc.imag), scale, size=size)
    return M[..., 0] + 1j*M[..., 1]
