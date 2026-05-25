#!/usr/bin/env python

# Faça um programa que peça a data de seu nascimento, dia (d), mês (m) e ano (a). Responda:
# a) Mostrar:
#   se d for ímpar: f(x)=-mx^2+dx+a
#   se d for par: f(x)=mx^2+dx-a
# b) Calcule as raízes (se houver).
# c) Encontre o mínimo (ou máximo) da função.
# d) Para quais intervalos de x o valor da função será Positivo (f(x) > 0) ou Negativo (f(x) < 0)?
# e) Com base nos dados acima, esboce o gráfico da função.

from math import sqrt
import matplotlib.pyplot as plt

d, m, a = [
    float(v) for v in input("Digite a data do seu nascimento (dd/mm/aaaa): ").split("/")
]

# A, B, C: Ax^2 + Bx + C
if d % 2 == 0:
    A, B, C = -m, d, a
else:
    A, B, C = m, d, -a

Delta = B**2 - 4 * A * C


def f(x):
    return A * x**2 + B * x + C


print(f"f(x) = {A}x^2 + {B}x + {C}")

if Delta > 0:
    x1 = (-B + sqrt(Delta)) / 2 * A
    x2 = (-B - sqrt(Delta)) / 2 * A

    print("As raízes da equação são:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

elif Delta == 0:
    x1 = x2 = (-B + sqrt(Delta)) / 2 * A

    print("A raíz da equação é: ")
    print(f"x = {x2}")

else:
    x1 = x2 = False
    print("A equação não tem raízes reais!")


Xv = -B / (2 * A)

print(
    f"O {'máximo' if A < 0 else 'mínimo' } da função é em x = {Xv} e com f(x) = {f(Xv)}"
)

if Delta > 0:
    print(f"f(x) {'>' if A < 0 else '<'} 0 para todo {x1} < x < {x2}")
    print(f"f(x) {'>' if A > 0 else '<'} 0 para todo x > {x2} ou x < {x1}")

elif Delta == 0:
    print(f"f(x) {'>' if A > 0 else '<'} 0 para todo x != {x1}")

else:
    print(f"f(x) {'>' if A > 0 else '<'} 0 para todo")

plot_size = 100

plt.plot(
    range(-plot_size, plot_size + 1), [f(x) for x in range(-plot_size, plot_size + 1)]
)

plt.grid(True)
plt.axhline(y=0, color="black", linewidth=1)
plt.axvline(x=0, color="black", linewidth=1)
plt.show()
