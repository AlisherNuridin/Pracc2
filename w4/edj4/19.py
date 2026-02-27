import math

r = float(input().strip())
ax, ay = map(float, input().split())
bx, by = map(float, input().split())

def dist(x, y):
    return math.hypot(x, y)

def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x

dx, dy = bx - ax, by - ay
ab2 = dx*dx + dy*dy
ab = math.sqrt(ab2)

if ab2 == 0.0:
    min_d = dist(ax, ay)
else:
    t = clamp(-(ax*dx + ay*dy) / ab2, 0.0, 1.0)
    cx, cy = ax + t*dx, ay + t*dy
    min_d = dist(cx, cy)

eps = 1e-12
if min_d >= r - eps:
    print(f"{ab:.10f}")
else:
    d1 = dist(ax, ay)
    d2 = dist(bx, by)

    a1 = 0.0 if d1 <= r else math.acos(clamp(r / d1, -1.0, 1.0))
    a2 = 0.0 if d2 <= r else math.acos(clamp(r / d2, -1.0, 1.0))

    cos_theta = (ax*bx + ay*by) / (d1 * d2)
    theta = math.acos(clamp(cos_theta, -1.0, 1.0))

    phi = theta - a1 - a2
    if phi < 0: 
        phi = 0.0

    l1 = math.sqrt(max(0.0, d1*d1 - r*r))
    l2 = math.sqrt(max(0.0, d2*d2 - r*r))

    ans = l1 + l2 + r * phi
    print(f"{ans:.10f}")