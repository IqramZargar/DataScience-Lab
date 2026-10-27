from scipy import stats

data = [10, 20, 20, 30, 40]

print("Mean:", stats.tmean(data))
print("Median:", stats.scoreatpercentile(data, 50))
print("Mode:", stats.mode(data).mode)