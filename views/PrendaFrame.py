#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Mon Mar 18 16:40:23 2013

import wx

# begin wxGlade: extracode
# end wxGlade



class PrendaFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PrendaFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, -1)
        self.label_prenda = wx.StaticText(self.panel_1, -1, "PRENDA")
        self.label_nombre = wx.StaticText(self.panel_1, -1, "Nombre", style=wx.ALIGN_RIGHT)
        self.texto_nombre = wx.TextCtrl(self.panel_1, -1, "")
        self.label_talle = wx.StaticText(self.panel_1, -1, "Talle", style=wx.ALIGN_CENTRE)
        self.texto_talle = wx.TextCtrl(self.panel_1, -1, "")
        self.label_costo = wx.StaticText(self.panel_1, -1, "Costo", style=wx.ALIGN_RIGHT)
        self.texto_costo = wx.TextCtrl(self.panel_1, -1, "")
        self.label_precio = wx.StaticText(self.panel_1, -1, "Precio", style=wx.ALIGN_RIGHT)
        self.texto_precio = wx.TextCtrl(self.panel_1, -1, "")
        self.label_descripcion = wx.StaticText(self.panel_1, -1, u"Descripción")
        self.text_descripcion = wx.TextCtrl(self.panel_1, -1, "", style=wx.TE_MULTILINE)
        self.label_vendida = wx.StaticText(self.panel_1, -1, "Vendida", style=wx.ALIGN_RIGHT)
        self.combo_box_vendida = wx.ComboBox(self.panel_1, -1, choices=["No", "Si"], style=wx.CB_DROPDOWN | wx.CB_READONLY)
        self.boton_cancelar = wx.Button(self.panel_1, -1, "Cancelar")
        self.boton_guardar = wx.Button(self.panel_1, -1, "Guardar")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PrendaFrame.__set_properties
        self.SetTitle("frame_1")
        self.label_prenda.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.label_nombre.SetMinSize((56, 18))
        self.label_nombre.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.texto_nombre.SetMinSize((320, 26))
        self.texto_nombre.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_talle.SetMinSize((56, 18))
        self.label_talle.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.texto_talle.SetMinSize((40, 26))
        self.texto_talle.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_costo.SetMinSize((42, 18))
        self.label_costo.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.texto_costo.SetMinSize((80, 26))
        self.texto_costo.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_precio.SetMinSize((46, 18))
        self.label_precio.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.texto_precio.SetMinSize((80, 26))
        self.texto_precio.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.label_descripcion.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.text_descripcion.SetMinSize((400, 78))
        self.label_vendida.SetMinSize((59, 18))
        self.label_vendida.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Ubuntu"))
        self.combo_box_vendida.SetMinSize((80, 27))
        self.combo_box_vendida.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.combo_box_vendida.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PrendaFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.label_prenda, 0, wx.LEFT | wx.TOP, 10)
        sizer_4.Add(self.label_nombre, 0, wx.LEFT | wx.TOP, 10)
        sizer_4.Add(self.texto_nombre, 0, wx.LEFT | wx.TOP, 6)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.label_talle, 0, wx.LEFT | wx.TOP | wx.ALIGN_RIGHT | wx.ALIGN_CENTER_HORIZONTAL, 10)
        sizer_5.Add(self.texto_talle, 0, wx.LEFT | wx.TOP, 6)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_5_copy.Add(self.label_costo, 0, wx.LEFT | wx.TOP, 6)
        sizer_5_copy.Add(self.texto_costo, 0, wx.LEFT | wx.TOP, 6)
        sizer_6.Add(sizer_5_copy, 1, wx.EXPAND, 0)
        sizer_5_copy_1.Add(self.label_precio, 0, wx.LEFT | wx.TOP, 10)
        sizer_5_copy_1.Add(self.texto_precio, 0, wx.LEFT | wx.TOP, 6)
        sizer_6.Add(sizer_5_copy_1, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_2.Add(self.label_descripcion, 0, wx.LEFT | wx.TOP, 10)
        sizer_2.Add(self.text_descripcion, 0, wx.ALL, 10)
        sizer_7.Add(self.label_vendida, 0, wx.LEFT | wx.TOP, 10)
        sizer_7.Add(self.combo_box_vendida, 0, wx.LEFT | wx.TOP, 6)
        sizer_2.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_8.Add(self.boton_cancelar, 0, 0, 0)
        sizer_8.Add(self.boton_guardar, 0, 0, 0)
        sizer_2.Add(sizer_8, 1, wx.RIGHT | wx.BOTTOM | wx.ALIGN_RIGHT, 8)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.LEFT | wx.TOP, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class PrendaFrame
class FramePrincipal(wx.Frame):
    def __init__(self, *args, **kwds):
        # content of this block not found: did you rename this class?
        pass

    def __set_properties(self):
        # content of this block not found: did you rename this class?
        pass

    def __do_layout(self):
        # content of this block not found: did you rename this class?
        pass

# end of class FramePrincipal
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = FramePrincipal(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
