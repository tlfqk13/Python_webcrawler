

sampleFile=open('test.txt','r').read()
splitFile=sampleFile.strip()
splitList=[]
splitList2=[]

print(splitFile)

for i in splitFile:
    x=i.encode('utf-8')
    splitList.append(x)
    #print(x)


test="#\\ub538\\uae30\\uc5d0\\uc774\\ub4dc"
test2=test.split('\n')

for i in test2:
    x=i.encode('utf-8').decode('unicode-escape')
    #print(x)




print("*"*50)
