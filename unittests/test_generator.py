#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 19:00:36 2020

@author: volker
"""
# stdlib modules
from unittest import TestCase, main
from pathlib import Path

#external modules
import wx

# internal modules
from mcm.generator import Generator

class GeneratorTest(TestCase):
    def test_run_example(self):
        app = wx.App()
        wx.Log.SetActiveTarget(wx.LogStderr())
        file = Path(__file__).resolve().parent / "example.xlsx"
        generator = Generator(file)
        generator.process()
        del app

if __name__ == "__main__":
    main()