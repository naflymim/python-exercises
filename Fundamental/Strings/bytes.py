myByte = b'some bytes test'
print(myByte.split())
print(myByte.split()[1])

#uniocde 
#https://www.ltg.ed.ac.uk/~richard/unicode-sample.html

#Convert byte to str
myString = 'Æ Ø Å æ ø å'
#b'\xc3\x86 \xc3\x98 \xc3\x85 \xc3\xa6 \xc3\xb8 \xc3\xa5'
data = myString.encode("utf-8")
print(data)

myString = data.decode("utf-8")
print(myString)
