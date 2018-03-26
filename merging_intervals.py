def merge_intervals(intervals):
	sorted_intervals = sorted(intervals)
	results = [sorted_intervals[0]]
	for idx in xrange(1,len(sorted_intervals)):
		prior_interval = results[-1]
		current_interval = sorted_intervals[idx]

		if prior_interval[1] >= current_interval[0]:
			prior_interval[1]= max(prior_interval[1],current_interval[1])
		else:
			results.append(current_interval)
	return results
