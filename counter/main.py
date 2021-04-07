import wx
import datacounter


class subClass(datacounter.MyFrame2):
    def __init__(self, parent):
        datacounter.MyFrame2.__init__(self, parent)
        self.counter = int(self.txt_counter_value.GetLabelText())

    def btn_increaseOnButtonClick(self, event):
        self.counter = self.counter + 1
        self.txt_counter_value.SetLabelText(str(self.counter))

    def btn_decreaseOnButtonClick(self, event):
        self.counter = self.counter - 1
        self.txt_counter_value.SetLabelText(str(self.counter))


app = wx.App()
frame = subClass(parent=None)
frame.Show()
app.MainLoop()