import math

r = float(input().strip())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

dx, dy = bx - ax, by - ay
seg_len = math.hypot(dx, dy)

if seg_len == 0.0:
    inside = (ax * ax + ay * ay) <= r * r
    print(f"{(0.0 if not inside else 0.0):.10f}")
    raise SystemExit

a = dx * dx + dy * dy
b = 2.0 * (ax * dx + ay * dy)
c = ax * ax + ay * ay - r * r

disc = b * b - 4.0 * a * c

def f(t):
    x = ax + t * dx
    y = ay + t * dy
    return x * x + y * y - r * r

length_inside = 0.0

if disc < 0:
    if f(0.0) <= 0:
        length_inside = seg_len
    else:
        length_inside = 0.0
else:
    sqrt_disc = math.sqrt(max(0.0, disc))
    t1 = (-b - sqrt_disc) / (2.0 * a)
    t2 = (-b + sqrt_disc) / (2.0 * a)
    if t1 > t2:
        t1, t2 = t2, t1

    left = max(0.0, t1)
    right = min(1.0, t2)

    if right > left:
        length_inside = seg_len * (right - left)
    else:
        length_inside = seg_len if f(0.0) <= 0 and f(1.0) <= 0 else 0.0

print(f"{length_inside:.10f}")