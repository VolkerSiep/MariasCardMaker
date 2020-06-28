#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:51:39 2020

@author: volker
"""
# stdlib modules
from os import getcwd
from time import time
from pathlib import Path

# external modules
import wx

# internal modules
from .generator import Generator


class CardMaker(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title="Maria's Card maker")
        sizer1 = wx.BoxSizer(wx.VERTICAL)
        sizer1.Add(wx.StaticText(self, wx.ID_ANY, "Excel file:"), 0,
                   wx.ALIGN_CENTER_VERTICAL|wx.ALL, 3)
        self.__file_name_ctrl = wx.TextCtrl(self, -1, size=(500, -1))
        sizer1.Add(self.__file_name_ctrl, 0,
                   wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 3)
        self.__new_cards = wx.CheckBox(self, wx.ID_ANY,
                                       "Create only new cards")
        sizer1.Add(self.__new_cards, 0, wx.ALL, 3)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        button = wx.Button(self, -1, "Open")
        button.Bind(wx.EVT_BUTTON, self.__on_chose_file)
        sizer2.Add(button, 0, wx.ALL, 3)
        sizer2.AddStretchSpacer(1)
        button = wx.Button(self, wx.ID_ANY, "Run")
        button.Bind(wx.EVT_BUTTON, self.__on_run)
        sizer2.Add(button, 0, wx.ALL, 3)
        sizer1.Add(sizer2, 0, wx.EXPAND)

        # add logger
        style = wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_WORDWRAP
        logger = wx.TextCtrl(self, size=(500, 300),style=style)
        sizer1.Add(logger, 1, wx.ALL|wx.EXPAND, 3)
        logger = wx.LogTextCtrl(logger)
        wx.Log.SetActiveTarget(logger)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(sizer1, 1, wx.EXPAND)
        zangoose = Path(__file__).parents[0] / "Zangoose.png"
        image = wx.Image(str(zangoose), wx.BITMAP_TYPE_ANY)
        image = image.Scale(418 // 4, 457 // 4, quality=wx.IMAGE_QUALITY_HIGH)
        image = wx.StaticBitmap(self, -1, wx.Bitmap(image))
        sizer.Add(image, 0, wx.ALL, 3)
        self.SetSizer(sizer)
        self.Fit()
        wx.LogMessage("Ready when you are! Select an Excel file")

    def __on_run(self, event):
        start_time = time()
        generator = Generator(self.__file_name_ctrl.GetValue())
        result = generator.process(self.__new_cards.GetValue())
        duration = time() - start_time
        total = sum(result.values())
        wx.LogMessage("Summary:")
        wx.LogMessage(f"  This took {duration:.1f} seconds for {total} cards.")
        for sheet, num in result.items():
            wx.LogMessage(f"  Sheet {sheet}: {num} cards generated")
        wx.LogMessage("Do you have more?")


    def __on_chose_file(self, event):
        style = (wx.FD_OPEN | wx.FD_CHANGE_DIR |
                 wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW)
        wildcard = "Excel workbook (*.xlsx)|*.xlsx|" \
                   "Macro-enabled Excel workbook (*.xlsm)|*.xlsm|" \
                   "All files (*.*)|*.*"

        dlg = wx.FileDialog(self, message="Choose a file", defaultDir=getcwd(),
                            defaultFile="", wildcard=wildcard, style=style)

        # Show the dialog and retrieve the user response. If it is the OK response,
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPaths()[0]
            self.__file_name_ctrl.SetValue(path)
            wx.LogMessage("Now press run to process the file")
        else:
            wx.LogMessage("Chicken!")

        dlg.Destroy()

class CardMakerApp(wx.App):
    def OnInit(self):
        CardMaker().Show()
        return True


def main():
    app = CardMakerApp()
    app.MainLoop()

if __name__ == "__main__":
    main()