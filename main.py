#!/usr/bin/python3

class ride():
    def __init__(self, a, b, x, y, s, f):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f


def printRide(ride):
    print(ride.a, ride.b, ride.x, ride.y, ride.s, ride.f)

input_file = input("Input file: ")

with open(input_file, 'r') as f:
    params = f.readline().split()
    R = int(params[0])
    C = int(params[1])
    F = int(params[2])
    N = int(params[3])
    B = int(params[4])
    T = int(params[5])

    rides = []
    for i in range(N):
        row = [int(x) for x in f.readline().split()]
        rides.append(ride(row[0], row[1], row[2], row[3], row[4], row[5]))

print(R, C, F, N, B, T)
for i in range(N):
    printRide(rides[i])
