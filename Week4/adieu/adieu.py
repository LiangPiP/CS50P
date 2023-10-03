list=[]
str=''
while True:
    try:
        list.append(input("Name: "))
    except EOFError:
        break

print('')

if len(list)==1:
    str=list[0]
elif len(list)==2:
    str=list[0] + ' and ' + list[1]
else:
    for i in range(len(list)-1):
        str=str+list[i]+', '
    str=str+'and '+list[-1]
print("Adieu, adieu, to "+str)
