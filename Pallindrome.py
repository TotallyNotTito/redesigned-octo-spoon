pList = []
pInputs = int(input())
pList.append(pInputs)
size = 0

while(pInputs != -1):
    size = size + 1
    pInputs = int(input())

    if (pInputs != -1):
        pList.append(pInputs)

counter = size
position = 0
flag = 0

while (position < counter):
    if (pList[position] != pList[size-1] ):
        flag = 1
        position = counter + 1
        # print('pallendrome')
    else :
        # print('not a pallandrome')
        position = position + 1
        size = size - 1

if (flag == 0):
    print('pallendrome')
else:
    print('not a pallendrome')

print(pList)
# print(size)
# print(counter)
