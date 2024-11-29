# File: mymath.py
def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    sum_values = 0.0
    for v in values:
        sum_values += v
    return float(sum_values) / nvals
