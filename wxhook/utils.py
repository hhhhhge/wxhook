import xmltodict


def parse_event(event: dict, fields=None) -> dict:
    for field in fields or ["content", "signature"]:
        try:
            if field in event:
                event[field] = xmltodict.parse(event[field])
        except Exception:
            pass
    return event
