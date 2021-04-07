///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame2::MyFrame2( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizer7;
	bSizer7 = new wxBoxSizer( wxVERTICAL );

	bSizer7->SetMinSize( wxSize( 1,1 ) );

	bSizer7->Add( 0, 100, 0, wxEXPAND|wxSHAPED, 5 );

	wxBoxSizer* bSizer11;
	bSizer11 = new wxBoxSizer( wxVERTICAL );

	bSizer11->SetMinSize( wxSize( 200,50 ) );
	wxBoxSizer* bSizer13;
	bSizer13 = new wxBoxSizer( wxHORIZONTAL );

	wxStaticText* m_staticText4;
	m_staticText4 = new wxStaticText( this, wxID_ANY, wxT("Current Counter : "), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText4->Wrap( -1 );
	bSizer13->Add( m_staticText4, 0, wxALIGN_CENTER_VERTICAL, 5 );

	txt_counter_value = new wxStaticText( this, wxID_ANY, wxT("0"), wxDefaultPosition, wxDefaultSize, 0 );
	txt_counter_value->Wrap( -1 );
	bSizer13->Add( txt_counter_value, 0, wxALL, 5 );


	bSizer11->Add( bSizer13, 1, wxALIGN_CENTER_HORIZONTAL|wxEXPAND|wxSHAPED, 5 );


	bSizer11->Add( 0, 20, 1, wxEXPAND, 5 );

	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxHORIZONTAL );

	btn_decrease = new wxButton( this, wxID_ANY, wxT("+ Decrease"), wxPoint( -1,-1 ), wxDefaultSize, 0 );
	bSizer8->Add( btn_decrease, 0, wxALIGN_CENTER_VERTICAL, 5 );


	bSizer8->Add( 10, 0, 1, wxEXPAND, 5 );

	btn_increase = new wxButton( this, wxID_ANY, wxT("+ Increase"), wxDefaultPosition, wxDefaultSize, 0 );
	bSizer8->Add( btn_increase, 0, wxALIGN_CENTER_VERTICAL, 5 );


	bSizer11->Add( bSizer8, 0, wxALIGN_CENTER, 0 );


	bSizer7->Add( bSizer11, 0, wxALIGN_CENTER|wxSHAPED, 0 );


	this->SetSizer( bSizer7 );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	btn_decrease->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame2::btn_decreaseOnButtonClick ), NULL, this );
	btn_increase->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame2::btn_increaseOnButtonClick ), NULL, this );
}

MyFrame2::~MyFrame2()
{
	// Disconnect Events
	btn_decrease->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame2::btn_decreaseOnButtonClick ), NULL, this );
	btn_increase->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame2::btn_increaseOnButtonClick ), NULL, this );

}
