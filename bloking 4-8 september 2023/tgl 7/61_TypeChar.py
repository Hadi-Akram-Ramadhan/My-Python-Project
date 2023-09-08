import PySimpleGUI as sg

sg.theme("BluePurple")

layout = [
    [sg.Text("Your Typed Char appear here"), sg.Text(size=(15, 1), key="-OUTPUT-")],
    [sg.Input(key="-IN-")],
    [sg.Button("Show"), sg.Button("EXIT")],
]

window = sg.Window("Pattern 2B", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Show":
        window["-OUTPUT-"].update(values["-IN-"])


window.close()
