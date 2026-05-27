#!/usr/bin/env python

# Um Círculo no plano cartesiano é definido por seu centro A(xc, yc) e seu raio r (r > 0).
# Um ponto P(xp, yp) pode estar dentro, sobre ou fora desse círculo. Crie um programa:
# 1. Solicite ao usuário as coordenadas do centro A: xc e yc.
# 2. Solicite o valor do raio r.
# 3. Solicite as coordenadas do ponto P: xp e yp.
# 4. Responda se o ponto P está dentro ou fora do Círculo.
#
# Use d^2 = (x2 − x1)^2 + (y2 − y1)^2

from math import sqrt, cos, sin, pi
import matplotlib.pyplot as plt
from numpy import linspace

input_str1 = "Digite as coordenadas do centro A (xc yc): "
xc, yc = [float(v) for v in input(input_str1).split(" ")]

r = float(input("Digite o valor do raio (r): "))

input_str2 = "Digite as coordenadas do ponto P (xp yp): "
xp, yp = [float(v) for v in input(input_str2).split(" ")]

d = sqrt((xp - xc) ** 2 + (yp - yc) ** 2)

if d <= r:
    print("O ponto está dentro da circunferência!")
else:
    print("O ponto está fora da circunferência!")


angles = linspace(0, 2 * pi)
Xs = [xc + r * cos(ang) for ang in angles]
Ys = [yc + r * sin(ang) for ang in angles]
plt.plot(Xs, Ys)

plt.plot(xp, yp, marker="P")

plt.grid(True)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.show()
