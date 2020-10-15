import time

from GUI_API import FormGUI,RunningScriptGUI


def example_form():
    def foo(x, operator, y):
        return eval(x + operator + y)

    # Initiates a GUI App instance with 'action_func' (the lambda function) and output in pop-up-message
    app = FormGUI(foo, output_type='messagebox', title="Basic Calculator",resizable=True)
    app.setItem('title','My Calculator :)')

    # Sets the fields, i.e. the arguments of 'action_func'
    app.setField('x', 'entry', label='Variable X')
    app.setField('operator', 'combobox', values=['+', '-', '*', '/', '**'])
    app.setField('y', 'entry', label='Variable Y')

    # Opens the GUI App
    app.run()

def example_running():
    def foo_script(gui):
        #script to be run
        for i in range(20):
            gui.print(f"line: #{i}")
            time.sleep(0.4)

    app = RunningScriptGUI(foo_script)
    app.run()

