def change(n, coins_available, coins_so_far):
	results = []
	if sum(coins_so_far) == n:  #if the sum of coins we used so far is our target, give that list
		results.append(coins_so_far)
	elif sum(coins_so_far) > n: #if sum is greater than target, then we went too far
		pass
	elif coins_available == []: #if there are no more coins to use, we need to pass
		pass
	else:
		for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]): #  coins_so_far+[coins_available[0]] = first coin available
			results.append(c)
		for c in change(n, coins_available[1:], coins_so_far):
			results.append(c)
	return results

n = 15
coins = [1, 5, 10, 25]
a = change(n, coins, [])

print a
