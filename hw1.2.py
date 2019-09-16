'''
Yili Lin
1/22/2019
I have not given or received any unauthorized assistance on this assignment
'''
#2
#a prime
def detprime(num):
    'determin the prime number'
    if type(num) is not int or num<=1:# determin for positive init
        return False
    elif num==2: #2 is prime
        return True
    else:
        for i in range(2,num):
            if num%i==0: #determin for prime
                return False
        return True
#b happy
def dethappy(num):
    'determin the happy number'
    past_num=set() # past set of number
    while num>1 and num not in past_num:
        past_num.add(num) #add number to the number list
        num=sum(int(i)**2 for i in list(str(num))) #calculate sum
    return num==1

#c happy prime
def dethappyprime(num):
    'determin the happy prime number'
    if detprime(num)==True and dethappy(num)==True:
        return True
    else:
        return False

#d
'print first 20 prime number'
primelist= []
i=0 #count
j=1 #number
while i < 20:
    if detprime(j)==True:
        primelist.append(j) #add number to list
        j+=1 #for next number
        i+=1 #count
    else:
        j+=1
print ('First 20 primes are '+str(primelist))

#e
'print first 20 happy number'
happylist=[]
i=0 #count
j=1 #number
while i < 20:
    if dethappy(j)==True:
        happylist.append(j)
        j+=1
        i+=1#count for 20
    else:
        j+=1
print ('First 20 happy numbers are '+str(happylist))

#f
'print first 20 happy prime number'
happyprimelist=[]
i=0
j=1
while i < 20:
    if dethappyprime(j)==True:
        happyprimelist.append(j)#add to list
        j+=1
        i+=1  #count for 20
    else:
        j+=1
print ('First 20 happy primes are '+str(happyprimelist))

#g
'print first 20 sad number'
sadprimelist=[]
i=0
j=1
while i < 20:
    if dethappyprime(j)==False and detprime(j)==True:
        sadprimelist.append(j)#add to list
        j+=1
        i+=1  #count for 20
    else:
        j+=1
print ('First 20 sad primes are '+str(sadprimelist))