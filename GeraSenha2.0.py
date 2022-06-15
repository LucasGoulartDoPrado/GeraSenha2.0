from datetime import datetime as dt
from PySimpleGUI import PySimpleGUI as sg
import pyperclip as c

sg.theme('DarkBlue3')


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
    return(senha)


def validaData(data):
    format = "%d/%m/%Y"
    valida = True
    try:
        valida = bool(dt.strptime(data, format))
    except ValueError:
        valida = False
    return (valida)


layout = [
    [sg.Text('Digite a data: '), sg.Input(
        key='data', default_text=dt.strftime(dt.today(), '%d/%m/%Y'))],
    [sg.Button('Gerar Senha')],
    [sg.Output(key='senha', size=(50, 1))],
]

janela = sg.Window('Gera Senha', layout, size=(250, 150), icon='geraSenha.ico')

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Gerar Senha':
        data = janela['data'].get()
        print(type(data))
        if validaData(data) == True:
            data = dt.strptime(data, '%d/%m/%Y').date()
            janela['senha'].update(calculaSenha(data))
            c.copy(calculaSenha(data))
        else:
            sg.popup_ok('Data inválida!')
