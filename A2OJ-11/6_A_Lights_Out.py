"""
6 Lights Out - https://codeforces.com/problemset/problem/275/A
"""

lights = [[1 for i in range(3)] for j in range(3)]
inputs = []
for _ in range(3):
    inputs.append(list(map(int, input().split())))

if inputs[0][0] %2 != 0:
    lights[0][0] = 0
    lights[0][1] = 0
    lights[1][0] = 0

if inputs[0][1] % 2 != 0:
    lights[0][1] = int(not lights[0][1])
    lights[0][0] = int(not lights[0][0])
    lights[0][2] = int(not lights[0][2])
    lights[1][1] = int(not lights[1][1])

if inputs[0][2] % 2 != 0:
    lights[0][1] = int(not lights[0][1])
    lights[0][2] = int(not lights[0][2])
    lights[1][2] = int(not lights[1][2])

if inputs[1][0] % 2 != 0:
    lights[0][0] = int(not lights[0][0])
    lights[1][0] = int(not lights[1][0])
    lights[1][1] = int(not lights[1][1])
    lights[2][0] = int(not lights[2][0])

if inputs[1][1] % 2 != 0:
    lights[1][0] = int(not lights[1][0])
    lights[1][1] = int(not lights[1][1])
    lights[1][2] = int(not lights[1][2])
    lights[0][1] = int(not lights[0][1])
    lights[2][1] = int(not lights[2][1])

if inputs[1][2] % 2 != 0:
    lights[0][2] = int(not lights[0][2])
    lights[1][1] = int(not lights[1][1])
    lights[1][2] = int(not lights[1][2])
    lights[2][2] = int(not lights[2][2])

if inputs[2][0] % 2 != 0:
    lights[2][0] = int(not lights[2][0])
    lights[2][1] = int(not lights[2][1])
    lights[1][0] = int(not lights[1][0])

if inputs[2][1] % 2 != 0:
    lights[2][0] = int(not lights[2][0])
    lights[2][1] = int(not lights[2][1])
    lights[1][1] = int(not lights[1][1])
    lights[2][2] = int(not lights[2][2])

if inputs[2][2] % 2 != 0:
    lights[2][2] = int(not lights[2][2])
    lights[2][1] = int(not lights[2][1])
    lights[1][2] = int(not lights[1][2])

for i in range(3):
    print(*lights[i], sep="")
