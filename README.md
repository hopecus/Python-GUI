# Making GUI Application with Python
I would like to build GUI application using many powerful python packages.

## IronPython with .Net
* Python Tools for Visual Studio : https://github.com/Microsoft/PTVS

Python Tools allows you to create python projects using the Visual Studio IDE. 

* IronPython : http://ironpython.net/

After installing IronPython, the Visual Stuido IDE supports several new project templates including "IronPython WPF Application".
Windows Presentation Foundation(WPF) application uses XAML files to describe rich user interfaces and 
Visual Studio includes a drag and drop designer. Python applicaiton with IronPython can interact with .Net code.

1) Add the following code to your main python file.
~~~~{.python}

import clr
clr.AddReference('PresentationCore')
clr.AddReference("PresentationFramework")
clr.AddReference('Microsoft.Dynamic')
clr.AddReference('Microsoft.Scripting')
clr.AddReference('System')
clr.AddReference('IronPython')
clr.AddReference('IronPython.Modules')
clr.AddReference('IronPython.Wpf')

~~~~

2) Compile python code with IronPython to build stand-alone executable GUI Application

~~~~
ipy.exe pyc.py /out:_application_name_ /main:_main_python_file_name.py_ /target:winexe /standalone
~~~~

> You can ipy.exe in IronPython installation path(ex. C:\Program Files\IronPython 2.7\ in Windows) and pyc.py at [IronPython Path]\Tools\Scripts


## Pyside (QT GUI)

