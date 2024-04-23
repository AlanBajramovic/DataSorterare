import PySimpleGUI as sg
import subprocess
import os

def main():
    subprocess.run([os.sys.excutable, 'data-sort.py'])

def create_window(theme):
    sg.theme(theme) #Ange tema 
    sg.set_options(font = 'Arial 25', button_element_size = (2,2))
    button_size = (2,2) # Storlek på knappar 
 
    layout = [
        [sg.Text(
            '!-QUICK SORT-!', #Text som visas i fönstret 
            font = 'Arial 25', 
            justification= 'center', 
            expand_x = True, 
            pad = (2,2),
            key = '-TEXT-') 
        ],
        [ 
        sg.Button('QUICK SORT', expand_x = True)
        ],
    ]
    return sg.Window('quick-sort.py', layout)
 
theme_menu = ['Menu', ['Blue']]
window = create_window('DarkBlue')




window.close()