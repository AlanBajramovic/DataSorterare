import PySimpleGUI as sg #Importering av PySimpleGUI och sg blev använt som förkortning 
import subprocess
import os

def main():
    subprocess.run([os.sys.excutable, 'quick-sort.py'])

def create_window(theme):
    sg.theme(theme) #Ange tema 
    sg.set_options(font = 'Arial 25', button_element_size = (2,2))
    button_size = (2,2) # Storlek på knappar 
 
    layout = [
        [sg.Text(
            '!-DATA SORT-!', #Text som visas i fönstret 
            font = 'Arial 25', 
            justification= 'center', 
            expand_x = True, 
            pad = (2,2),
            key = '-TEXT-') #Exempel på nyckel som används för att identifera texen 
        ],
        [
        sg.Button('GUIDE', expand_x = True), 
        sg.Button('MERGE SORT ', expand_x = True), 
        sg.Button('BUBBLE SORT', expand_x = True), 
        sg.Button('INSERTION SORT', expand_x = True), 
        sg.Button('QUICK SORT', expand_x = True)
        ],
    ]
    
    return sg.Window('data-sort.py', layout)
#Temamenyn 
theme_menu = ['Menu', ['Blue']]
window = create_window('DarkBlue')
#Skapa en fönster med tema dark

current_num = []
full_operation = []

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event == ('GUIDE'):
        print('GUIDE')

    if event == ('MERGE SORT'):
        print('MERGE SORT')

    if event == ('BUBBLE SORT'):
        print('BUBBLE SORT')
        
    if event == ('INSERTION SORT'):
        print('INSERTION SORT')
    
    if event == ('QUICK SORT'):
        print('QUICK SORT')
        
window.close() #Stänger ner fönstret (miniräknaren) när loopen är klar