from datetime import datetime, timezone, timedelta

def parse(line: str):
    date_part, time_part, tz_part = line.strip().split()
    dt = datetime.strptime(date_part + " " + time_part, "%Y-%m-%d %H:%M:%S")
    
    sign = 1 if tz_part[3] == '+' else -1
    hh, mm = map(int, tz_part[4:].split(":"))
    offset = timedelta(hours=hh, minutes=mm) * sign
    
    tz = timezone(offset)
    return dt.replace(tzinfo=tz).astimezone(timezone.utc)

start = parse(input())
end = parse(input())

print(int((end - start).total_seconds()))