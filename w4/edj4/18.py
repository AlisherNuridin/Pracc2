ax, ay = map(float, input().split())
bx, by = map(float, input().split())

bx2, by2 = bx, -by
t = -ay / (by2 - ay)
rx = ax + t * (bx2 - ax)
ry = 0.0

print(f"{rx:.10f} {ry:.10f}")