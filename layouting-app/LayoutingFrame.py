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
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,40 ), wx.NO_FULL_REPAINT_ON_RESIZE )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer11.SetMinSize( wx.Size( 500,40 ) )
		self.m_staticText3 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"182410102024", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText31 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Menu", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )


		bSizer11.Add( ( 3, 0), 0, 0, 5 )

		self.m_staticText311 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Window", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText311.Wrap( -1 )

		self.m_staticText311.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.m_staticText311, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )


		bSizer11.Add( ( 3, 0), 0, 0, 5 )

		self.m_staticText3111 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Options", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText3111.Wrap( -1 )

		self.m_staticText3111.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer11.Add( self.m_staticText3111, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )


		self.m_panel4.SetSizer( bSizer11 )
		self.m_panel4.Layout()
		bSizer7.Add( self.m_panel4, 1, 0, 30 )


		bSizer5.Add( bSizer7, 0, wx.FIXED_MINSIZE, 5 )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )


		bSizer13.Add( ( 0, 50), 0, 0, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"My First App with Layout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		self.m_staticText20.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer13.Add( self.m_staticText20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer13.Add( ( 0, 10), 0, 0, 5 )

		self.btn_printName = wx.Button( self.m_panel5, wx.ID_ANY, u"Print My Name", wx.DefaultPosition, wx.Size( 120,20 ), 0 )
		self.btn_printName.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer13.Add( self.btn_printName, 0, wx.ALIGN_CENTER_HORIZONTAL, 0 )


		self.m_panel5.SetSizer( bSizer13 )
		self.m_panel5.Layout()
		bSizer13.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_printName.Bind( wx.EVT_BUTTON, self.btn_printNameOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_printNameOnButtonClick( self, event ):
		event.Skip()


