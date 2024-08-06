import numpy as np
from linear import linear
from exp import exponential
from log import logarithmic

coefficients = False

class Classification:
    def __init__(self, points):
        self.points = points
        self.threshold = 10

    def is_linear(self):
        global coefficients
        coefficients = linear(self.points)
        errors = []
        for p in self.points:
            expected_y = coefficients[0] * p[0] + coefficients[1]
            error = abs(p[1] - expected_y)
            errors.append(error)
        return np.mean(errors) < self.threshold

    def is_exponential(self):
        global coefficients
        coefficients = exponential(self.points)
        errors = []
        for p in self.points:
            expected_y = np.exp(coefficients[0] * p[0] + coefficients[1])
            error = abs(p[1] - expected_y)
            errors.append(error)
        return np.mean(errors) < self.threshold

    def is_logarithmic(self):
        global coefficients
        coefficients = logarithmic(self.points)
        errors = []
        for p in self.points:
            expected_y = coefficients[0] * np.log(p[0]) + coefficients[1]
            error = abs(p[1] - expected_y)
            errors.append(error)
        return np.mean(errors) < self.threshold

    def predict_y(self, x):
        global coefficients
        if self.is_linear():
            predict_y = coefficients[0] * x + coefficients[1]
            return int(predict_y)
        elif self.is_exponential():
            predict_y = np.exp(coefficients[0] * x + coefficients[1])
            return int(predict_y)
        elif self.is_logarithmic():
            predict_y = coefficients[0] * np.log(x) + coefficients[1]
            return int(predict_y)
        else:
            return False