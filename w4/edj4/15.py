from datetime import datetime, timezone, timedelta

def is_leap(y: int) -> bool:
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def parse_date_and_tz(line: str):
    date_part, tz_part = line.strip().split()
    d = datetime.strptime(date_part, "%Y-%m-%d").date()

    sign = 1 if tz_part[3] == '+' else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timedelta(hours=hh, minutes=mm) * sign
    return d, timezone(offset)

def local_midnight_to_utc(d, tz):
    return datetime(d.year, d.month, d.day, 0, 0, 0, tzinfo=tz).astimezone(timezone.utc)

birth_date, birth_tz = parse_date_and_tz(input())
current_date, current_tz = parse_date_and_tz(input())

bm, bd = birth_date.month, birth_date.day
current_utc = local_midnight_to_utc(current_date, current_tz)

def birthday_date_for_year(y: int):
    if bm == 2 and bd == 29 and not is_leap(y):
        return datetime(y, 2, 28).date()
    return datetime(y, bm, bd).date()
current_in_birth = current_utc.astimezone(birth_tz)
y = current_in_birth.year

cand_utc = local_midnight_to_utc(birthday_date_for_year(y), birth_tz)
if cand_utc < current_utc:
    y += 1
    cand_utc = local_midnight_to_utc(birthday_date_for_year(y), birth_tz)

delta_seconds = int((cand_utc - current_utc).total_seconds())
days_left = 0 if delta_seconds == 0 else (delta_seconds + 86400 - 1) // 86400
print(days_left)