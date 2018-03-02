#!/usr/bin/python3

import sys

class ride():
    def __init__(self, n, a, b, x, y, s, f):
        self.n = n
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        self.s = s
        self.f = f
        self.dist = abs(a-x) + abs (b-y)


def copyRides(rides):
    crides
    for ride in rides:
        crides.append(ride)
    return crides


def getTimeWasted(ride, x, y, t):
    tcum = abs(x-ride.a) + abs(y-ride.b)
    twait = ride.s - (t + tcum)
    tfinish = t + tcum + ride.dist
    if tfinish > ride.f:
        return sys.maxsize

    return tcum+twait


def chooseRide(rides, x, y, t):
    bestRide = None
    minTimeWasted = sys.maxsize - 1

    for ride in rides:
        timeWasted = getTimeWasted(ride, x, y, t)
        if timeWasted < minTimeWasted:
            minTimeWasted = timeWasted
            bestRide = ride


    return bestRide


def printRide(ride):
    print(ride.n, ride.a, ride.b, ride.x, ride.y, ride.s, ride.f)

input_file = input("Input file: ")

with open(input_file+'.in', 'r') as f:
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
        rides.append(ride(i, row[0], row[1], row[2], row[3], row[4], row[5]))

print(R, C, F, N, B, T)
for i in range(N):
    printRide(rides[i])

f = open(input_file+'.out', 'w')

for car in range(F):
    takenRides = []
    x = 0
    y = 0
    t = 0
    while t < T:
        ride = chooseRide(rides, x, y, t)
        if ride == None:
            break
        tcum = abs(x-ride.a) + abs(y-ride.b) + t
        t = max(tcum, ride.s) + ride.dist
        if t <= T:
            rides.remove(ride)
            takenRides.append(ride)
        x = ride.x
        y = ride.y

    f.write(str(len(takenRides)))
    for ride in takenRides:
        f.write(' '+str(ride.n))
    f.write('\n')

f.close()
