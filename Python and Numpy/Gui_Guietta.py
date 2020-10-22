import guietta import _,Gui, Quit

gui = Gui(

    [   'Enter numbers:' , '__a__' , '+' , '__b__', ['Calculate']],
    [   'Result:  --> ','result' ,  _  ,    _                 ],
    [   __a__          ,    _    ,  _   ,    _ ,    Quit        ]

)

with gui.Calculate:
    gui.result=float(gui.a)+ float(gui.b)

gui.run