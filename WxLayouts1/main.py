import wx
import helloWxGui


class Splashscreen (helloWxGui.MyFrame1):
    def __init__(self, parent):
        helloWxGui.MyFrame1.__init__(self, parent)

    def agung_btn( self, event ):
        print("agung")

    def firman_btn( self, event ):
        print("firman")

    def abiyu_btn( self, event ):
        print("abiyu")


app = wx.App()
frame = Splashscreen(parent=None)
frame.Show()
app.MainLoop()

