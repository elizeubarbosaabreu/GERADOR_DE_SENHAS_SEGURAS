import PySimpleGUI as sg
import string, clipboard, webbrowser
from random import choice, randint

# 
#  ____  _                           ____                                     _ 
# / ___|| |_ _ __ ___  _ __   __ _  |  _ \ __ _ ___ _____      _____  _ __ __| |
# \___ \| __| '__/ _ \| '_ \ / _` | | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
#  ___) | |_| | | (_) | | | | (_| | |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
# |____/ \__|_|  \___/|_| |_|\__, | |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
#                            |___/                                              
#   ____                           _             
#  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
# | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
# | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
#  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
#                                                
caracteres_especiais = ['!', '#', '$', '%', '&', '*', ',', '.', ':', ';', '/', '?', '_', '-', '<', '>']
letras_minusculas = list(string.ascii_lowercase)
letras_maiusculas = list(string.ascii_uppercase)
letras = []
senha = ''
url = 'https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/'

def sortear_numero():
    return randint(0, 10)    

def sortear_minuscula(letras_minusculas):
    return choice(letras_minusculas)

def sortear_maiuscula(letras_maiusculas):
    return choice(letras_maiusculas)

def sortear_caracter(caracteres_especiais):
    return choice(caracteres_especiais)

def embaralhar(lista_de_funcoes):
    return choice(lista_de_funcoes)

sg.theme('Topanga')

layout = [[sg.Stretch(), sg.Text('GERADOR DE SENHAS', font=('Arial', 18)), sg.Stretch()],
          [sg.Stretch(),
           sg.Text('Tamanho da Senha:', font=('Arial', 12)),
           sg.Combo(['8', '9', '10', '11', '12', '13', '14', '15', '20', '25', '100'],
                    key='-tam_senha-', default_value='2')],
          [sg.HorizontalSeparator()],
          [sg.VerticalSeparator(),
           sg.T('Sua Senha Vai Aparecer Aqui',
                font=('Courier', 18), size=(30, 1), key='-output-'),
           sg.VerticalSeparator()],
          [sg.HorizontalSeparator()],
          [sg.VerticalSeparator(),
           sg.Button('Gerar Senha', size=(14, 1)),
           sg.VerticalSeparator(),
           sg.Button('Copiar Senha', size=(14, 1)),
           sg.VerticalSeparator(),
           sg.Button('?', size=(14, 1)),
           sg.VerticalSeparator()],
           [sg.HorizontalSeparator()]
          ]

window = sg.Window('GERADOR DE SENHAS SEGURAS', layout)

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    elif event == '?':
        sg.Popup('Autor', '''
Este Software foi desenvolvido por Elizeu Barbosa Abreu.
Carteiro, Licenciado em Ci\u00eancias Biol\u00f3gicas e que tem como hobby programar em Python...
''')
        webbrowser.open(f'{url}')
        
    
    elif event == 'Gerar Senha':
        
        senha = ''
        window['-output-'].Update('')
        
        tamanho_da_senha = values['-tam_senha-']        
        
        if tamanho_da_senha == '':
            
            sg.Popup('CAMPO OBRIGAT\u00d3RIO VAZIO!!!',
                     '''O campo de tamanho de senha n\u00e3o pode estar vazio''')
            tamanho_da_senha == '0'
            
            continue
            
        tamanho = int(tamanho_da_senha)
        
        if tamanho == 0 or tamanho < 8:
            sg.Popup('TAMANHO DE SENHA INV\u00c1LIDA!!!',
                          '''A sua senha deve ter mais de 8 caracteres para ter o m\u00ednimo de seguran\u00e7a. Volte \u00e0 tela inicial e altere o valor no campo tamanho da senha...''')
        
        for letra in range(int(tamanho_da_senha)):
            
            lista_de_funcoes = (
                sortear_numero(),
                sortear_minuscula(letras_minusculas),
                sortear_maiuscula(letras_maiusculas),
                sortear_caracter(caracteres_especiais)
                )
            
            letras = embaralhar(lista_de_funcoes)
            
            senha += str(letras)           
        window['-output-'].Update(f'{senha}')  
        
    
    if event == 'Copiar Senha':
        
        clipboard.copy(senha)        
        senha = ''
        
window.close()
