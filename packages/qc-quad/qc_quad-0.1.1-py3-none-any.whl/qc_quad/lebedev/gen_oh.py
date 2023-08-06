"""Generates points under OH symmetry.


    Given a point on a sphere, specified by A and B, this routine generates all the equivalent
    points under OH symmetry, making grid points with weight `v`.

    The variable `n` is increased by the number of different points generated.

    Depending on `code`, from 6 to 48 different but equivalent points are generated:

      CODE=1:   (0,0,1) etc                                (  6 points)
      CODE=2:   (0,A,A) etc, A=1/sqrt(2)                   ( 12 points)
      CODE=3:   (A,A,A) etc, A=1/sqrt(3)                   (  8 points)
      CODE=4:   (A,A,B) etc, B=sqrt(1-2 A^2)               ( 24 points)
      CODE=5:   (A,B,0) etc, B=sqrt(1-A^2), A input        ( 24 points)
      CODE=6:   (A,B,C) etc, C=sqrt(1-A^2-B^2), A, B input ( 48 points)

  Modified:
    11 September 2010

  Author:
    Dmitri Laikov

  Reference:
    Vyacheslav Lebedev, Dmitri Laikov, "A quadrature formula for the sphere of the 131st
    algebraic order of accuracy", Russian Academy of Sciences Doklady Mathematics,
    Volume 59, Number 3, 1999, pages 477-481.

Args:
    code: selects the symmetry group.
    a: number needed to generate the coordinates of the points for `code` = 4, 5 and 6 only.
    b: number needed to generate the coordinates of the points for `code = 6` only.
    v: the weight to be assigned the points.
    s: index in arrays w and xyz to start filling.
    xyz: array of coordinates of shape (n, 3)
    w: array of weights which is filled

Returns:
    n : next start index (n = s + num_points).
    the arrays `xyz[s:s + num_points]` and `w[s:s + num_points]` are modified inplace.
"""

from typing import Optional
from math import sqrt

import numpy as np


CODE_2_NUM_POINTS: np.ndarray = np.array((0, 6, 12, 8, 24, 24, 48))


def gen_oh1(s: int, v: float, xyz: np.ndarray, w: np.ndarray) -> int:
    f = s + 6
    a = 1.00
    w[s:f] = v
    xyz[s:f, :] = ((a, 0., 0.),
                   (-a, 0., 0.),
                   (0., a, 0.),
                   (0., -a, 0.),
                   (0., 0., a),
                   (0., 0., -a))
    return f


def gen_oh2(s: int, v: float, xyz: np.ndarray, w: np.ndarray) -> int:
    f = s + 12
    a = sqrt(0.50)
    w[s:f] = v
    xyz[s:f, :] = ((0., a, a),
                   (0., -a, a),
                   (0., a, -a),
                   (0., -a, -a),
                   (a, 0., a),
                   (-a, 0., a),
                   (a, 0., -a),
                   (-a, 0., -a),
                   (a, a, 0.),
                   (-a, a, 0.),
                   (a, -a, 0.),
                   (-a, -a, 0.))
    return f


def gen_oh3(s: int, v: float, xyz: np.ndarray, w: np.ndarray) -> int:
    f = s + 8
    a = sqrt(1.00 / 3.00)
    w[s:f] = v
    xyz[s:f, :] = ((a, a, a),
                   (-a, a, a),
                   (a, -a, a),
                   (-a, -a, a),
                   (a, a, -a),
                   (-a, a, -a),
                   (a, -a, -a),
                   (-a, -a, -a))
    return f


def gen_oh4(s: int, a: float, v: float, xyz: np.ndarray, w: np.ndarray) -> int:
    f = s + 24
    b = sqrt(1.00 - 2.00 * a * a)
    w[s:f] = v
    xyz[s:f, :] = ((a, a, b),
                   (-a, a, b),
                   (a, -a, b),
                   (-a, -a, b),
                   (a, a, -b),
                   (-a, a, -b),
                   (a, -a, -b),
                   (-a, -a, -b),
                   (a, b, a),
                   (-a, b, a),
                   (a, -b, a),
                   (-a, -b, a),
                   (a, b, -a),
                   (-a, b, -a),
                   (a, -b, -a),
                   (-a, -b, -a),
                   (b, a, a),
                   (-b, a, a),
                   (b, -a, a),
                   (-b, -a, a),
                   (b, a, -a),
                   (-b, a, -a),
                   (b, -a, -a),
                   (-b, -a, -a))
    return f


def gen_oh5(s: int, a: float, v: float, xyz: np.ndarray, w: np.ndarray) -> int:
    f = s + 24
    b = sqrt(1.00 - a * a)
    w[s:f] = v
    xyz[s:f, :] = ((a, b, 0.),
                   (-a, b, 0.),
                   (a, -b, 0.),
                   (-a, -b, 0.),
                   (b, a, 0.),
                   (-b, a, 0.),
                   (b, -a, 0.),
                   (-b, -a, 0.),
                   (a, 0., b),
                   (-a, 0., b),
                   (a, 0., -b),
                   (-a, 0., -b),
                   (b, 0., a),
                   (-b, 0., a),
                   (b, 0., -a),
                   (-b, 0., -a),
                   (0., a, b),
                   (0., -a, b),
                   (0., a, -b),
                   (0., -a, -b),
                   (0., b, a),
                   (0., -b, a),
                   (0., b, -a),
                   (0., -b, -a))
    return f


def gen_oh6(s: int, a: float, b: float, v: float, xyz: np.ndarray, w: np.ndarray) -> int:
    f = s + 48
    c = sqrt(1.00 - a * a - b * b)
    w[s:f] = v
    xyz[s:f, :] = ((a, b, c),
                   (-a, b, c),
                   (a, -b, c),
                   (-a, -b, c),
                   (a, b, -c),
                   (-a, b, -c),
                   (a, -b, -c),
                   (-a, -b, -c),
                   (a, c, b),
                   (-a, c, b),
                   (a, -c, b),
                   (-a, -c, b),
                   (a, c, -b),
                   (-a, c, -b),
                   (a, -c, -b),
                   (-a, -c, -b),
                   (b, a, c),
                   (-b, a, c),
                   (b, -a, c),
                   (-b, -a, c),
                   (b, a, -c),
                   (-b, a, -c),
                   (b, -a, -c),
                   (-b, -a, -c),
                   (b, c, a),
                   (-b, c, a),
                   (b, -c, a),
                   (-b, -c, a),
                   (b, c, -a),
                   (-b, c, -a),
                   (b, -c, -a),
                   (-b, -c, -a),
                   (c, a, b),
                   (-c, a, b),
                   (c, -a, b),
                   (-c, -a, b),
                   (c, a, -b),
                   (-c, a, -b),
                   (c, -a, -b),
                   (-c, -a, -b),
                   (c, b, a),
                   (-c, b, a),
                   (c, -b, a),
                   (-c, -b, a),
                   (c, b, -a),
                   (-c, b, -a),
                   (c, -b, -a),
                   (-c, -b, -a))
    return f


def gen_oh(code: int, a: Optional[float] = None, b: Optional[float] = None) -> np.ndarray:
    if code > 6 or code < 1:
        raise ValueError(f'Illegal value of CODE. {code}')

    n = CODE_2_NUM_POINTS[code]
    w = np.zeros(n)
    xyz = np.zeros((n, 3))

    if code == 1:
        gen_oh1(0, 1.0, xyz, w)

    elif code == 2:
        gen_oh2(0, 1.0, xyz, w)

    elif code == 3:
        gen_oh3(0, 1.0, xyz, w)

    elif code == 4:
        gen_oh4(0, a, 1.0, xyz, w)

    elif code == 5:
        gen_oh5(0, a, 1.0, xyz, w)

    elif code == 6:
        gen_oh6(0, a, b, 1.0, xyz, w)

    return xyz
