import json

def deep_diff(obj1, obj2, path=""):
    diffs = []

    keys = set(obj1.keys()) | set(obj2.keys())

    for key in keys:
        new_path = f"{path}.{key}" if path else key

        if key not in obj1:
            diffs.append((new_path, "<missing>", json.dumps(obj2[key], separators=(",", ":"))))
        elif key not in obj2:
            diffs.append((new_path, json.dumps(obj1[key], separators=(",", ":")), "<missing>"))
        else:
            v1 = obj1[key]
            v2 = obj2[key]

            if isinstance(v1, dict) and isinstance(v2, dict):
                diffs.extend(deep_diff(v1, v2, new_path))
            elif v1 != v2:
                diffs.append((
                    new_path,
                    json.dumps(v1, separators=(",", ":")),
                    json.dumps(v2, separators=(",", ":"))
                ))

    return diffs


obj1 = json.loads(input())
obj2 = json.loads(input())

differences = deep_diff(obj1, obj2)
differences.sort(key=lambda x: x[0])

if not differences:
    print("No differences")
else:
    for path, old, new in differences:
        print(f"{path} : {old} -> {new}")