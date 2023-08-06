import numpy as np

from qc_quad.gauss_legendre import gauss_legendre_ab
from qc_quad.lebedev.llq_all import all_quads, NUM_POINTS


def gen_xyz_ww_ball(dr: float, r_ball: float) -> tuple[np.ndarray, np.ndarray]:
    """Generate a 3D grid for integration over a volume of a ball or radius `r_ball`.

    Args:
        dr: distance between points along radial coordinate.
        r_ball: radius of the ball.

    Returns:
        Arrays or coordinates and weights.
    """
    if dr < 0.0:
        raise ValueError(f'Invalid dr {dr}')

    num_gl = 2 * (int(0.5 * r_ball / dr) + 1)
    rr, ww_gl = gauss_legendre_ab(num_gl, 0.0, r_ball)

    dv = 4 * np.pi * dr**3 / 3
    num_ll_float = 4 * np.pi * rr**2 * dr / dv
    orders_ll = np.searchsorted(NUM_POINTS, num_ll_float)
    ll_max = len(NUM_POINTS)
    orders_ll[orders_ll == ll_max] = ll_max - 1

    ls_xyz, ls_ww = [], []
    for i, (r, w_gl, o) in enumerate(zip(rr, ww_gl, orders_ll)):
        xyz, ww = all_quads[o].gen_xyz_ww()
        ls_xyz.append(xyz * r)
        ls_ww.append(ww * 4 * np.pi * r**2 * w_gl)

    return np.concatenate(ls_xyz), np.concatenate(ls_ww)