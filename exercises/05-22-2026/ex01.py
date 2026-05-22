#!/usr/bin/env python

import matplotlib.pyplot as plt

# 1. Solicite ao usuário os valores de dois pontos no plano cartesiano: • Ponto A(x1,y1) • Ponto B(x2,y2)
x1, y1 = [float(v) for v in input("Ponto A (separado por espaço): ").split(" ")]
x2, y2 = [float(v) for v in input("Ponto B (separado por espaço): ").split(" ")]

# 2. Calcule os coeficientes a (inclinação) e b (intercepto) da função afim f(x) = ax + b que passa por esses dois pontos: a = (y2 - y1) / (x2 - x1), b = y1 - a * x1
if x1 == x2:
    print("A reta é vertical")
else:
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a * x1

    # 3. Crie uma função chamada f(x) que recebe um valor x e os retorna f(x)
    def f(x):
        return a * x + b

    # 4. Mostre na tela: • A equação da função no formato f(x) = ax+b • O valor de f(0) • A raiz da função (x • Os intervalos de x em que f(x) > 0 e f(x) < 0. • Mostre o gráfico
    print(f"f(x) = {a}x + {b}")
    print(f"f(0) = {f(0)}")

    if a == 0:
        print("a função é horizontal")
        print(f"f(x) {">=" if b >= 0 else "<="} 0 para todo x")

    else:
        root = -b / a
        print(f"raiz de f = {root}")
        print(f"f(x) > 0 para x {">" if a > 0 else "<"} {root}")
        print(f"f(x) < 0 para x {">" if a < 0 else "<"} {root}")

    plt.plot(range(-10, 11), [f(x) for x in range(-10, 11)])
    plt.grid(True)
    plt.axhline(y=0, color="black", linewidth=1)
    plt.axvline(x=0, color="black", linewidth=1)
    plt.show()
