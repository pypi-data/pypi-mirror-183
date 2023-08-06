from typing import Tuple

import numpy as np


def gauss_legendre_ab(n: int, a: float, b: float) -> Tuple[np.ndarray, np.ndarray]:
    """Computes the knots and weights for Gauss - Legendre quadrature for a finite range(a..b)

       A transformation y = (b-a) * x / 2 + (b+a) / 2 is applied.

    Args:
        n: number of points in the quadrature rule.
        a: lower integration limit
        b: upper integration limit

    Returns:
        Arrays of knots and weight.
    """
    xx, ww = gauss_legendre(n)
    xx = (b - a) * 0.5 * xx + (b + a) * 0.5
    ww = ww * (b - a) * 0.5
    return xx, ww


def gauss_legendre(n: int) -> Tuple[np.ndarray, np.ndarray]:
    """Generates the Gauss-Legendre knots and weights.

    This is derived from James Talman's subroutine gauleg(n,x,w).

    Args:
        n: number of knots and weights.

    Returns:
        Arrays of knots and weight.
    """
    cmx = 10
    eps = 1.0E-15
    pi = np.pi
    m = int((n + 1) / 2)

    x = np.zeros(n)
    w = np.zeros(n)

    for i in range(m):
        z = np.cos(pi * (i + 0.75) / (n + 0.5))

        for c in range(cmx):
            p1, p2 = 1.0, 0.0
            for j in range(n):
                p2, p3 = p1, p2
                p1 = ((2.0 * j + 1) * z * p2 - j * p3) / (j + 1)
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            if (abs(z - z1) < eps):
                break

        x[i] = -z
        x[n - i - 1] = z
        w[i] = 2.0 / ((1.0 - z * z) * pp * pp)
        w[n - i - 1] = w[i]

    return x, w
