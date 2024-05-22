import PySimpleGUI as sg  
import subprocess
import os

def run_script(script_name):
    subprocess.run([os.sys.executable, script_name])

def create_window(theme):
    sg.theme(theme) 
    sg.set_options(font='Arial 25', button_element_size=(2, 2))

    layout = [
        [sg.Text(
            '!-MENY-!',
            font='Arial 25', 
            justification='center', 
            expand_x=True, 
            pad=(4, 2),
            right_click_menu=['Menu', ['SandyBeach1']]
        )],
        [sg.Button('Guide', expand_x=True)], 
        [sg.Button('Bubble Sort', expand_x=True)], 
        [sg.Button('Insertion Sort', expand_x=True)], 
        [sg.Button('Quick Sort', expand_x=True)]
    ]

    return sg.Window('Meny', layout)

window = create_window('SandyBeach1')

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Guide':
        window.close()
        run_script('guide.py')

    elif event == 'Bubble Sort':
        window.close()
        run_script('bubble-sort.py')

    elif event == 'Insertion Sort':
        window.close()
        run_script('insertion-sort.py')

    elif event == 'Quick Sort':
        window.close()
        run_script('quick-sort.py')

window.close()
