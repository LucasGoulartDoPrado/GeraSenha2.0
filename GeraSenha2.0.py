from datetime import datetime as dt


def calculaSenha(data):
    if data.day % 2 == 0:
        digito = str(8)
    else:
        digito = str(9)

    if data.day > 30:
        data_2 = data.replace(day=1, month=(data.month-1))
    else:
        data_2 = data.replace(day=(data.day+1), month=(data.month-1))

    dia_str = data_2.strftime("%d")[::-1]
    mes = data_2.strftime("%m")
    senha = dia_str + mes + digito
    print(senha)


def validaData(data):
    format = "%d/%m/%Y"
    valida = True
    try:
        valida = bool(dt.strptime(data, format))
    except ValueError:
        valida = False
    return (valida)


valor_str = input('Digite a data(DD/MM/AAAA): ')
if validaData(valor_str) == True:
    valor = dt.strptime(valor_str, '%d/%m/%Y').date()
    calculaSenha(valor)
else:
    print('Data digitada é invalida!')
