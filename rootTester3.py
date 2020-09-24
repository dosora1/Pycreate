import math

#제곱수 리스트
sqrLst=[]
for j in range(2,32):
    sqrLst.append(j**2)
sqrLst.reverse()

#소수 리스트
primeLst=[]
for i in range(2,100):
    res=0
    for j in range(1,i+1):
        if i%j==0: 
            res+=1
    if res==2: 
        primeLst.append(i)

#루트를 계산
def root(n):
    sym = '√(' ;close=')'
    frnt=1
    # 0이나 1이라면
    if n==1 or n==0:
        return n
    elif n in sqrLst: #제곱수라면
        sym='';close=''
        n=int(math.sqrt(n))
    else:
        for j in sqrLst:
            if n%j==0:
                    frnt=int(math.sqrt(j))
                    n//=j

    if frnt==1:frnt=''
    return str(frnt)+sym+str(n)+close

for i in range(1000):
    print(root(i))