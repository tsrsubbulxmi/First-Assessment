#==================1===============

def gcd(x,r):
    if r==0:
        return x
    else:
        return gcd(r,x%r)
a=int(input("Enter 1st no."))
b=int(input("Enter 2nd no."))
print('GCD:', gcd(a,b))

#==================2===============

def is_power(a,b):
    if b==0:
			return False
	if b==1 or b==-1:
        return True
    else:
        if a%b==0:
            return True
        else:
            return False

a=int(input("Enter a"))
b=int(input("Enter b"))
print(is_power(a,b))

#==================3===============

def factI(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def factR(n):
    if n==0:
        return 1
    elif n==1:
        return n
    else:
        return n*factR(n-1)
n=int(input("Enter the value"))
print(factI(n))
print(factR(n))

#==================4===============

a=input("Enter the number")
dec=0
for i in range(0,len(a)):
    dec=dec+(int(a[i])*(2**i))
print(dec)

#==================5===============
def sumDigits(s):
    a="1234567890"
    sum1=0
    flag=0
    for i in s:
        if i in a:
            flag=1
            sum1=sum1+int(i)
    try:
        if flag==0:
            raise ValueError("There is no digits in the string")
        else:
            return sum1
    except ValueError as e:
        print(e)
    #return sum1
s=input("Enter the string")
print("\nSum of digits",sumDigits(s))


#==================6===============

def findAnEven(l):
    for i in range(0,len(l)):
        try:
            if l[i]%2==0:
                print(l[i])
                break
            elif i==len(l)-1:
                raise ValueError("No Even Numbers in the List")
        except ValueError as e:
            print(e)

l=[3,25,11,13,15]
findAnEven(l)

#==================7===============

def isPalindrome(s):
    a="abdefghijklmnopqrstuvwxyz"
    st=s.lower()
    st1=''
    for i in st:
        if i in a:
            st1=st1+i
    s1=st1[-1::-1]
    str2=s1.lower()
    print(s)
    if st1==str2:
        return "Palindrome"
    else:
        return "Not a Palindrome"
def testIsPalindrome():
    s=input("Enter the string")
    return(isPalindrome(s))
print(testIsPalindrome())

#==================8===============

def eval_loop():
    s1=''
    while True:
        s=input("Enter the string")
        if s=='done':
            return s1
        else:
            s1=eval(s)
            print(s1)
print(eval_loop())        

#==================9===============
