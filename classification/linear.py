import numpy as np

def linear(points):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    coefficients = np.polyfit(x, y, 1)
    return coefficients