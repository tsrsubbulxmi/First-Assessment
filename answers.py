a="Hello World!"
print(a[-1::-1])

s="AcCeNtUrE"
print(s.swapcase())

a="accenture"
dic={}
for i in a:
    dic[i]=0
    for k in a:
        if i==k:
            dic[i]=dic.get(i)+1
print(dic)

l=[]
odd_list=[]
even_list=[]
for i in range(1,51):
    l.append(i)
for i in l:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("List")
print(l)
print("Odd List")
print(odd_list)
print("Even List")
print(even_list)


l=[]
for i in range(1,51):
    if i%3==0 and i%5==0:
        l.append("fizz-buzz")
    elif i%3==0:
        l.append("fizz")
    elif i%5==0:
        l.append("buzz")
    else:
        l.append(i)
print(l)

a=0
e=0
u=0
s="accenture"
for i in s:
    if i == 'a':
        a=a+1 
    if i == 'e':
        e=e+1
    if i == 'u':
        u=u+1
s1="{0}a{1}e{2}u"
print(s1.format(a,e,u))

s="ga24nbv2k6jg523jg2545lsfwe"
a="1234567890"
sum1=0
char=0
for i in s:
    if i in a:
        sum1=sum1+int(i)
    else:
        char=char+1
print("\nSum of digits",sum1)
print("Character count",char)

l=[1,2,3,4,5,6,7,8,9,10]
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[j]+l[i]==9:
            print(l[i],l[j])

a=input("Enter the first string")
b=input("Enter the second string")
if(sorted(a)==sorted(b)):
    print("Anagram")
else:
    print("Not an Anagram")

flag=0
a=int(input("Enter the number\n"))
for i in range(2,int(a/2)+1):
    if a%i==0:
        print("Not a prime")
        flag=1
        break
if flag==0:
    print("prime")
divisor=[]
primedivisor=[]
if flag==1:
    for i in range(2,int((a/2)+1)):
        if a%i==0:
            divisor.append(i)
print(divisor)
for i in divisor:
    for k in range(2,int(i/2)+1):
        if i%k==0:
            break
    else:
        primedivisor.append(i)
print(primedivisor)

tup=(1,2,3,4,5)
print(tup)
l=list(tup)
l.append('a')
tup=tuple(l)
print(tup)

s=input("Enter the string")
s1=s[-1::-1]
if s==s1:
    print(s+" "+s1+" "+"Palindrome")
else:
    print(s+" "+s1+" "+"Not a Palindrome")

n=int(input("Enter the multiplier"))
for i in range(1,21):
    s="{0}*{1}={2}"
    print(s.format(i,n,i*n))

a=-1
b=1
c=a+b
while(c<=50):
    print(c)
    a=b
    b=c
    c=a+b

s="green-red-yellow-black-white"
st=s.split("-")
x=sorted(st)
y='-'.join(x)
print(y)

def uniquelist(mylist=[]):
    ul=[]
    for i in mylist:
        if i not in ul:
            ul.append(i)
    return ul
l=[1,2,3,3,3,3,4,5]
uniquel=uniquelist(l)
print(uniquel)

s="abcdeghijklmnopqrstuvwxyz"
a="The quick brown fox jumps over the lazy dog"
flag=0
for i in s:
    if i not in a:
        flag=1
        break
if flag==0:
    print("Panagram")
else:
    print("Not a Panagram")

l=[]
print("Enter 5 numbers")
for i in range(0,5):
    a=int(input())
    l.append(a)
print(l)
big=0
for i in range(0,5):
    if(l[i]%2==0):
        continue
    else:
        if l[i]>big:
            big=l[i]
if big==0:
    print("No odd numbers in list")
else:
    print(big)

r=float(input("Enter the radius"))
print(3.14*r*r)

n=int(input("Enter the number"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
