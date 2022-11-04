import copy
from itertools import groupby
from functools import reduce
alunos=[
    {'nome':'Hilster','notas':[10,10]},
    {'nome':'Carlos','notas':[6,8]},
    {'nome':'Talia','notas':[8,9]},
    {'nome':'Bruno','notas':[7,6]},
    {'nome':'Gabrieli','notas':[8,6]},
    {'nome':'Paloma','notas':[5,9]},
    {'nome':'Ketlin','notas':[7,10]},
    {'nome':'Jader','notas':[7,7]},
    {'nome':'Arthur','notas':[6,6]},
    {'nome':'Raitam','notas':[8,5]},
]
fil0=lambda a:a['notas'][0]
fil1=lambda a:a['notas'][1]

alunos.sort(key=fil0)
al1=copy.deepcopy(alunos)
al1=groupby(al1,fil0)

alunos.sort(key=fil1)
al2=copy.deepcopy(alunos)
al2=groupby(al2,fil1)

for i,j in al1:
    print(f"Nota 1 ={i}")
    for a in j:
        print(f"\t{a}")
print("_"*50)
for i,j in al2:
    print(f"Nota 2 ={i}")
    for a in j:
        print(f"\t{a}")
print()
print(f"Soma de todas as notas 1:{reduce(lambda sm, i: i['notas'][0]+ sm, alunos,0)}")
print(f"Soma de todas as notas 1:{reduce(lambda sm, i: i['notas'][1]+ sm, alunos,0)}")
