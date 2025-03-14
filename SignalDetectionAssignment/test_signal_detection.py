import unittest
from signal_detection import SignalDetection

class TestSignalDetection(unittest.TestCase):
    def test_d_prime_zero(self):
        sd = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_d_prime_nonzero(self):
        sd = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_criterion_zero(self):
        sd = SignalDetection(5, 5, 5, 5)
        expected = 0
        obtained = sd.criterion()
        self.assertAlmostEqual(obtained, expected, places=6)

    def test_criterion_nonzero(self):
        sd = SignalDetection(15, 10, 15, 5)
        expected = -0.463918426665941
        obtained = sd.criterion()
        self.assertAlmostEqual(obtained, expected, places=6)

if __name__ == '__main__':
    unittest.main()
