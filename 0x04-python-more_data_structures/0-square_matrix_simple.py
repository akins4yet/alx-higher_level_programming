#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        news = []
        for rows in matrix:
            news.append(list(map(lambda x: x**2, rows)))
    return news
