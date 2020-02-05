import datetime
def cur_time(pos,time,time_zone):
    t=time_zone[pos]
    x=dict(zip(time_zone,time))
    h1=float(datetime.datetime.now().strftime("%H"))
    m1=float((datetime.datetime.now().strftime("%M")))/60
    t1=h1+m1+float(x[t])
    if t1<0:
        t1=12+t1
    t1=t1*60
    h=int((t1/60))
    m=int(t1%60)
    s=str(h)+':'+str(m)
    return s,t
def lang(pos,language):
    return language[pos]
def cur_val(pos,currency_rate,currency):
    return float(currency_rate[pos]),currency[pos]


country=["UK","USA","INDIA","MEXICO","AUSTRALIA"]
time_zone=("GMT","EST","IST","CST","ADET")
time=("-5.5","-10.5","0.0","-11.5","5.5")
currency=('POUND','USD','INR','USD','AUD')
language=('ENGLISH','ENGLISH','HINDI','SPANISH','ENGLISH')
currency_rate=['92.72','71.32','1','71.32','47.73']

cntry=input("Enter country name from (UK,USA,MEXICO,AUSTRALIA):")
amt=int(input("Enter amount in INR:"))
for i in range(0,len(country)):
    if country[i]==cntry:
        pos=i
print("\nCountry:",cntry)
t,z=cur_time(pos=pos,time_zone=time_zone,time=time)
print("Current Time:",t,z)
print("Language:",lang(pos,language))
currency_value,currency_name=cur_val(pos,currency_rate,currency)
print("Currency Value:",currency_value,"INR")
s="Equivalent Currency value for {0} INR : {1} {2}"
eq_cur_val= lambda a,b:a/b
print(s.format(amt,eq_cur_val(amt,currency_value),currency_name))