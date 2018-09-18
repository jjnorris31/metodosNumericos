def get_abs_sum(lst):
	res = [i * -1 for i in lst if i < 0]
	res += [i for i in lst if i > 0]
	return sum(res)
