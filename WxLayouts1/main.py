import wx
import helloWxGui

app = wx.App()
frame = helloWxGui.MyFrame1(parent=None)
frame.Show()
app.MainLoop()