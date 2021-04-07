import wx
import praktikum_1

class Start(praktikum_1.MyFrame1):
    def __init__(self, parent):
        praktikum_1.MyFrame1.__init__(self, parent)

    def login_btn( self, event ):
        username = self.user_text.GetValue().replace(" ","")
        password = self.password_text.GetValue().replace(" ", "")

        if username == "" or password == "":
            self.error.SetLabel(str("Data Salah"))
            wx.MessageBox("Data Salah Gez", "Informasi", wx.OK | wx.ICON_ERROR)

        elif username == "Agung" and password == "12345":
            wx.MessageBox("Berhasilll !:)", "Informasi", wx.OK | wx.ICON_ASTERISK)
            print("Username = {}\nPassword = {}".format(self.user_text.GetValue(), self.password_text.GetValue()))
        else:
            print("Else")

    def tambah_btn( self, event ):
        print("Bertambah")
        try:
            data1 = self.bil1_text.GetValue()
            data2 = self.bil2_text.GetValue()
            result = int(data1) + int(data2)
            print(result)
            self.resultdata.SetLabel(str(result))
        except Exception:
            self.resultdata.SetLabel("Input harus bilangan bulat")


    def kali_btn( self, event ):
        print("Berkali")
        data1 = self.bil1_text.GetValue()
        data2 = self.bil2_text.GetValue()
        result = float(data1) * float(data2)
        print(result)
        self.resultdata.SetLabel(str(result))



data = wx.App()
frame = Start(None)
frame.Show()
data.MainLoop()