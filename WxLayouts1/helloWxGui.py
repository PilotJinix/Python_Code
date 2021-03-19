# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Page", pos = wx.DefaultPosition, size = wx.Size( 495,432 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.username_text = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.username_text, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.password_text = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.password_text, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"Lupa Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button3, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( fgSizer2 )
		self.m_panel2.Layout()
		fgSizer2.Fit( self.m_panel2 )
		bSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 10 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.login_btn )
		self.m_button3.Bind( wx.EVT_BUTTON, self.lupapassword )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def login_btn( self, event ):
		event.Skip()

	def lupapassword( self, event ):
		event.Skip()


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Bilangan Pertama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.bil1_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.bil1_text, 0, wx.ALL, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Bilangan Kedua", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.bil2_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.bil2_text, 0, wx.ALL, 5 )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.m_button4, 0, wx.ALL, 5 )


		bSizer3.Add( fgSizer2, 1, 0, 60 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText9 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Hasil =", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer7.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.resultdata = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.resultdata, 0, wx.ALL, 0 )


		bSizer6.Add( bSizer7, 1, wx.ALL, 50 )


		bSizer6.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer6 )
		self.m_panel2.Layout()
		bSizer6.Fit( self.m_panel2 )
		bSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button4.Bind( wx.EVT_BUTTON, self.tambah_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambah_btn( self, event ):
		event.Skip()


