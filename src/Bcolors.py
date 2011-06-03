from Mathstuff import mathstuff

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    Classname = ""

    def __init__(self, classname):
	self.Classname = classname

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def check(self, s):
	evalString = eval(self.Classname + "()." + s)
	if(evalString == True):
		self.printOK(s)
	elif(evalString == False):
		self.printFAIL(s)
	else:
		self.printWarning(s)

    def printOK(self, s):
	print self.OKGREEN + "OK Passed \t|\t " + s + self.ENDC

    def printFAIL(self, s):
	print self.FAIL + "Failed Test \t|\t " + s + self.ENDC

    def printWarning(self, s):
	print self.WARNING + "Error, Unknown \t|\t " + s + self.ENDC

