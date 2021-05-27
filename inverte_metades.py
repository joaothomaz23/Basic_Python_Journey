string = 'hieroglifo'
str1 = ''
str2 = ''
if len(string)%2 == 0:
    for i in range(0,len(string),1):
        if i < (len(string))/2 :
            str1 = str1 + string[i]
            print(str1)
        else:
            str2 = str2 + string[i]
            print(str2)
else:
    for i in range(0,int(((len(string)-1)/2)),1):
        str1 = str1 + string[i]
        print(str1)
    for i in range(int(((len(string)-1)/2)+1),len(string),1):
        str2 = str2 + string[i]
        print(str2)
        
str1s = ''
str2s = ''
print('--------------------------------')
for j in range(len(str1)-1,-1,-1):
    str1s = str1s + str1[j]
    print(str1s)
for j in range(len(str2)-1,-1,-1):
    str2s = str2s + str2[j]
    print(str2s)
if len(string)%2 == 0:
    ans = str1s + str2s
else:
    e_m = string[int(round(len(string)/2))-1]
    ans = str1s + e_m + str2s
print(ans)
