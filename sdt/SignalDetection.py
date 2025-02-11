import scipy.stats as stats

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):

        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections

    def hit_rate(self):

        total_signals = self.hits + self.misses
        if total_signals == 0:
            raise ValueError("Total signal trials (hits + misses) must be greater than zero.")
        return self.hits / total_signals

    def false_alarm_rate(self):
        
        total_noise = self.false_alarms + self.correct_rejections
        if total_noise == 0:
            raise ValueError("Total noise trials (false alarms + correct rejections) must be greater than zero.")
        return self.false_alarms / total_noise

    def d_prime(self):
      
        # Calculate hit rate and false alarm rate
        hr = self.hit_rate()
        far = self.false_alarm_rate()
        # Clip extreme values
        epsilon = 1e-5
        hr = min(max(hr, epsilon), 1 - epsilon)
        far = min(max(far, epsilon), 1 - epsilon)
        return stats.norm.ppf(hr) - stats.norm.ppf(far)

    def criterion(self):
     
        hr = self.hit_rate()
        far = self.false_alarm_rate()
        epsilon = 1e-5
        hr = min(max(hr, epsilon), 1 - epsilon)
        far = min(max(far, epsilon), 1 - epsilon)
        return -0.5 * (stats.norm.ppf(hr) + stats.norm.ppf(far))
