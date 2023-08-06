def zf64(r: int or str) -> str:
    if isinstance(r, int):
        return str(hex(r)[2:]).zfill(64)
    elif isinstance(r, str):
        return str(r[2:]).zfill(64)
    else:
        raise TypeError("input type int or str!")
