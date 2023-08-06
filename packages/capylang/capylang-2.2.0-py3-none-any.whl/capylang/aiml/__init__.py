import statistics

def mean(arr):
  return float(sum(arr)) / max(len(arr), 1)

def median(arr):
  return statistics.median(arr)

def mode(arr):
  return statistics.mode(arr)