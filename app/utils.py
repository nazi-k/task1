def parse_bool(value: str) -> bool | None:
    if value.lower() in ('true', '1'):
        return True
    elif value.lower() in ('false', '0'):
        return False
    return None
