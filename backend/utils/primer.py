from typing import Literal, List, Tuple


def calc_gc(seq: str) -> float:
    all = len(seq)
    gc = len([s for s in seq if s.lower() == "g" or s.lower() == "c"])
    return gc / all


Method = Literal["Wallace", "NearestNeighbor"]


def kmerlize(seq: str, k: int = 15) -> List[str]:
    """Return kmers of input seq
    >>> kmerlize(seq="agtggtctcctataagt", k=15)
    ['agtggtctcctataa', 'gtggtctcctataag', 'tggtctcctataagt']
    >>> kmerlize(seq="atgc")
    ['atgc']
    >>> kmerlize(seq="atgcatgcatgcatg")
    ['atgcatgcatgcatg']
    """
    if len(seq) <= 15:
        return [seq]
    kmers = []
    for i in range(0, len(seq) - k + 1):
        kmers.append(seq[i : i + k])
    return kmers


HS_PARAMS = {
    "AA": [-9.1, -24],
    "TT": [-9.1, -24],
    "AT": [-8.6, -23.9],
    "TA": [-6, -16.9],
    "CA": [-5.8, -12.9],
    "TG": [-5.8, -12.9],
    "GT": [-6.5, -17.3],
    "AC": [-6.5, -17.3],
    "CT": [-7.8, -20.8],
    "AG": [-7.8, -20.8],
    "GA": [-5.6, -13.5],
    "TC": [-5.6, -13.5],
    "CG": [-11.9, -27.8],
    "GC": [-11.1, -26.7],
    "GG": [-11, -26.6],
    "CC": [-11, -26.6],
}


def make_pairs(seq: str) -> List[str]:
    """
    >>> make_pairs(seq="ATGAGCCCTGAAGTG")
    ['AT', 'TG', 'GA', 'AG', 'GC', 'CC', 'CC', 'CT', 'TG', 'GA', 'AA', 'AG', 'GT', 'TG']
    """
    return [seq[i : i + 2] for i in range(len(seq) - 1)]


def hs_list(pairs: List[str]) -> Tuple[List[str], List[str]]:
    """
    >>> pairs = make_pairs(seq = "ATGAGCCCTGAAGTG")
    >>> h_list, s_list = hs_list(pairs)
    >>> h_list
    [-8.6, -5.8, -5.6, -7.8, -11.1, -11, -11, -7.8, -5.8, -5.6, -9.1, -7.8, -6.5, -5.8]
    >>> s_list
    [-23.9, -12.9, -13.5, -20.8, -26.7, -26.6, -26.6, -20.8, -12.9, -13.5, -24, -20.8, -17.3, -12.9]
    """
    h_list = [HS_PARAMS[k][0] for k in pairs]
    s_list = [HS_PARAMS[k][1] for k in pairs]
    return (h_list, s_list)


def tm_by_nearest_neighbor(
    seq: str, ct: float = 0.5 * (10 ** -6), na_conc: float = 50 * (10 ** -3)
) -> float:
    """Return tm calculated by nearest neighbor method
    Breslauer, K.J. et al. (1986) Proc. Natl. Acad. Sci. USA. 83: 3746-3750.
    >>> seq = "ATGAGCCCTGAAGTG"
    >>> tm_by_nearest_neighbor(seq)
    51.59223448408926
    """
    import math

    seq = seq.upper()
    pairs = make_pairs(seq)
    h_list, s_list = hs_list(pairs)
    h, s = sum(h_list), sum(s_list)

    tm = (
        (1000 * h) / (s - 10.8 + 1.9872 * math.log(ct / 4))
        - 273.15
        + 16.6 * math.log10(na_conc)
    )
    return tm


def calc_tm(seq: str, method: Method = "Wallace") -> float:
    if method == "Wallace":
        all = len(seq)
        gc = len([s for s in seq if s.lower() == "g" or s.lower() == "c"])
        at = all - gc
        return at * 2 + gc * 4

    elif method == "NearestNeighbor":
        return tm_by_nearest_neighbor(seq)
