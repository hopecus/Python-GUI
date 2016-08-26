import clr
clr.AddReference('PresentationCore')
clr.AddReference("PresentationFramework")
clr.AddReference('Microsoft.Dynamic')
clr.AddReference('Microsoft.Scripting')
clr.AddReference('System')
clr.AddReference('IronPython')
clr.AddReference('IronPython.Modules')
clr.AddReference('IronPython.Wpf')

import wpf

from System.Windows import Application, Window, MessageBox

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'HelloWorld.xaml')
    
    def Button_Click(self, sender, e):
        MessageBox.Show("Hello World", "Notice")
    

if __name__ == '__main__':
    Application().Run(MyWindow())
