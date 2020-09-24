from GUI_API import GUIApp

def test():
    def foo(x,operator,y):
        return eval(x+operator+y)
    app = GUIApp(foo,
                 output_type='messagebox', title="Basic Calculator")
    app.setInnerTitle('Calculator')
    app.setField('x', 'entry',{'label':'Variable X'})
    app.setField('y', 'entry',{'label':'Variable Y'})
    app.setInnerTitle('operator operator operatoroperator'
                 '')
    app.setField('operator', 'combobox', {'values': ['+', '-', '*', '/', '**']})
    app.run()


test()