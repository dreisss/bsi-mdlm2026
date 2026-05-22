#!/usr/bin/env python

from math import sqrt, cos, acos, pi

input_str = "Digite os 4 valores para A, B, C e D (separadas por espaços): "
A, B, C, D = [float(v) for v in input(input_str).split(" ")]
a, b, c = B / A, C / A, D / A

print(f"f(x) = {A}x^3 + {B}x^2 + {C}x + {D}")
print(f"f'(x) = x^3 + {a}x^2 + {b}x + {c}")

Q = (a**2 - 3 * b) / 9
R = (2 * a**3 - 9 * a * b + 27 * c) / 54
Delta = R**2 - Q**3

print(f"Delta = {Delta}")

if Delta >= 0:
    print("A equação só tem uma raíz")
else:
    print("A equação tem 3 raízes distintas")

    Teta = acos(R / sqrt(Q**3))

    x1 = -2 * sqrt(Q) * cos(Teta / 3) - a / 3
    x2 = -2 * sqrt(Q) * cos((Teta + 2 * pi) / 3) - a / 3
    x3 = -2 * sqrt(Q) * cos((Teta - 2 * pi) / 3) - a / 3

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    print(f"x3 = {x3}")
