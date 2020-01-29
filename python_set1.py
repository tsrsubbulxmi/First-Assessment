#==================1===============

print("Enter 3 numbers")
x=eval(input())
y=eval(input())
z=eval(input())
l=[]
l.append(x)
l.append(y)
l.append(z)
big=0
for i in range(0,3):
    if(l[i]%2==0):
        continue
    else:
        if l[i]>big:
            big=l[i]
if big==0:
    print("No odd numbers in list")
else:
    print("Maximum odd number",big)
	
#==================2===============

def right_justify(s):
    for i in range(0,70-len(s)):
        print(end=' ')
    print(s)
right_justify("cigna")

#==================3===============

l=[]
print("Enter 10 numbers")
for i in range(0,10):
    a=int(input())
    l.append(a)
print(l)
big=0
for i in range(0,10):
    if(l[i]%2==0):
        continue
    else:
        if l[i]>big:
            big=l[i]
if big==0:
    print("No odd numbers in list")
else:
    print(big)

#==================4a==============

r=int(input("Enter the radius of the sphere"))
pi=3.14
v=(4/3)*pi*r**3
print(v)

#==================4b==============

cp=24.95
disc=0.4
ad_cpy=59
cost=(cp*disc)+3+((cp*disc*ad_cpy)+(ad_cpy*0.75))
print(cost)

#==================4c==============

lt=(6*60*60)+(52*60)
ep=(8*60)+15
t=(7*60)+12
at=(ep*2)+(t*3)
arr_time=lt+at
h=int(arr_time/(60*60))
m=int((arr_time%(60*60))/60)
s=int((arr_time%(60*60))%60)
print(h,':',m,':',s)

#==================5===============

root=1
a=int(input("Enter the number\n"))
while(root<a):
    for power in range(1,7):
        if root ** power==a:
            print(root," ",power)
    root=root+1

#==================6===============

s=input("Enter the string")
a=s.split(',')
print(a)
sum1=0.0
for i in range(0,len(a)):
    sum1=sum1+float(a[i])
print(sum1)

#==================7===============

def isIn(str1,str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False
a=input("Enter the first string")
b=input("Enter the second string")
print(isIn(a,b))

#==================8===============

def getRatios(vect1,vect2):
    l=[]
    for i in range(0,len(vect1)):
        try:
            l.append(int(vect1[i]/vect2[i]))
        except:
            print(vect1[i],'/',vect2[i],"is not possible")
    return l
l1=[6,8,9,4,45,25]
l2=[3,4,2,2,0,5]
print(getRatios(l1,l2))

#==================9===============

width = 17
height = 12.0
delimiter = '.'
print(width/2)
#8
print(width/2.0)
#8.5
print(height/3)
#4.0
print(1 + 2 * 5)
#11
print(delimiter * 5)
#.....

#10 A)infite loop with low and high value=0

#================10 B)===============
 
 x = -125
epsilon = 0.01
numGuesses = 0
low = 0.0
y=abs(x)
high = max(1.0, y)
ans = (high + low)/2.0
while abs(ans**3 - y) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < y:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

