from pathlib import Path
from typing import List, Tuple


def get_codes(lines: List[str]) -> List[int]:
    """Get a list of symmetry codes from the matlab script."""
    codes = []
    for line in lines:
        if 'gen_oh' in line:
            codes.append(int(line.split('(')[1].split(',')[0]))
    return codes


def get_variables(lines: List[str], let_str: str) -> List[str]:
    weights = []
    for line in lines:
        if let_str in line:
            weights.append(line.split('=')[1].split(';')[0])
    return weights


def get_codes_ww_aa_bb(file_path: Path) -> Tuple[List[int], List[float], List[float]]:
    content = file_path.read_text()
    lines = content.splitlines()
    codes = get_codes(lines)
    vv = get_variables(lines, 'v = ')
    aa = get_variables(lines, 'a = ')
    bb = get_variables(lines, 'b = ')
    return codes, vv, aa, bb


def format_quad(file_path: Path) -> List[str]:

    codes, ww, aa, bb = get_codes_ww_aa_bb(file_path)

    file_name_stem = file_path.stem

    lines = []
    lines.append(f'{file_name_stem} = LLQ({tuple(codes)}, (')
    count_a = 0
    count_b = 0
    for code, w in zip(codes, ww):
        if code > 0 and code < 4:
            lines.append(f'        ({w}, 0.0, 0.0),')
        elif code > 3 and code < 6:
            count_a += 1
            a = aa[count_a]
            lines.append(f'        ({w}, {a}, 0.0),')
        elif code == 6:
            count_a += 1
            count_b += 1
            a = aa[count_a]
            b = bb[count_b]
            lines.append(f'        ({w}, {a}, {b}),')
        else:
            raise ValueError(f'Invalid code {code}')
    lines.append('        ))')
    return lines
