globalVar = 1 # глобальная переменная

def printGlobal():
	print(globalVar) #1

def printLocal():
	local = 2 # локальная переменная
	print(globalVar)
	print(local) #2
	
printLocal()    
