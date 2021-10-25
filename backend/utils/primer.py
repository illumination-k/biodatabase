from typing import Literal


def calc_gc(seq: str) -> float:
    all = len(seq)
    gc = len([s for s in seq if s.lower() == "g" or s.lower() == "c"])
    return gc / all

Method = Literal["Wallace", "NearestNeighbor"]
def calc_tm(seq: str, method: Method = "Wallace") -> float:
    if method == "Wallace":
        all = len(seq)
        gc = len([s for s in seq if s.lower() == "g" or s.lower() == "c"])
        at = all - gc
        return at * 2 + gc * 4

