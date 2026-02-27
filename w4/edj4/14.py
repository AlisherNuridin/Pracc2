import json
import re

data = json.loads(input())
q = int(input())

def resolve_query(data, query):
    current = data
    
    # разбиваем по точкам, но сохраняем индексы [число]
    parts = re.findall(r'[^.\[\]]+|\[\d+\]', query)
    
    for part in parts:
        if part.startswith('['):
            # это индекс массива
            index = int(part[1:-1])
            if isinstance(current, list) and 0 <= index < len(current):
                current = current[index]
            else:
                return "NOT_FOUND"
        else:
            # это ключ объекта
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return "NOT_FOUND"
    
    return json.dumps(current, separators=(",", ":"))

for _ in range(q):
    query = input().strip()
    result = resolve_query(data, query)
    print(result)