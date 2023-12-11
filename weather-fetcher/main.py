import PySimpleGUI as sg
from layout import create_layout
from function import get_weather_info

def main():
    sg.theme('LightBlue')
    # sg.theme('DarkTeal9')
    


    layout = create_layout()
    window = sg.Window('Aplikacja Pogodowa', layout)

    while True:
        event, values = window.read()
        if event in (None, 'Wyjdź'):
            break
        if event == 'Pokaż pogodę':
            weather_info = get_weather_info(values['CITY'])
            window['WEATHER_INFO'].update(weather_info)

    window.close()

if __name__ == "__main__":
    main()