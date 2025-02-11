import scipy.stats as stats
import numpy as np


class SignalDetection:
   def __init__(self, hits, misses, false_alarms, correct_rejections):
       self.hits = hits
       self.misses = misses
       self.false_alarms = false_alarms
       self.correct_rejections = correct_rejections


   def hit_rate(self):
       return (self.hits) / (self.hits + self.misses)


   def false_alarm_rate(self):
       return (self.false_alarms) / (self.false_alarms + self.correct_rejections) 


   def d_prime(self):
       hit_rate = self.hit_rate()
       false_alarm_rate = self.false_alarm_rate()


       z_hit = stats.norm.ppf(hit_rate)
       z_false_alarm = stats.norm.ppf(false_alarm_rate)


       return z_hit - z_false_alarm


   def criterion(self):
       hit_rate = self.hit_rate()
       false_alarm_rate = self.false_alarm_rate()


       z_hit = stats.norm.ppf(hit_rate)
       z_false_alarm = stats.norm.ppf(false_alarm_rate)


       return -0.5 * (z_hit + z_false_alarm)