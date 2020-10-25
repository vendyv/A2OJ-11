"""
83 Cards with Numbers - https://codeforces.com/problemset/problem/254/A 
"""
def main():
	with open("input.txt",'r') as f:
		N = int(f.readline().rstrip())
		arr = list(map(int,f.readline().rstrip().split()))	
	number = {}
	for i in range(len(arr)):
		if arr[i] in number:
			number[arr[i]].append(i+1)
		else:
			number[arr[i]] = [i+1]
	# print(number)
	# print(len(number[20]))
	for key in number:
		if len(number[key])%2!=0:
			with open("output.txt",'w') as f:
				print(key)
				f.write("-1")
				return
	with open("output.txt",'w') as f:
		for key in number.keys():
			x = number[key]
			for y in x:
				f.write(str(y)+" ")
			f.write('\n')
 
 
main()