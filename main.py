array=list(map(int,input().split()))
max=array[0]
count=0
for l in range(1,len(array)):
    if(array[l]>max):
        max=array[l]
for l in range(len(array)):
    if(array[l]==max):
        count+=1
print(count)

