class Strong:
	def __init__(self,iNo):
		self.iNo = iNo

	def ChkStrong(self):
		iFact = 1
		iAdd = 0
		iNumber = self.iNo
		while(iNumber != 0):
			iDigit = int(iNumber % 10)
			while(iDigit != 0):
				iFact = iFact * iDigit
				iDigit -= 1
			iAdd = iAdd + iFact
			iFact = 1
			iNumber = int(iNumber / 10)
		if(iAdd == self.iNo):
			return True
		else:
			return False

if __name__ == "__main__":
	print("Enter Number")
	iNo = int(input())

	obj = Strong(iNo)

	if(obj.ChkStrong() == True):
		print("Strong Number")
	else:
		print("Not Solid")
