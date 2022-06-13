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


valor_str = input('Digite a data(DD/MM/AAAA): ')
valor = dt.strptime(valor_str, '%d/%m/%Y').date()
calculaSenha(valor)
