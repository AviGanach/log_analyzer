from config import INTERNALS_IP

# כתבו פונקציה שמקבלת את הנתונים ומחזירה רשימה של כתובות IP מקור
# חיצוניות בלבד

def is_external_ip(ip: str) -> bool:
    try:
        return not ip.startswith(INTERNALS_IP)
    except Exception as e:
        raise e

def externals_ip(data:list[list[str]]) -> list[str]:
    try:
        external = []
        for line in data:
            if is_external_ip(line[1]):
                external.append(line[1])
        return external
    except Exception as e:
        raise e