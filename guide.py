import PySimpleGUI as sg  
import subprocess
import os
# Funktion för att köra andra Python-skript
def run_script(script_name):
    subprocess.run([os.sys.executable, script_name])

# Skapa Guide-fönstret
def create_window(theme):
    sg.theme(theme) 
    sg.set_options(font='Arial 16', button_element_size=(2, 2))

    # Text för guide
    guide_text = '''
    !-GUIDE-!
    
    Välkommen till DataSorteraren! Så här använder du den och en kort förklaring av de olika sorteringsmetoderna.
    '''
    # Instruktioner för användning
    instructions_text = '''
    1. Välj en sorteringsmetod från menyn:
        - Bubble Sort
        - Insertion Sort
        - Quick Sort

    2. Följ instruktionerna på skärmen för att sortera din data.
    '''
    # Beskrivning av sorteringsmetoder
    sorting_methods_text = '''
    Sorteringsmetoder:
    
    - Bubble Sort:
      Jämför och byt plats på två intilliggande element om de är i fel ordning. Upprepa tills listan är sorterad.

    - Insertion Sort:
      Ta ett element i taget och placera det på rätt plats i den sorterade delen av listan.

    - Quick Sort:
      Välj ett pivot-element och dela upp listan i två delar: en med element mindre än pivot och en med element större. Sortera sedan delarna.
    '''
    # Layouten för Guide-fönstret
    layout = [
        [sg.Text(guide_text, font='Arial 20', justification='center', expand_x=True, pad=(4, 2))],
        [sg.Text(instructions_text, font='Arial 16', justification='left', expand_x=True, pad=(4, 2))],
        [sg.Text(sorting_methods_text, font='Arial 16', justification='left', expand_x=True, pad=(4, 2))],
        [sg.Button('Meny', expand_x=True)]
    ]

    return sg.Window('Guide', layout)

window = create_window('SandyBeach1')

# Huvudloop för att läsa händelser i fönstret
while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED: # Stäng fönstret
        break
    # Hantera Meny-knappen
    if event == 'Meny':
        window.close()
        run_script('meny.py')

window.close()
