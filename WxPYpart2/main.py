import wx
import noname

class Start(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        self.baris = 0

    def m_button_add( self, event ):
        datauser = []
        datauser.append(str(self.input_ID.GetValue()))
        datauser.append(str(self.input_FS.GetValue()))
        datauser.append(str(self.input_LS.GetValue()))
        datauser.append(self.input_age.GetValue())
        try:
            temp = 0
            for i in range(len(datauser)):
                if datauser[i] == "":
                    print("Data Kosong")
                elif not datauser[3].isnumeric():
                    print("Data umur Salah")
                else:
                    temp += 1
                    print(temp)
            if temp == len(datauser):
                self.set_cell(datauser)
                wx.MessageBox('Data berhasil disimpan', 'Data disimpan !', wx.OK | wx.ICON_INFORMATION)
            else:
                raise Exception

        except Exception:
            print("error")
            wx.MessageBox('Data Salah', 'Warning !', wx.OK | wx.ICON_ERROR)

    def set_cell(self, data):
        self.tabel.AppendRows()
        for i in range(len(data)):
            self.tabel.SetCellValue(self.baris, i , data[i])
        self.baris += 1

data = wx.App()
frame = Start(None)
frame.Show()
data.MainLoop()
