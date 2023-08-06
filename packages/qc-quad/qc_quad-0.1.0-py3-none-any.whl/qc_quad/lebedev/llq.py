from typing import Iterable, Tuple

import numpy as np

from qc_quad.lebedev.gen_oh import (CODE_2_NUM_POINTS, gen_oh1, gen_oh2,
                                                       gen_oh3, gen_oh4, gen_oh5, gen_oh6)


def gen_ld_cc_wab(codes: np.ndarray, wab: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:

    num = CODE_2_NUM_POINTS[codes].sum()
    xyz, ww = np.zeros((num, 3)), np.zeros((num))

    s = 0
    for code, (v, a, b) in zip(codes, wab):
        if   code == 1:
            s = gen_oh1(s, v, xyz, ww)
        elif code == 2:
            s = gen_oh2(s, v, xyz, ww)
        elif code == 3:
            s = gen_oh3(s, v, xyz, ww)
        elif code == 4:
            s = gen_oh4(s, a, v, xyz, ww)
        elif code == 5:
            s = gen_oh5(s, a, v, xyz, ww)
        elif code == 6:
            s = gen_oh6(s, a, b, v, xyz, ww)
        else:
            raise ValueError(f'Invalid code {code}')
    return xyz, ww


class LLQ:
    def __init__(self, codes: Iterable[int], wab: Iterable[Tuple[float, float, float]]) -> None:
        self.codes: np.ndarray = np.array(codes)
        self.wab: np.ndarray = np.array(wab)
        if len(self.codes) != len(self.wab):
            raise ValueError(f'Invalid input: {len(self.codes)} {len(self.wab)}')
        if self.wab.shape[1] != 3:
            raise ValueError(f'Invalid second dimension in wab.shape = {self.wab.shape}')

    def __repr__(self) -> str:
        return f'Lebedev-Laikov quadrature with {self.get_num_points()} points\n' \
               f'    codes = {self.codes}\n    wab = \n{self.wab}'

    def get_num_points(self) -> int:
        return CODE_2_NUM_POINTS[self.codes].sum()

    def get_weights(self) -> np.ndarray:
        return self.wab[:, 0]

    def get_aa(self) -> np.ndarray:
        return self.wab[:, 1]

    def get_bb(self) -> np.ndarray:
        return self.wab[:, 2]

    def gen_xyz_ww(self) -> Tuple[np.ndarray, np.ndarray]:
        return gen_ld_cc_wab(self.codes, self.wab)
