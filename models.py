import datetime
import string
import wx
from wx.lib.pubsub import Publisher as pub

class Movimiento:
    """
    Un movimiento representa alguna transaccion de productos
    y/o dinero. Sirve como base para compras, entregas, etc..
    """

    def __init__(self, cliente):

        self.fecha = datetime.date.today()
        self.cliente = cliente


    def __cmp__(self, otroMov):

        if (self.fecha > otroMov.fecha):
            return 1
        elif (self.fecha < otroMov.fecha):
            return -1
        else: 
            return 0



class Pago(Movimiento):
    """
    Un pago es una entrega de dinero en cualquier concepto. Ya sea
    en una Compra (en concepto de entrega) o saldar una deuda.
    """

    def __init__(self, monto, cliente):

        Movimiento.__init__(self, cliente)
        self.monto = monto



class Compra(Movimiento):
    """
    Una compra representa un movimiento en el cual se realiza el
    pago parcial o completo de una prenda por parte de un cliente. 
    Y se retira el producto.
    """

    def __init__(self, monto, prenda, cliente):

        Movimiento.__init__(self, cliente)
        self.prenda = prenda
        self.monto = monto



class Condicional(Movimiento):
    """
    Un concepto de la magia villangelense, donde una persona puede 
    llevar una prenda y decidir si lo va a comprar luego. Sino devuelve la
    prenda.
    """

    def __init__(self, prenda, cliente):

        Movimiento.__init__(self, cliente)
        self.prenda = prenda



class Cliente:
    """
    Representa a un Cliente, y contiene su informacion.
    """

    def __init__(self, dni, nombre, telefono, email, direccion, fecha_nacimiento):

        self._dni = dni
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._direccion = direccion
        self._fecha_nacimiento = fecha_nacimiento

        self._compras = []
        self._pagos = []
        self._condicionales = []


    def setNombre(self, nombre):

        self._nombre = nombre
        pub.sendMessage("CAMBIO_CLIENTE", self)


    def setTelefono(self, telefono):

        self._telefono = telefono
        pub.sendMessage("CAMBIO_CLIENTE", self)


    def setEmail(self, email):

        self._email = email
        pub.sendMessage("CAMBIO_CLIENTE", self)

    def setFechaNacimiento(self, fecha):
        self._fecha_nacimiento = fecha
        pub.sendMessage("CAMBIO_CLIENTE", self)

    def setDireccion(self, direccion):
        self._direccion = direccion
        pub.sendMessage("CAMBIO_CLIENTE", self)

   
    def addCompra(self, compra):

        self._compras.append(compra)
        pub.sendMessage("COMPRA_AGREGADA", self)


    def addPago(self, pago):

        self._pagos.append(pago)
        pub.sendMessage("PAGO_AGREGADO", self)


    def deleteCompra(self, compra):

        self._compras.remove(compra)
        pub.sendMessage("COMPRA_ELIMINADA", self)

    
    def deletePago(self, pago):

        self._pagos.remove(pago)
        pub.sendMessage("PAGO_ELIMINADO", self)


    def addCondicional(self, condicional):

        self._condicionales.append(condicional)
        pub.sendMessage("CONDICIONAL_AGREGADO", self)

    def deleteCondicional(self, condicional):

        self._condicionales.remove(condicional)
        pub.sendMessage("CONDICIONALES_ELIMINADOS")
        
    def deleteCondicionales(self):

        self._condicionales = []
        pub.sendMessage("CONDICIONALES_ELIMINADOS", self)


    def getDni(self):

        return self._dni


    def getMovimientos(self):

        movimientos = self._compras + self._pagos + self._condicionales
        movimientos.sort()

        return movimientos


    def getSaldo(self):

        deuda = 0
        credito = 0

        for compra in self._compras:
            deuda += compra.prenda.precio

        for pago in self._pagos:
            credito += pago.monto

        return (credito - deuda)


    def getUltimoPago(self):
        if len(self._pagos) > 0:
            return max(self._pagos, key= lambda x:x.fecha)
        else:
            raise NameError('no_hay_pagos')
    
    def getEstado(self):

        # La cantidad de dias en la cual se debe realizar un pago
        plazo = datetime.timedelta(days=30)


        try:
            # Cantidad de dias desde que hizo el ultimo pago hasta hoy
            delta = (datetime.date.today() - self.getUltimoPago().fecha).days
        except NameError:
            if len(self._compras) > 0:
                delta = (datetime.date.today() - self._compras[0].fecha).days
            else:
                return 'al_dia'
        

        en_plazo = delta < 30

        if self.getSaldo() == 0 or en_plazo:
            return "al_dia"
        else:
            
            if delta > 60:
                return "moroso"
            else:
                return "tardio"

    def getNombre(self):
        
        return self._nombre  

    def getTelefono(self):
        
        return self._telefono

    def getEmail(self):

        return self._email

    def getFechaNacimiento(self):

        return self._fecha_nacimiento
    
    def getDireccion(self):
        return self._direccion


    def cumpleAniosEsteMes(self):
        nacim = self._fecha_nacimiento.GetMonth() +1
        actual = datetime.date.today().month

        if nacim == actual:
            return True
        else: 
            return False

    def getCompraPorPrenda(self, prenda):
        
        for compra in self._compras:
            if prenda == compra.prenda:
                return compra
                break

class Prenda:
    """
    Representa una prenda de ropa. El producto del negocio.
    """

    _index = 0 # Lleva la cuenta de los codigos de las prendas

    def __init__(self, nombre, talle, costo, precio, descripcion):

        self._codigo = Prenda._index #el codigo se autoasigna con el valor de _index
        Prenda._index += 1

        self.nombre = nombre
        self.talle = talle
        self.costo = costo
        self.precio = precio
        self.descripcion = descripcion
        #si fue vendida cliente apunta al ciente que se vendio, y _condicional esta en False.
        #si esta como condicional cliente apunta al cliente que lo llevo cndicional y 
        #condicional esta en verdadero. Si aun no fue vendidia ni esta en condicional, _cliente
        #no almacena ningun cliente y condicional esta en false.
        self._cliente = None 
        self._condicional = False

    def getNombre(self):
        return self.nombre

    def getTalle(self):
        return self.talle

    def getCosto(self):
        return self.costo

    def getPrecio(self):
        return self.precio

    def getDescripcion(self):
        return self.descripcion

    def setNombre(self, nombre):

        self.nombre = nombre
        pub.sendMessage("CAMBIO_PRENDA", self)


    def setTalle(self, talle):

        self.talle = talle
        pub.sendMessage("CAMBIO_PRENDA", self)


    def setCosto(self, costo):

        self.costo = costo
        pub.sendMessage("CAMBIO_PRENDA", self)

    
    def setPrecio(self, precio):
    
        self.precio = precio
        pub.sendMessage("CAMBIO_PRENDA", self)


    def setDescripcion(self, descripcion):

        self.descripcion = descripcion
        pub.sendMessage("CAMBIO_PRENDA", self)


    def setCliente(self, cliente):

        self._cliente = cliente
        pub.sendMessage("CAMBIO_PRENDA", self)


    def setCondicional(self, condicional):

        self._condicional = condicional
        pub.sendMessage("CAMBIO_PRENDA", self)
    

    def getEstado(self):

        estado = "disponible"
        
        if (self._cliente != None) and not self._condicional:
            estado = "vendida"
        elif (self._cliente != None) and self._condicional:
            estado = "condicional"

        return estado

    def getCodigo(self):

        return self._codigo

    def getCliente(self):

        return self._cliente

class ListaClientes:
    """
    Coleccion de instancias de Cliente
    """

    def __init__(self):

        self._clientes = []
    def __len__(self):
        
        longitud = len(self._clientes)
        return longitud


    def addCliente(self, cliente):
        flag = False
        #buscamos que no exista un cliente con ese dni
        for clientebus in self._clientes:
            if clientebus.getDni() == cliente.getDni():
                flag = True
                break

        if flag:
            raise NameError('prenda_no_disponible')
        else:
            self._clientes.append(cliente)
            pub.sendMessage("CLIENTE_AGREGADO", cliente)


    def deleteCliente(self, cliente):

        cliente.deleteCondicionales()

        for movimiento in cliente.getMovimientos():
            movimiento.cliente = cliente_casual
            
            if isinstance(movimiento, Compra):
                cliente_casual.addCompra(movimiento)
            elif isinstance(movimiento, Pago):
                cliente_casual.addPago(movimiento)      

        self._clientes.remove(cliente)
        pub.sendMessage("CLIENTE_ELIMINADO", self)


    def getClientes(self): 

        return self._clientes
    

    def getClientesPorEstado(self, estado):
        
        return filter(lambda c:c.getEstado()==estado, self._clientes)


    def getClientesMorosos(self):

        return self.getClientesPorEstado('moroso')


    def getClientesAlDia(self):

        return self.getClientesPorEstado('al_dia')


    def getClientesTardios(self):

        return self.getClientesPorEstado('tardio')


    def getClientePorDni(self, dni):

        return filter(lambda c:c.getDni()==dni, self._clientes)[0]


    def findClientePorNombre(self, nombre):

        return filter(lambda c:string.find(string.lower(c.getNombre()), string.lower(nombre)) >= 0, self._clientes)
                

    def getClientesActivos(self, configuracion):

        clientes_activos = []

        if configuracion.mostrar_morosos:
            for cliente in self.getClientesMorosos():
                clientes_activos.append(cliente)

        if configuracion.mostrar_tardios:
            for prenda in self.getClientesTardios():
                clientes_activos.append(cliente)
       
        if configuracion.mostrar_al_dia:
            for cliente in self.getClientesAlDia():
                clientes_activos.append(cliente)

        return clientes_activos



class ListaPrendas:
    """
    Coleccion de instancias de Prenda.
    """

    def __init__(self):

        self._prendas = []


    def addPrenda(self, prenda):

        self._prendas.append(prenda)
        pub.sendMessage("PRENDA_AGREGADA", prenda)
    

    def deletePrenda(self, prenda):
        if prenda.getEstado() == 'disponible':

            self._prendas.remove(prenda)
            pub.sendMessage("PRENDA_ELIMINADA", self)
        else:
            raise NameError('prenda_no_disponible')


    def getPrendas(self): 
    
        return self._prendas


    def getPrendasVendidas(self):

        return filter(lambda p:p.getEstado() == 'vendida', self._prendas)


    def getPrendasDisponibles(self):

        return filter(lambda p:p.getEstado()== 'disponible', self._prendas)


    def getPrendasCondicionales(self):

        return filter(lambda p:p.getEstado() == 'condicional', self._prendas)


    def getPrendaPorCodigo(self, codigo):

        return filter(lambda p:p.getCodigo()==codigo, self._prendas)[0]


    def findPrendaPorNombre(self, nombre):

        return filter(lambda p:string.find(string.lower(p.nombre), string.lower(nombre)) >= 0, self._prendas)

    #este metodo filtra las prendas que se deben mostrar segun la configuracion actual
    def getPrendasActivas(self, configuracion):

        prendas_activas = []

        if configuracion.mostrar_vendidas:
            for prenda in self.getPrendasVendidas():
                prendas_activas.append(prenda)

        if configuracion.mostrar_condicionales:
            for prenda in self.getPrendasCondicionales():
                prendas_activas.append(prenda)
       
        if configuracion.mostrar_disponibles:
            for prenda in self.getPrendasDisponibles():
                prendas_activas.append(prenda)

        return prendas_activas

class Carrito:
    """
    Almacena terporalmente las prendas antes de realizar la venta
    """

    def __init__(self):

        self._prendas = []

    def addOrDeletePrenda(self, prenda):

        #agrega o quita una prenda al carrito, siempre y cuando este disponible
        
        if prenda.getEstado() == 'disponible':
            try:
                self._prendas.remove(prenda)
                pub.sendMessage("PRENDA_ELIMINADA_CARRITO", self)          
            except:
                self._prendas.append(prenda)
                pub.sendMessage("PRENDA_AGREGADA_CARRITO", self)  
        else:
            raise NameError('prenda_no_disponible')

    def getPrendas(self): 
    
        return self._prendas

    def vaciarCarrito(self):
        self._prendas = []

        pub.sendMessage("CARRITO_VACIADO", self)

    def enCarrito(self, prenda):
        flag = False
        for p in self._prendas:
            if p == prenda:
                flag = True
                break
        return flag
            

class Configuracion:
    """
    Guarda la configuracion del sistema
    """

    def __init__(self):
        
        self.mostrar_morosos = True
        self.mostrar_tardios = True
        self.mostrar_al_dia = True

        self.mostrar_vendidas = True
        self.mostrar_condicionales = True
        self.mostrar_disponibles = True

    def setMostrarMorosos(self, estado):
        self.mostrar_morosos = estado
        pub.sendMessage("CONFIGURACION_CLIENTES_CAMBIO", self)

    def setMostrarTardios(self, estado):
        self.mostrar_tardios = estado
        pub.sendMessage("CONFIGURACION_CLIENTES_CAMBIO", self)

    def setMostrarAlDia(self, estado):
        self.mostrar_al_dia = estado
        pub.sendMessage("CONFIGURACION_CLIENTES_CAMBIO", self)

    def setMostrarVendidas(self, estado):
        self.mostrar_vendidas = estado
        pub.sendMessage("CONFIGURACION_PRENDAS_CAMBIO", self)
       
    def setMostrarCondicionales(self, estado):
        self.mostrar_condicionales = estado
        pub.sendMessage("CONFIGURACION_PRENDAS_CAMBIO", self)

    def setMostrarDisponibles(self, estado):
        self.mostrar_disponibles = estado
        pub.sendMessage("CONFIGURACION_PRENDAS_CAMBIO",self)







#Creacion del cliente casual, al que se le asignan ventas casuales.

cliente_casual = Cliente("0", 'cliente_casual', '', '', '', '')
