from GUI_API import GUIApp


def test():
    def foo(x, operator, y):
        return eval(x + operator + y)

    # Initiates a GUI App instance with 'action_func' (the lambda function) and output in pop-up-message
    app = GUIApp(foo, output_type='messagebox', title="Basic Calculator")
    app.setInnerTitle('Calculator')

    # Sets the fields, i.e. the arguments of 'action_func'
    app.setField('x', 'entry', label='Variable X')
    app.setField('operator', 'combobox', values=['+', '-', '*', '/', '**'])
    app.setField('y', 'entry', label='Variable Y')

    # opens the GUI App
    app.run()


test()
