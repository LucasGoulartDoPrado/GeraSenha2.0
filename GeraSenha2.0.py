from calendar import month
from datetime import datetime as dt


def calculaSenha(data):
    if data.day % 2 == 0:
        digito = str(8)
    else:
        digito = str(9)
    data_2 = data.replace(day=(data.day+1), month=(data.month-1))
    dia_str = data_2.strftime("%d")[::-1]
    mes = data_2.strftime("%m")
    senha = dia_str + mes + digito
    print(senha)


#valor = input('Digite a data(DD/MM/AAAA): ')
valor = '31/05/2021'
dia = dt.strptime(valor, '%d').date.day
mes = dt.strptime(valor, '%m').date.month
print(type(dia.days))
# print(data.day)
# print(data.Month)
# calculaSenha(data)
