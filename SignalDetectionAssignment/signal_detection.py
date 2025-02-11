import numpy as np
from scipy.stats import norm

class SignalDetection:
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        self.hits = hits
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections

    def hit_rate(self):
        return self.hits / (self.hits + self.misses) if (self.hits + self.misses) > 0 else 0.5

    def false_alarm_rate(self):
        return self.falseAlarms / (self.falseAlarms + self.correctRejections) if (self.falseAlarms + self.correctRejections) > 0 else 0.5

    def d_prime(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()

        # Correction for edge cases
        H = np.clip(H, 1e-5, 1 - 1e-5)
        FA = np.clip(FA, 1e-5, 1 - 1e-5)

        d_prime_value = norm.ppf(H) - norm.ppf(FA)
        print(f"Hit Rate: {H}, False Alarm Rate: {FA}, d': {d_prime_value}")
        return d_prime_value

    def criterion(self):
        H = self.hit_rate()
        FA = self.false_alarm_rate()

        # Correction for edge cases
        H = np.clip(H, 1e-5, 1 - 1e-5)
        FA = np.clip(FA, 1e-5, 1 - 1e-5)

        criterion_value = -0.5 * (norm.ppf(H) + norm.ppf(FA))
        print(f"Criterion: {criterion_value}")
        return criterion_value
