import PySimpleGUI as sg  
import subprocess
import os

def run_script(script_name):
    subprocess.run([os.sys.executable, script_name])

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

def create_window(theme):
    sg.theme(theme) 
    sg.set_options(font='Arial 25', button_element_size=(2, 2))

    layout = [
        [sg.Text(
            '!-INSERTION SORT-!',
            font='Arial 25', 
            justification='center', 
            expand_x=True, 
            pad=(4, 2),
            right_click_menu=['Menu', ['SandyBeach1']]
        )],
        [sg.Text('Ange nummer, vilket du vill sortera:', font='Arial 16')],
        [sg.InputText(key='input_numbers', font='Arial 16')],
        [sg.Button('Sortera', expand_x=True, font='Arial 16')],
        [sg.Text('Resultat:', font='Arial 16')],
        [sg.Multiline('', size=(40, 5), key='output', font='Arial 16')],
        [sg.Button('Meny', expand_x=True, font='Arial 16')],
        [sg.Button('Guide', expand_x=True, font='Arial 16')],
    ]

    return sg.Window('Insertion Sort', layout)

window = create_window('SandyBeach1')

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Meny':
        window.close()
        run_script('meny.py')
    
    if event == 'Guide':
        window.close()
        run_script('guide.py')
    
    if event == 'Sortera':
        input_numbers = values['input_numbers']
        try:
            numbers = list(map(int, input_numbers.split(',')))
            sorted_numbers = insertion_sort(numbers)
            window['output'].update(', '.join(map(str, sorted_numbers)))
        except ValueError:
            window['output'].update('Felaktig inmatning, ange endast nummer separerade med kommatecken.')

window.close()
