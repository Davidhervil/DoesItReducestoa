A={'a','ac','bc','ca'}
B={'b','ab','bb','aa'}
C={'c','ba','cb','cc'}
def reduces(to,string):
	n=len(string)
	#print('Recursion',to,string)
	if n==0:
		return False
	does1=does2=does3=False
	if to == 'a':
		if string in A:
			return True
		for i in range(0,n):
			does1 =	(reduces('a',string[0:i]) and reduces('c',string[i:n]) )
			if does1:
				A.add(string)
				return True
			does2 =	(reduces('b',string[0:i]) and reduces('c',string[i:n]) )
			if does2:
				A.add(string)
				return True
			does3 =	(reduces('c',string[0:i]) and reduces('a',string[i:n]) )
			if does3:
				A.add(string)
				return True
		return False
	elif to == 'b':
		if string in B:
			return True
		for i in range(0,n):
			does1 = (reduces('a',string[0:i]) and reduces('b',string[i:n]) )
			if does1:
				B.add(string)
				return True
			does2 =	(reduces('b',string[0:i]) and reduces('b',string[i:n]) )
			if does2:
				B.add(string)
				return True
			does3 =	(reduces('a',string[0:i]) and reduces('a',string[i:n]) )
			if does3:
				B.add(string)
				return True
		return False
	else:
		if string in C:
			return True
		for i in range(0,n):
			does1 = (reduces('b',string[0:i]) and reduces('a',string[i:n]) )
			if does1:
				C.add(string)
				return True
			does2 =	(reduces('c',string[0:i]) and reduces('b',string[i:n]) )
			if does2:
				C.add(string)
				return True
			does3 =	(reduces('c',string[0:i]) and reduces('c',string[i:n]) )
			if does3:
				C.add(string)
				return True
		return False

seq = raw_input()
print(len(seq))
print(reduces('a',seq))
print(A)
print(B)
print(C)
