#D.R.Y. = don't repeat yourself
#W.E.T = we write everything twice (don't do this)



#when you get an error
#1. what you are trying to do
#2. what the error is
#3. how to fix it

#error: greeting take no arguement, 1 given. 
#this means that it doesn't want any arguements

def greeting():
	name = raw_input("What is your name?")
	print "Hello, " + name

#this is called the function definition. 
#'name' will be equal to whatever is in the brackets
def hello(name):
	print "Hello, " + name
	
hello("Rebecca")
## see? run it and it will work

def add(a, b):
	return a + b
print add (2, 3)





	

