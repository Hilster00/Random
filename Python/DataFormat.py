from datetime import datetime, timedelta
import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')
nova_data=input("Digite a data no formato d/m/a:")
data = datetime.strptime(nova_data,'%d/%m/%Y')
print(data)

print('Data (%d/%m/%Y): ',end="")
print(data.strftime('%d/%m/%Y'))

print('Data (%d/%m/%y): ',end="")
print(data.strftime('%d/%m/%y'))

print('Data (%d/%m/%-y): ',end="")
print(data.strftime('%d/%m/%-y'))

print('Data (%d/%-m/%Y): ',end="")
print(data.strftime('%d/%-m/%Y'))

print('Data (%d/%B/%Y): ',end="")
print(data.strftime('%d/%B/%Y'))

print('Data (%-d/%m/%Y): ',end="")
print(data.strftime('%-d/%B/%Y'))
    
print("Data (%A):",end="")
print(data.strftime("%A"))


print("Data atual")
data = datetime.now()
print(data)

print('Data (%d/%m/%Y): ',end="")
print(data.strftime('%d/%m/%Y'))

print('Data (%d/%m/%y): ',end="")
print(data.strftime('%d/%m/%y'))

print('Data (%d/%m/%-y): ',end="")
print(data.strftime('%d/%m/%-y'))

print('Data (%d/%-m/%Y): ',end="")
print(data.strftime('%d/%-m/%Y'))

print('Data (%d/%B/%Y): ',end="")
print(data.strftime('%d/%B/%Y'))

print('Data (%-d/%m/%Y): ',end="")
print(data.strftime('%-d/%B/%Y'))
    
print("Data (%A):",end="")
print(data.strftime("%A"))
print(f'Hoje é: {data.strftime("%A, %d de %B de %Y")}')
