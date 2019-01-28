# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 15:36:33 2019

"""

import wx

def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()
    
def save(event):
    file = open(filename.GetValue())
    file.write(contents.GetValue())
    file.close()
    
app = wx.App()
win = wx.Frame(None, title="sample editor", size=(410, 335))

bkg = wx.Panel(win)

loadbutton = wx.Button(bkg, label='open')
loadbutton.Bind(wx.EVT_BUTTON, load)

savebutton = wx.Button(bkg, label='save')
savebutton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag=wx.EXPAND)
hbox.Add(loadbutton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(savebutton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)

win.Show()
app.MainLoop()