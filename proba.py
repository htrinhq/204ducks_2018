##
## EPITECH PROJECT, 2019
## 204ducks_2018
## File description:
## proba
##

from math import exp, sqrt

def duck_return(min: float, data: float) -> (int, int, int):
    """Get the proba after a min amount of ducks."""
    x = 1.0
    while (get_proba(data, x / 60) - get_proba(data, 0) < min):
        x += 0.1
    minute = int(x / 60)
    tenSec = int(x % 60 / 10)
    sec = round(x % 10)
    return minute, tenSec, sec

def get_avg_time(data: float, mode = 0) -> (int, int) or float:
    """Get Average Time."""
    t = 0
    result = 0
    while t < 10:
        result += get_proba(data, t, 1) * t / 1000
        t += 0.001
    minute = int(result)
    sec = round((result - int(result)) * 60)
    return (minute, sec) if mode == 0 else (result)

def get_standard_dev(data: float, avg_time: float) -> float:
    """Get the standard deviation."""
    result = 0
    time = 0
    while time < 100:
        result += pow(time - avg_time, 2) * get_proba(data, time, 1) / 1000
        time += 0.001
    return sqrt(result)

def get_proba(data: float, t: float, proba = 0) -> float:
    """Get the probability for 1 t gave."""
    if proba == 0:
        result = - data * exp(-t) - (4 - 3 * data) / 2 * exp(-2 * t) - \
            (2 * data - 4) / 4 * exp(-4 * t)
    else:
        result = data * exp(-t) + (4 - 3 * data) * \
            exp(-2 * t) + (2 * data - 4) * exp(-4 * t)
    return result
