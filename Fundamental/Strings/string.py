#Multi line string 
myString = """This is 
a multiline 
string"""
print(myString)

#Universal Newline \n
#https://www.python.org/dev/peps/pep-0278/
myString = 'This string\nspans mutiple\nlines'
print(myString)

#Escape Characters 
myString = "This is a \" and \' in a string."
print(myString)

#Escape Characters ASCII Bell (BEL)
#https://docs.python.org/3/reference/lexical_analysis.html#strings
myString = "This is \a in a string."
print(myString)

#Define paths
myPath = r'I:\Web Developments\Python\Dev\python-exercises'
print(myPath)

#creating integers
print(str(1985))
print(str(6.02e23))

#Index accessing of string
myString = "Python is awesome"
print(myString[2]) #t
print(type(myString[2])) #<class 'str'>

#Get help
#https://docs.python.org/2/library/string.html
c = 'oslo'
print(c.capitalize())
print(c)