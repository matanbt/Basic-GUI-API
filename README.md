# Basic-GUI-API

### Description
Add basic GUI to a command-line-script with a few lines of code.


### Example:
#### Result:
<img src="">

#### Code:
```
from GUI_API import GUIApp

# Initiates a GUI App instance with 'action_func' (the lambda function) and output in pop-up-message 
app = GUIApp(lambda x,operator,y : eval(x+operator+y),
             output_type='messagebox', title="Basic Calculator")

# Sets the fields, i.e. the arguments of 'action_func'
app.setField('x', 'entry',{'label':'Variable X'})
app.setField('operator', 'combobox',{'values':['+','-','*','/','**']})
app.setField('y', 'entry',{'label':'Variable Y'})

#opens the GUI App
app.run()
```
