import unittest
import math
from signal_detection import SignalDetection  # Adjust this import as needed for your project structure

class TestSignalDetectionAdditional(unittest.TestCase):
    def test_hit_rate_at_upper_bound(self):
        """
        When all signal trials are hits, the raw hit rate is 1.0.
        With correction, it should be: 1 - 0.5 / (hits + misses)
        """
        hits = 20
        misses = 0
        sd = SignalDetection(hits, misses, falseAlarms=5, correctRejections=5)
        expected = 1 - 0.5 / (hits + misses)
        obtained = sd.hit_rate()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_false_alarm_rate_at_upper_bound(self):
        """
        When all noise trials are false alarms, the raw false alarm rate is 1.0.
        With correction, it should be: 1 - 0.5 / (falseAlarms + correctRejections)
        """
        falseAlarms = 15
        correctRejections = 0
        sd = SignalDetection(hits=5, misses=5, falseAlarms=falseAlarms, correctRejections=correctRejections)
        expected = 1 - 0.5 / (falseAlarms + correctRejections)
        obtained = sd.false_alarm_rate()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_hit_rate_at_lower_bound(self):
        """
        When no signal trial is a hit, the raw hit rate is 0.
        With correction, it should be: 0.5 / (hits + misses)
        """
        hits = 0
        misses = 20
        sd = SignalDetection(hits, misses, falseAlarms=5, correctRejections=5)
        expected = 0.5 / (hits + misses)
        obtained = sd.hit_rate()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_false_alarm_rate_at_lower_bound(self):
        """
        When no noise trial is a false alarm, the raw false alarm rate is 0.
        With correction, it should be: 0.5 / (falseAlarms + correctRejections)
        """
        falseAlarms = 0
        correctRejections = 30
        sd = SignalDetection(hits=5, misses=5, falseAlarms=falseAlarms, correctRejections=correctRejections)
        expected = 0.5 / (falseAlarms + correctRejections)
        obtained = sd.false_alarm_rate()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_no_signal_trials(self):
        """
        When there are no signal trials (hits + misses == 0), hit_rate should return 0.0.
        """
        sd = SignalDetection(hits=0, misses=0, falseAlarms=10, correctRejections=10)
        expected = 0.0
        obtained = sd.hit_rate()
        self.assertEqual(obtained, expected)

    def test_no_noise_trials(self):
        """
        When there are no noise trials (falseAlarms + correctRejections == 0), false_alarm_rate should return 0.0.
        """
        sd = SignalDetection(hits=10, misses=10, falseAlarms=0, correctRejections=0)
        expected = 0.0
        obtained = sd.false_alarm_rate()
        self.assertEqual(obtained, expected)

    def test_output_types(self):
        """
        Ensure that both d_prime() and criterion() return float values.
        """
        sd = SignalDetection(hits=15, misses=10, falseAlarms=15, correctRejections=5)
        self.assertIsInstance(sd.d_prime(), float)
        self.assertIsInstance(sd.criterion(), float)

    def test_extreme_values_finite(self):
        """
        Even when using extreme inputs (e.g., all hits and all false alarms),
        d_prime and criterion should return finite numbers.
        """
        sd = SignalDetection(hits=100, misses=0, falseAlarms=100, correctRejections=0)
        dprime_val = sd.d_prime()
        crit_val = sd.criterion()
        self.assertTrue(math.isfinite(dprime_val), "d_prime should be finite")
        self.assertTrue(math.isfinite(crit_val), "criterion should be finite")

if __name__ == '__main__':
    unittest.main()
