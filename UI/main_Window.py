import PySimpleGUI as sg

#from calc_Engine.ExpressionChecker import *
#from calc_Engine.Postfix_Evaluation import Post_Evaluation

#PE=Post_Evaluation()

layout = [
    [sg.InputText(size=(50,4),key="-Display-")],
    [sg.Button("7"),sg.Button("8"),sg.Button("9"),sg.Button(u'\u00F7')],
    [sg.Button("4"),sg.Button("5"),sg.Button("6"),sg.Button("x")],
    [sg.Button("1"),sg.Button("2"),sg.Button("3"),sg.Button("+")],
    [sg.Button("0"),sg.Button("00"),sg.Button("-"),sg.Button("=")],
    [sg.Button("C"),sg.Button("Sqrt"),sg.Button("Sin"),sg.Button("Cos"),sg.Button("Tan")],
]

window = sg.Window("Scientific Calculator", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event in "0123456789.+-x u'\u00F7'":
        window["-Display-"].update(values["-Display-"]+event)
    elif event=="=":
        try:                
            result=eval(values["-Display-"])
            window["-Display-"].update(str(result))
        except:
            window["-Display-"].update("Error")
    elif event=="C":
        window["-Display-"].update("")
    
window.close()
