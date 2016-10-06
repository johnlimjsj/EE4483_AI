#!/usr/bin/env python
from fractions import Fraction
cnt=0
def findRoot(subj, rootv):
	def _findRoot(x_knext, x_k):
		global cnt
		cnt+=1
		if (abs(x_knext - x_k) < 0.0000000001):
			return x_knext;
		else:
			return _findRoot(_findNextRootIteration(x_knext), x_knext);

	def _findNextRootIteration(x_k):
		return ((rootv-1.0)*x_k + subj/(pow(x_k,rootv-1))) /rootv;

	x0 = 1.0;
	x1 = _findNextRootIteration(x0);

	return _findRoot(x1, x0);


def findPower(x, power):
	operand = x

	def _findPower(x, power):
		if power <= 1:
			return x
		else:
			return _findPower(x*operand, power-1)

	return _findPower(x,power)


def findPowAndRoot(subj, power, root):
	
	final = findRoot(subj, root)
	final = pow(final, power)
	return final

def GetRange(subj,pwr):
    range=1
    subj = abs(subj)
    while (pow(range,pwr) < subj):
        range*=2
    return (range/2,range)
count = 0

def BinSearch(first,last,subj,pwr):
	# If you want to floor the root include below:
    # w1 = x - pow(a,n)
    # w2 = pow(b,n) - x
    global count
    count+=1
    first=abs(first)
    last=abs(last)
    if (last <= first+0.0000000001):
    	if subj < 0: return -first
    	else: return first
        # if w1 < w2: return a
        # else: return b
    mid = (float(first)+last)/2
    if (abs(subj) < pow(mid,pwr)) :
        return BinSearch(first,mid,subj,pwr)
    else:
        return BinSearch(mid,last,subj,pwr)

def findBinRoot(num, power, root):
	num = pow(num,power)
	first,last = GetRange(num,root)
	return BinSearch(first,last,num,root)

# numer, denom = (1.25).as_integer_ratio()
# print numer
# print denom
# a = Fraction(0.6).limit_denominator()
# print a.numerator
# print a.denominator
while(1):
	number = input('Enter a number you want to perform a root opertion on: ')
	print "Next I will ask you to input the power. "
	print "If you want the number to have a power of 3/5 for instance: "
	print " when prompted to key in the power: key in '3' "
	print "when prompted to key in the root, key in '5' "
	power = input('Enter the power: ')
	root = input("Enter the root: ")
	print root%2
	if(number<0 and root%2==0): 
		print "Invalid input. Answer is not a real number. Please Key in again"
	else: break
	
# ans = findPowAndRoot(999,3,5)
ans_bin = findBinRoot(number,power,root)
ans_newton = findPowAndRoot(number, power, root)
print "Performing operation of ", number, "^", power, "/", root
print "Power by the Binary Search Algorithm: ", ans_bin
print "binary search iterations: ", count
print "Power by the Newton Rhapsodian Algorithm: ", ans_newton
print "newton method iterations: ", cnt





