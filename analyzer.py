from checks import is_large

# כתבו פונקציה שמקבלת את הנתונים ומחזירה רשימה שבה כל שורה מתויגת:
# "LARGE "אם הגודל מעל ,5000 אחרת "NORMAL ".
def tag_large_normal(data:list[list[str]])->list[list[str]]:
    try:
        for line in data:
            if is_large(int(line[5])):
                line.append("LARGE")
            else:
                line.append("NORMAL")
    except Exception as e:
        raise(e)