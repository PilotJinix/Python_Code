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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer7.SetMinSize( wx.Size( 1,1 ) )

		bSizer7.Add( ( 0, 100), 0, wx.EXPAND|wx.SHAPED, 5 )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer11.SetMinSize( wx.Size( 200,50 ) )
		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Current Counter : ", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.Wrap( -1 )

		bSizer13.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

		self.txt_counter_value = wx.StaticText( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txt_counter_value.Wrap( -1 )

		bSizer13.Add( self.txt_counter_value, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer13, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND|wx.SHAPED, 5 )


		bSizer11.Add( ( 0, 20), 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_decrease = wx.Button( self, wx.ID_ANY, u"+ Decrease", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_decrease, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer8.Add( ( 10, 0), 1, wx.EXPAND, 5 )

		self.btn_increase = wx.Button( self, wx.ID_ANY, u"+ Increase", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_increase, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( bSizer8, 0, wx.ALIGN_CENTER, 0 )


		bSizer7.Add( bSizer11, 0, wx.ALIGN_CENTER|wx.SHAPED, 0 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_decrease.Bind( wx.EVT_BUTTON, self.btn_decreaseOnButtonClick )
		self.btn_increase.Bind( wx.EVT_BUTTON, self.btn_increaseOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_decreaseOnButtonClick( self, event ):
		event.Skip()

	def btn_increaseOnButtonClick( self, event ):
		event.Skip()


