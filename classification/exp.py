import numpy as np

def exponential(points):
    x = [p[0] for p in points]
    y = [np.log(p[1]) for p in points]
    coefficients = np.polyfit(x, y, 1)
    return coefficients