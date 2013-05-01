from wx.html import HtmlEasyPrinting
import datetime

class Printer(HtmlEasyPrinting):
    def __init__(self):
        HtmlEasyPrinting.__init__(self)

    def GetHtmlText(self,text):

        html_text = text.replace('\n', '<BR>')
        return html_text

    def Print(self, text, doc_name):
        self.SetHeader(doc_name)
        self.PrintText(self.GetHtmlText(text),doc_name)

    def PreviewText(self, text, doc_name):
        self.SetHeader(doc_name)
        HtmlEasyPrinting.PreviewText(self, self.GetHtmlText(text))

"""No se bien los atributos que llevaria. Yo le puse prenda(para sacar el tipo y costo) 
y compra(para saber la cantidad de ropa que compro) pero fijate frankii o leo!!!!"""
class ImpresionComprobante()
    def __init__(self, carrito):
        self.printer = Printer()
        self.carrito = carrito
        self.doc_name = ""

    def Imprimir(self):
        self.printer.Print(self.GetHtml(), self.doc_name)

    def VistaPrevia(self):
        self.printer.PreviewText(self.GetHtml(), self.doc_name)

    def GetHtml(self):
        TOTAL = 0
        html = "<html><table width="310px"><tr><td  width="95px"><img src="aym.jpg"></td><td width="20px"><img src="Separador.jpg"></td><td width="140px"><table><tr><td VALIGN="top" ALIGN="right"><h5>COMPROBANTE Documento no valido como factura</h5></td></tr><tr><td VALIGN="bottom" ALIGN="right">Fecha: %d/%d/%d</td></tr></table></td></tr>" %(datetime.date.today().day, datetime.date.today().month, datetime.date.today().year)
        html +="<tr><table width="310px" border="1" style="border:solid;"><tr><th width="60">Tipo</th><th>Detalle</th><th width="60">Monto</th></tr>"

        for i in compra
            html += "<tr><td>%d</td><td>%s</td><td>%g</td></tr>" %(i.ladero, i.ladero2, i.laderoladero)
            TOTAL += i.laderoladero
            
        html +="</table></tr></table>"
        html +="<table width="310px"><tr><td width="60"></td><td ALIGN="right">Total a Pagar:</td><td width="60">%d</td></tr></table>" %(TOTAL)
        html +="<br><br>"
        html +="<table width="310px"><tr><td></td><td width="250px" ALIGN="centre">GRACIAS POR TU COMPRA!!!</td><td></td></tr></table><html>"

        return html
