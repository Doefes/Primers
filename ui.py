import wx


class primerUI(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        self.panel = wx.Panel(self)
        self.Center()
        self.button = wx.Button(self.panel, label="Save")
        self.pcrLabel = wx.StaticText(self.panel, label="PCR Size: ")
        self.pcrSizeField = wx.SpinCtrl(self.panel,
                                        -1,
                                        '300',
                                        min=200,
                                        max=500)
        self.sequenceLabel = wx.StaticText(self.panel, label="Sequence:")
        self.sequenceField = wx.TextCtrl(self.panel,
                                         size=(400, 100),
                                         style=wx.TE_MULTILINE)
        self.errorMessage = wx.StaticText(self.panel)
        self.errorMessage.SetForegroundColour(wx.RED)

        # Set sizer for the frame,so wes can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.pcrLabel, (0, 0))
        self.sizer.Add(self.pcrSizeField, (0, 1))
        self.sizer.Add(self.sequenceLabel, (1, 0))
        self.sizer.Add(self.sequenceField, (1, 1))
        self.sizer.Add(self.errorMessage, (2, 1), (1, 2), flag=wx.EXPAND)
        self.sizer.Add(self.button, (3, 1), (1, 2), flag=wx.EXPAND)

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)
        self.SetSizerAndFit(self.windowSizer)

        # Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, e):
        self.errorMessage.SetLabel("Error")


app = wx.App(False)
frame = primerUI(None)
frame.Show()
app.MainLoop()
