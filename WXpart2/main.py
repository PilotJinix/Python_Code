import wx
import noname

class Start(noname.MyFrame1):
    def __init__(self, parent):
        noname.MyFrame1.__init__(self, parent)
        self.baris = 0

    def set_cell(self, data):
        self.m_grid1.AppendRows()
        for i in range (len(data)):
            self.m_grid1.SetCellValue(self.baris, i, data[i])
        self.baris += 1


    def m_button_add( self, event ):
        datauser = []
        datauser.append(str(self.input_ID.GetValue()))
        datauser.append(str(self.input_first_name.GetValue()))
        datauser.append(str(self.input_last_name.GetValue()))
        datauser.append(self.input_age.GetValue())
        try:
            temp = 0
            for i in range(len(datauser)):
                if datauser[i] == "":
                    print("Salah")
                    raise Exception

                elif not (datauser[3].isnumeric()):
                    print("data tidak numerik")
                    raise Exception
                else:
                    temp +=1

            if temp == 4:
                self.set_cell(datauser)
            else:
                print("Data salah")

        except Exception:
            wx.MessageBox("Data Salah Gez", "Informasi", wx.OK | wx.ICON_ERROR)

data = wx.App()
frame = Start(None)
frame.Show()
data.MainLoop()



