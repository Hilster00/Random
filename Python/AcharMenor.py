import random
def AcharMenor(vetor,inicio=0,fim=None):
    if fim == None:
        fim=len(vetor)-1
    if fim==inicio:
        return vetor[inicio]
    m=(fim+inicio)//2
    mtd1=AcharMenor(vetor,inicio,m)
    mtd2=AcharMenor(vetor,m+1,fim)
    return mtd1 if mtd1 <= mtd2 else mtd2

vetor=[random.randint(0,100) for i in range (10)]
print(vetor)
print(AcharMenor(vetor))
