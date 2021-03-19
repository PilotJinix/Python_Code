import wx
import helloWxGui


class Splashscreen(helloWxGui.MyFrame1):
    def __init__(self, parent):
        helloWxGui.MyFrame1.__init__(self, parent)

    def login_btn(self, event):
        name = self.username_text.GetValue().replace(" ", "")
        password = self.password_text.GetValue().replace(" ", "")

        if name == "" or password == "":
            wx.MessageBox("Data tidak boleh kososng", "Error", wx.OK | wx.ICON_ASTERISK)

        elif name == "Agung" and password == "12345":
            print("Username = {}\nPassword = {}".format(name, password))

        else:
            wx.MessageBox("Data salah", "Error", wx.OK | wx.ICON_WARNING)

    def lupapassword(self, event):
        print("Lupa Password")

class Calculate(helloWxGui.MyFrame3):
    def __init__(self, parent):
        helloWxGui.MyFrame3.__init__(self, parent)

    def tambah_btn( self, event ):
        try:
            data1 = self.bil1_text.GetValue()
            data2 = self.bil2_text.GetValue()
            result = int(data1) + int(data2)
            print(result)
            self.resultdata = result
        except Exception:
            print("Error")






app = wx.App()
# frame = Splashscreen(None)
frame = Calculate(None)
frame.Show()
app.MainLoop()
