s1 = str(input("enter string 1"))
s2 = str(input("enter string 2"))
s3 = str(input("enter string 3"))
s4 = str(input("enter string 4"))
s5 = str(input("enter string 5"))
s6 = str(input("enter string 6"))
s7 = str(input("enter string 7"))
s8 = str(input("enter string 8"))
s9 = str(input("enter string 9"))
s10 = str(input("enter string 10"))
s11 = str(input("enter string 11"))
s12 = str(input("enter string 12"))
s13 = s1 + s2 + s3
s14 = s4 + s5 + s6
s15 = s7 + s8 + s9
sa = s13 + s14 + s15
srev = sa[::-1]
if sa == srev :
    print("\n",sa,"is palindrome")
else :
    print("\n",sa,"is not palindrome")
    
"""better version using lists and taking every group of 3 strings :


list= [""] * 12
for i in range (12):
    str1=raw_input("enter name:")
    list[i]=str1
i=0
for i in range (10):
    strr=list[i]+list[1+i]+list[i+2]
    l=len(strr)-1
    str2=""
    while (l>=0):
       str2+=strr[l]
       l=l-1
    if(strr==str2):
       print "palindrome"
    else:
       print "not palindrome"
       
       """
