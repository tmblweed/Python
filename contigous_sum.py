seq = [2,-8,3,-2,4,-10]
b = [4, -2, -8, 5, -2, 7, 7, 2, -6, 5]

def mssl(x):
    max_ending_here = max_so_far = 0
    for a in x:
        max_ending_here = max(0, max_ending_here + a)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print mssl(seq)
