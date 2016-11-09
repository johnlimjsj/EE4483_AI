#!/usr/bin/env python

from copy import deepcopy

class Swap():
	def left(self):
		print 'left'

class Dir():
	swap = Swap()
	def __init__(self):
		self.u = True
		self.d = True
		self.l = True
		self.r = True
		self.marker = "x"
		self.sumHeu = 0
		self.marker_pos = (-1, -1)

	def getAvailableDir(self, coord):
		row = coord[0]
		col = coord[1]
		if row == 0:
			self.u=False
		elif row==2 :
			self.d = False
		else :
			self.u = True
			self.d = True

		if col==0 :
			self.l = False
		elif col==2 :
			self.r = False
		else :
			self.l = True
			self.r = True

	def swapLeft(self, array, coord):
		row = coord[0]
		col = coord[1]
		newArray = deepcopy(array)
		buffer = array[row][col]
		newArray[row][col] = array[row][col-1]
		newArray[row][col-1] = buffer
		return newArray

	def swapRight(self, array, coord):
		row = coord[0]
		col = coord[1]
		newArray = deepcopy(array)
		buffer = array[row][col]
		newArray[row][col] = array[row][col+1]
		newArray[row][col+1] = buffer
		return newArray

	def swapUp(self, array, coord):
		row = coord[0]
		col = coord[1]
		newArray = deepcopy(array)
		buffer = array[row][col]
		newArray[row][col] = array[row-1][col]
		newArray[row-1][col] = buffer
		return newArray

	def swapDown(self, array, coord):
		row = coord[0]
		col = coord[1]
		newArray = deepcopy(array)
		buffer = array[row][col]
		newArray[row][col] = array[row+1][col]
		newArray[row+1][col] = buffer
		return newArray

	def printm(self):
		print self.marker
		# self.printm()


	def printSum(self):
		self.printm();

	def getHeuristics(self, sol_arr, in_arr):
		numTilesOut = 0
		distance = 0
		for r in range(0,3):
			for c in range(0,3):
				if in_arr[r][c] == self.marker:
					self.marker_pos = (r, c)
				else:
					if in_arr[r][c] != sol_arr[r][c]:
						numTilesOut += 1
						#traverse to find the exact r,c, coordinates of the item in the sol_arr
						for _r in range(0,3):
							for _c in range(0,3):
								if sol_arr[_r][_c] == in_arr[r][c]:
									distance += (abs(_r - r) + abs(_c - c))
									break
		return numTilesOut+distance


	def solvePuzzle(self, sol_arr, in_arr):
		buff_in_arr = deepcopy(in_arr)
		swap = Swap()
		
		#check for invalid inputs
		if invalidSolAndInputPuzzle(sol_arr, in_arr):
			return "Invalid inputs detected. SOlution and Input have different elements"

		self.getHeuristics(sol_arr, in_arr) #to set marker position
		marker_pos = self.marker_pos
		

		self.getAvailableDir(self.marker_pos)
		printPuzzle(in_arr)

		sumH = {'up':999, 'down':999, 'left':999, 'right':999,  }
		if self.u :
			sumH['up'] = self.getHeuristics(sol_arr, self.swapUp(in_arr, marker_pos)) #why does this perform an upward swap?  
		if self.d :
			sumH['down'] = self.getHeuristics(sol_arr, self.swapDown(in_arr, marker_pos))
		if self.l :
			sumH['left'] = self.getHeuristics(sol_arr, self.swapLeft(in_arr, marker_pos))
		if self.r :
			sumH['right'] = self.getHeuristics(sol_arr, self.swapRight(in_arr, marker_pos))

		print sumH
		printPuzzle(in_arr)
		direction = min(sumH, key=sumH.get)
		raw_input('Press any key to continue')
		if direction == 'up':
			print direction
			print "marker position: ", marker_pos
			new_inarr = self.swapUp(in_arr, marker_pos)
			self.solvePuzzle(sol_arr, new_inarr)
		if direction == 'down':
			print direction
			new_inarr = self.swapDown(in_arr, marker_pos)
			self.solvePuzzle(sol_arr, new_inarr)
		if direction == 'left':
			print direction
			new_inarr = self.swapLeft(in_arr, marker_pos)
			self.solvePuzzle(sol_arr, new_inarr)
		if direction == 'right':
			print direction
			new_inarr = self.swapRight(in_arr, marker_pos)
			self.solvePuzzle(sol_arr, new_inarr)


		





def itemInList(item, list_2d):
	return any(item in sublist for sublist in list_2d)

def inputPuzzle():
	#initialization
	puzzle_arr = [["" ,"",""],["","",""],["","",""]]
	#user inputs to generate puzzle array


	for row in range(0,3):
		for col in range(0,3):
			basestr = 'provide an entry for row ' + str(row) + ' and column ' + str(col) + ': '
			while (1) :
				input_buffer = raw_input(basestr)
				if itemInList(input_buffer, puzzle_arr):
				# if any( input_buffer in sub_puzzle_arr for sub_puzzle_arr in puzzle_arr):
					print "Invalid Input! Please key in a unique value"
				else: 
					puzzle_arr[row][col] = input_buffer
					break
	global marker
	while(1) :
		marker = raw_input('Please identify the Marker from one of your inputs: ')


	return puzzle_arr		

def printPuzzle(puzzlearray):
	s = "|"
	for row in puzzlearray:
		print s.join(row)

def invalidSolAndInputPuzzle(sol_arr, in_arr):
	for row in range(0,3):
		for col in range(0,3):
			#checks whether any elemet of input is not inside the solution array
			if not itemInList(in_arr[row][col],sol_arr):
				return True;
	return False

def solvePuzzle(sol_arr, in_arr):
	global marker
	print "step: "
	printPuzzle(in_arr)
	k = raw_input('Press any key to continue')
	traversedCoord = []
	#check for invalid inputs
	if invalidSolAndInputPuzzle(sol_arr, in_arr):
		return "Invalid inputs detected. SOlution and Input have different elements"

	numTilesOut = 0
	distance = 0
	sumHeuristics = 0
	#traverse the 2d list one by one
	for r in range(0,3):
		for c in range(0,3):
			if in_arr[r][c] == marker:
				marker_pos = (r, c)
			else:
				if in_arr[r][c] != sol_arr[r][c]:
					numTilesOut += 1
					#traverse to find the exact r,c, coordinates of the item in the sol_arr
					for _r in range(0,3):
						for _c in range(0,3):
							if sol_arr[_r][_c] == in_arr[r][c]:
								distance += (abs(_r - r) + abs(_c - c))
								break
	
	sumHeuristics = numTilesOut+distance		
	if sumHeuristics == 0: #solution has been found
		return
	else:
		d.getAvailableDir(marker_pos)
		if d.u :
			solvePuzzle(sol_arr, d.swapUp(in_arr, marker_pos))
		if d.l :
			solvePuzzle(sol_arr, d.swapLeft(in_arr, marker_pos))

	return (numTilesOut, distance)




# after solving, it generates the array, then calls the method generatePuzzle to print it
# generatePuzzle(list);
# printPuzzle(inputPuzzle())
# anarray =  inputPuzzle()

# a1 = [["1","2","3"],["4","5","6"],["7","8","9"]]
a1 = [["2","8","3"],["1","6","4"],["x","7","5"]]
# a2 = [["1","2","3"],["4","5","6"],["7","8","9"]]
a2 = [["1","2","3"],["8","x","4"],["7","6","5"]]
marker = "x"
d = Dir()
d.solvePuzzle(a1, a2)

# a3 = deepcopy(a2)
# printPuzzle(a2)
# printPuzzle(d.swapLeft(a2, (1,1)))
# printPuzzle(a3)

# d[1].getAvailableDir(2, 1)

# print "Up", d[1].u
# print "Down", d[1].d
# print "Left", d[1].l
# print "Right", d[1].r

# d[1].getAvailableDir(2, 2)
# print "Up", d[1].u
# print "Down", d[1].d
# print "Left", d[1].l
# print "Right", d[1].r


# kkk = [(1,2), (3,4)]

# kkk.append((1,3))
# print kkk

# if (1,3) in kkk:
# 	print 'hahaha'
















