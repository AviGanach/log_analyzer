from config import *

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

# כתבו פונקציה שמקבלת את הנתונים ומחזירה רשימה של כל השורות עם פורט
# רגיש ),22 ,23 או 3389(
def is_sensitive(port: str) -> bool:
    try:
        return port in SENSITIVE_PORTS
    except Exception as e:
        raise e

def sensitive_ports(data:list[list[str]]) -> list[str]:
    try:
        sensitive = []
        for line in data:
            if is_sensitive(line[3]):
                sensitive.append(line[3])
        return sensitive
    except Exception as e:
        raise e

# כתבו פונקציה שמקבלת את הנתונים ומחזירה רשימה של כל השורות עם חבילות
# מעל 5000 בייט.

def is_large(size:int) -> bool:
    try:
        return size > MAX_SIZE
    except Exception as e:
        raise e

def large_size(data:list[list[str]]) -> list[str]:
    try:
        larges = []
        for line in data:
            if is_large(int(line[5])):
                larges.append(line[5])
        return larges
    except Exception as e:
        raise e