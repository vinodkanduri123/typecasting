#typecasting int to float boolean complex
a=10
print(float(a))
print(bool(a))
print(complex(a))

#output
#10.0
#True
#10
#(10+0j)


#typecasting float to int,boolean,complex
b=23.4
print(int(b))
print(bool(b))
print(complex(b))

#output

#23
#True
#(23.4+0j)
#23.4



#typecasting boolean to int,float,complex

c=True
print(int(c))
print(float(c))
print(complex(c))



#output

#1
#1.0
#(1+0j)


#typecasting boolean to int,float,complex
d=False
print(int(d))
print(float(d))
print(complex(d))



#output

#0
#0.0
#0j



#typecasting complex to int,float,boolean

e=5+6j
#print(int(e))  #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#print(float(e)) #TypeError: float() argument must be a string or a real number, not 'complex'
print(bool(e)) #True











