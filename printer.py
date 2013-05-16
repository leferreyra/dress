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

        
# """No se bien los atributos que llevaria. Yo le puse prenda(para sacar el tipo y costo) 
# y compra(para saber la cantidad de ropa que compro) pero fijate frankii o leo!!!!"""

class ImpresionComprobante:
    def __init__(self, carrito, nombre_cliente, monto_pago):
        self.printer = Printer()
        self.carrito = carrito
        self.nombre_cliente = nombre_cliente
        self.monto_pago = monto_pago
        self.doc_name = ""

    def Imprimir(self):
        self.printer.Print(self.GetHtml(), self.doc_name)

    def VistaPrevia(self):
        self.printer.PreviewText(self.GetHtml(), self.doc_name)

    def GetHtml(self):
        TOTAL = 0
        html = "<html><table width='310'><tr><td  width='95'><img src='aym.jpg'></td><td width='20'><img src='Separador.jpg'></td><td width='140'><table><tr><td VALIGN='top' ALIGN='right'><h6>Comprobante No valido como factura</h6></td></tr><tr><td VALIGN='bottom' ALIGN='right'>Fecha: %d/%d/%d</td></tr></table></td></tr>" %(datetime.date.today().day, datetime.date.today().month, datetime.date.today().year)
        
        html += "<tr><td COLSPAN = 3>Cliente: %s</td></tr>" % self.nombre_cliente

        html +="<tr><table width='310' border='1' style='border:solid;'><tr><th>Detalle</th><th width='60'>Monto</th></tr>"

        for prenda in self.carrito.getPrendas():
            html += "<tr><td>%s</td><td>%g</td></tr>" %(prenda.getNombre(), prenda.getPrecio())
            TOTAL += prenda.getPrecio() 

        html += "<tr><td>%s</td><td>%g</td></tr>" %("Total:", TOTAL)
        if self.monto_pago > 0:
            html += "<tr><td>%s</td><td>%g</td></tr>" %("Pago:", self.monto_pago)
        
        html +="</table></tr></table>"
        html +="<table width='310'><tr><td width='60'></td><td ALIGN='right'>Resta Pagar:</td><td width='60'>%g</td></tr></table>" % (TOTAL - self.monto_pago)
        html +="<br><br>"
        html +="<table width='310'><tr><td></td><td width='250' ALIGN='centre'>Gracias por tu compra!!!</td><td></td></tr></table><html>"

        return html
