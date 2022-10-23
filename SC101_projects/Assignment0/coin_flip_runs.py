"""
File: coin_flip_runs.py
Name: Sharon
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r


def main():
	"""
	input number of runs
	coin flip results will reach the runs
	print the coin flip results
	"""
	print("Let's flip a coin!")
	runs = int(input('Number of runs: '))
	ans = ""
	coin1 = r.randint(1, 2)
	run = 0
	ans += str(coin1)
	is_in_a_roll = False
	while run != runs:
		coin2 = r.randint(1, 2)
		ans += str(coin2)
		if coin1 == coin2:
			if not is_in_a_roll:
				run += 1
				is_in_a_roll = True
		else:
			is_in_a_roll = False
		coin1 = coin2
	run_result = ""
	for i in range(len(ans)):
		if ans[i] == '1':
			run_result += 'H'
		else:
			run_result += 'T'
	print(run_result)


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
