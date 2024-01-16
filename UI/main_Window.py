import PySimpleGUI as sg
import math
import sympy as sp
from calc_Engine import *


pr=Precedence()
tk=Tokenization()
Pe=Postfix_Evaluation()


Unicode_Dic={
    'logx':"log\u2090x",
    'div':"\u00F7",
    'mul':"\u00D7"
}

layout = [
    [sg.Multiline(size=(50, 7), key="-Display-", no_scrollbar=True)],
    [sg.Button("7", size=(5, 2)), sg.Button("8", size=(5, 2)), sg.Button("9", size=(5, 2)),sg.Button("C", size=(5, 2)), sg.Button("AC", size=(5, 2))],
    [sg.Button("4", size=(5, 2)), sg.Button("5", size=(5, 2)), sg.Button("6", size=(5, 2)),sg.Button(Unicode_Dic["div"], size=(5, 2)), sg.Button(Unicode_Dic["mul"], size=(5, 2))],
    [sg.Button("1", size=(5, 2)), sg.Button("2", size=(5, 2)), sg.Button("3", size=(5, 2)),sg.Button("+", size=(5, 2)), sg.Button("-", size=(5, 2))],
    [sg.Button("0", size=(5, 2)), sg.Button(".", size=(5, 2)), sg.Button("=", size=(5, 2)),sg.Button("Ans", size=(5, 2)), sg.Button("Exp", size=(5, 2))]
]

expression=""
window = sg.Window("Scientific Calculator", layout, size=(310, 500), resizable=True, finalize=True)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    elif event.isdigit():
        expression +=event
        window["-Display-"].update(expression)
    elif event in pr.OPERATORS:
        expression+=event
        window["-Display-"].Update(expression)
    elif event =='=':
        print(expression)


    

window.close()
