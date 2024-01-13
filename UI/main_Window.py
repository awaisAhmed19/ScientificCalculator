import PySimpleGUI as sg

#from calc_Engine.ExpressionChecker import *
#from calc_Engine.Postfix_Evaluation import Post_Evaluation

#PE=Post_Evaluation()

layout = [
    [sg.Multiline(size=(50,7),key="-Display-",no_scrollbar=True)],
    [sg.Button("log\u2090x",size=(5,2)),sg.Button("x\u00B2",size=(5,2)),sg.Button("a/b",size=(5,2)),sg.Button('\u221A',size=(5,2)),sg.Button("x\u00B2",size=(5,2))],
    [sg.Button("x\u207F",size=(5,2)),sg.Button("log",size=(5,2)),sg.Button("ln",size=(5,2)),sg.Button("hyp",size=(5,2)),sg.Button("x\u00B3",size=(5,2))],
    [sg.Button("Sin",size=(5,2)),sg.Button("Tan",size=(5,2)),sg.Button("Cos",size=(5,2)),sg.Button("e\u207F",size=(5,2)),sg.Button("x\u221Ax",size=(5,2))],
    [sg.Button("7",size=(5,2)),sg.Button("8",size=(5,2)),sg.Button("9",size=(5,2)),sg.Button("C",size=(5,2)),sg.Button("AC",size=(5,2))],
    [sg.Button("4",size=(5,2)),sg.Button("5",size=(5,2)),sg.Button("6",size=(5,2)),sg.Button(u'\u00F7',size=(5,2)),sg.Button("\u00D7",size=(5,2))],
    [sg.Button("2",size=(5,2)),sg.Button("2",size=(5,2)),sg.Button("3",size=(5,2)),sg.Button("+",size=(5,2)),sg.Button("-",size=(5,2))],
    [sg.Button("0",size=(5,2)),sg.Button(".",size=(5,2)),sg.Button("=",size=(5,2)),sg.Button("Ans",size=(5,2)),sg.Button("Exp",size=(5,2))]
    
]

window = sg.Window("Scientific Calculator", layout,size=(310,500),resizable=True,finalize=True)

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
