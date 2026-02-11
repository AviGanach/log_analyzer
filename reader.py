from pathlib import Path
import csv

# כתבו פונקציה שמקבלת נתיב לקובץ CSV ומחזירה רשימה של רשימות - כל שורה
# כרשימה של שדות.
def lode_csv_to_lst(path:Path) -> list|None:
    try:
        with open(path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = list(reader)
            return data
    except Exception as e:
        print('lode_csv_to_lst', e)
        return None
