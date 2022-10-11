import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
file_list_column = [
    [sg.Text("Importe os dados e a pasta de destino", font="Poppins 20")],
    [
        sg.Text("Caminho do json ", size=(15, 1), font="Poppins 16"),
        sg.InputText(key="-FILES-"),
        sg.FileBrowse(button_text="Selecionar"),
    ],
    [
        sg.Text("Pasta de destino ", size=(15, 1), font="Poppins 16"),
        sg.InputText(key="-FOLDER-"),
        sg.FolderBrowse(button_text="Selecionar"),
    ],
    [sg.Submit(button_text="Executar" ,size=(50, 1)), sg.Cancel(button_text="Cancelar")],
    [sg.Text("", key="-ERROR-")],
    
]

# Create the Window
window = sg.Window('Window Title', file_list_column)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()