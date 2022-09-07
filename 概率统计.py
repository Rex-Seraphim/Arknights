import random
sum=0
ci=100000
#可以将结果归类到数列中，然后结合数据可视化
while ci>0:

    i=random.randint(1,50)
    print(i,end='\t')
    j=random.randint(1,50)
    print(j,end='\t')
    if i==j:
        sum+=1
    ci-=1

print()
print()
print()
print('-'*20)
print(sum)
print('-'*20)

