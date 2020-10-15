# Basic-GUI-API

### Description:
Allows turning a command-line-script to basic form-like-GUI with a few lines of code.
Includes in-code documentation [e.g. `help(FormGUI)`].

### Example:

#### Code:
```python
from GUI_API import FormGUI

# Initiates a GUI App instance with 'action_func' (the lambda function) and output in pop-up-message 
app = FormGUI(lambda x,operator,y : eval(x+operator+y), output_type='messagebox', title="Basic Calculator")

# Sets the fields, i.e. the arguments of 'action_func'
app.setField('x', 'entry', label = 'Variable X')
app.setField('operator', 'combobox',values = ['+','-','*','/','**'])
app.setField('y', 'entry', label = 'Variable Y')

# Opens the GUI App
app.run()
```

#### Result:
<img src="https://github.com/matanbt/Basic-GUI-API/blob/master/img/demo.png" width=300>

