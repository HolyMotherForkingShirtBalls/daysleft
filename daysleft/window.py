import PySimpleGUI as sg
import backend as bak


sg.theme('BluePurple')

bak.dayCount()
   
layout = [[sg.Text("Days Remaining:",bak.RD, "Time Remaining:",RH,":",RM,":",RS),
           sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Display'), sg.Button('Exit')]]
  
window = sg.Window('Introduction', layout)
  
while True:
    event, values = window.read()
    print(event, values)
      
    if event in  (None, 'Exit'):
        break
      
    if event == 'Display':
        # Update the "output" text element
        # to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])
  
window.close()