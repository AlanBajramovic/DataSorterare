import PySimpleGUI as sg  
import subprocess
import os

def run_script(script_name):
    subprocess.run([os.sys.executable, script_name])

def create_window(theme):
    sg.theme(theme) 
    sg.set_options(font = 'Arial 25', button_element_size = (2,2)) 

 
    layout = [
        [sg.Text(
            '!-QUICK SORT-!',
            font = 'Arial 25', 
            justification= 'center', 
            expand_x = True, 
            pad = (2,2),
            right_click_menu = 
            ['Menu', ['Lightgrey1', 'SandyBeach', 'Tan', 'Random']])
        ],
        [sg.Button('Meny', expand_x = True), 
         sg.Button('Merge Sort ', expand_x = True), 
         sg.Button('Bubble Sort', expand_x = True), 
         sg.Button('Insertion Sort', expand_x = True), 
         sg.Button('Data Sort', expand_x = True)],
        ]
    
    return sg.Window('Guide', layout)


window = create_window('dark')

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == ('Data Sort'):
        run_script('data-sort.py')
        
window.close() 
