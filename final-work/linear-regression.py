#!/usr/bin/env python

# Tema: O Uso da Regressão Linear em Python como Ferramenta Didática para o Estudo de Fenômenos Físicos no Ensino Médio.
# A aplicação (x e y): Implementar o algoritmo utilizando dados de experimentos reais (como a relação entre Massa (x) e
# Extensão de uma mola (y) — Lei de Hooke) para mostrar como a programação ajuda a validar leis científicas.

import matplotlib.pyplot as plt
from random import random, randint

points: list[list[float]] = []

# PARA TESTES: popular com dados aleatórios
# m = randint(-1, 1) * random() * 100
# for x in range(1, 100):
#     points.append([x, m * x + random() * 1000])


def calculate_coef(points):
    avg_x = sum([x for [x, _] in points]) / len(points)
    avg_y = sum([y for [_, y] in points]) / len(points)

    m_num = sum([(x - avg_x) * (y - avg_y) for [x, y] in points])
    m_den = sum([(x - avg_x) ** 2 for [x, _] in points])
    m = m_num / m_den

    b = avg_y - m * avg_x

    return (m, b)


print("Digite os valores separados por espaço ('1.1 1.0').")
print("Para finalizar aperte 'Enter'.")

while True:
    input_text = input("x y: ")

    if input_text.strip() == "":
        print("Programa finalizado!")
        break

    points.append([float(c) for c in input_text.split(" ")])

    X = [x for [x, _] in points]
    Y = [y for [_, y] in points]
    min_x, max_x = min(X), max(X)
    min_y, max_y = min(Y), max(Y)

    plt.scatter(X, Y)

    if len(points) >= 2:

        def f_avg(x):
            m, b = calculate_coef(points)

            return m * x + b

        plt.plot([min_x - 10, max_x + 10], [f_avg(min_x - 10), f_avg(max_x + 10)])

    plt.grid(True)
    plt.show()
