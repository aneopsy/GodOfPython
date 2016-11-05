import sys
import random
import os
import math
import collections
import time

Sphere = collections.namedtuple("Sphere", "cx cy cz r")
V3 = collections.namedtuple("V3", "x y z")


def normalize((x, y, z)):
    len = math.sqrt(x**2 + y**2 + z**2)
    return V3(x / len, y / len, z / len)


def dot(v1, v2):
    d = v1.x*v2.x + v1.y*v2.y + v1.z*v2.z
    return -d if d < 0 else 0.0


def hit_sphere(sph, x0, y0):
    x = x0 - sph.cx
    y = y0 - sph.cy
    zsq = sph.r ** 2 - (x ** 2 + y ** 2)
    if zsq < 0:
        return (False, 0, 0)
    szsq = math.sqrt(zsq)
    return (True, sph.cz - szsq, sph.cz + szsq)


def draw_sphere(k, ambient, light, posi):
    shades = ".:!*oe&#%@"
    pos = Sphere(20.0, 20.0, 0.0, 20.0)
    neg = Sphere(posi.x, posi.y, posi.z, 16.0)

    for i in xrange(int(math.floor(pos.cy - pos.r)),
                    int(math.ceil(pos.cy + pos.r) + 1)):
        y = i + 0.5
        for j in xrange(int(math.floor(pos.cx - 2 * pos.r)),
                        int(math.ceil(pos.cx + 2 * pos.r) + 1)):
            x = (j - pos.cx) / 2.0 + 0.5 + pos.cx

            (h, zb1, zb2) = hit_sphere(pos, x, y)
            if not h:
                hit_result = 0
            else:
                (h, zs1, zs2) = hit_sphere(neg, x, y)
                if not h:
                    hit_result = 1
                elif zs1 > zb1:
                    hit_result = 1
                elif zs2 > zb2:
                    hit_result = 0
                elif zs2 > zb1:
                    hit_result = 2
                else:
                    hit_result = 1

            if hit_result == 0:
                sys.stdout.write(' ')
                continue
            elif hit_result == 1:
                vec = V3(x - pos.cx, y - pos.cy, zb1 - pos.cz)
            elif hit_result == 2:
                vec = V3(neg.cx-x, neg.cy-y, neg.cz-zs2)
            vec = normalize(vec)

            b = dot(light, vec) ** k + ambient
            intensity = int((1 - b) * len(shades))
            intensity = min(len(shades), max(0, intensity))
            sys.stdout.write(shades[intensity])
        print

t = 0
k = 20
h = 20
zh = 50
zk = 50
zr = 50
r = 20
z = 0
while True:
    t += 0.03
    z -= 0.001
    pos = V3(r*math.cos(t) + h, r*math.sin(t) + k, -20/2)
    sun = V3(zr*math.cos(z) + zh, zr*math.sin(z) + zk, 30)
    light = normalize(sun)
    draw_sphere(2, 0.5, light, pos)
    time.sleep(0.05)
    os.system('cls' if os.name == 'nt' else 'clear')
