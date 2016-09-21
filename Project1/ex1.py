#!/usr/bin/env python
from fractions import Fraction

def findRoot(subj, rootv):
	def _findRoot(x_knext, x_k):
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

def GetRange(x,n):
    y=1
    while (pow(y,n) < x):
        y*=2
    return (y/2,y)

def BinSearch(a,b,x,n):
	# If you want to floor the root include below:
    # w1 = x - pow(a,n)
    # w2 = pow(b,n) - x
    if (b <= a+0.00000000001):
    	return a
        # if w1 < w2:
        #    return a
        # else:
        #    return b
    c = (float(a)+b)/2
    if (x < pow(c,n)) :
        return BinSearch(a,c,x,n)
    else:
        return BinSearch(c,b,x,n)

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

number = input('Enter a number you want to perform a root opertion on: ')
print "Next I will ask you to input the power. "
print "If you want the number to have a power of 3/5 for instance: "
print " when prompted to key in the power: key in '3' "
print "when prompted to key in the root, key in '5' "
power = input('Enter the power: ')
root = input("Enter the root: ")
# ans = findPowAndRoot(999,3,5)
ans_bin = findBinRoot(number,power,root)
ans_newton = findPowAndRoot(number, power, root)
print "Performing operation of ", number, "^", power, "/", root
print "Power by the Binary Search Algorithm: ", ans_bin
print "Power by the Newton Rhapsodian Algorithm: ", ans_newton





