import PySimpleGUI as sg

def create_layout():
    layout = [
        [sg.Text('Wpisz nazwę miasta:'), sg.InputText(key='CITY')],
        [sg.Button('Pokaż pogodę'), sg.Button('Wyjdź')],
        [sg.Text(size=(40, 2), key='WEATHER_INFO')]
    ]
    return layout