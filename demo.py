# gitdemo
print('hello')
print('sanjay welcomes you')
#code for binary serch
def bubblesooort(list):
    for i in range(int(len(list))-1,0,-1):
        for j in range(i):
           if list[j]<list[j+1]:
               a=list[j]
               list[j]=list[j+1]
               list[j+1]=a


    print(list)



list=[78,55,6,4,88,7,9,33,2,144]

bubblesooort(list)
#end