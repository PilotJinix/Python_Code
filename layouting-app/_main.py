import wx
import LayoutingFrame

class subClass(LayoutingFrame.MainFrame):
    def __init__(self, parent):
        LayoutingFrame.MainFrame.__init__(self, parent)
    def btn_printNameOnButtonClick( self, event ):
        print("My Name is : Rahmad Firmansyah")

app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()
