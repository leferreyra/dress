import cPickle as pickle
from os.path import exists
from models import ListaPrendas, ListaClientes, Configuracion, Cliente

DATA_FILE = 'dress.dat'
objects = {}

def save(sfile=DATA_FILE):

    dfile = open(sfile, 'wb')
    pickler = pickle.Pickler(dfile)
    pickler.dump(objects)
    dfile.close()


def load(lfile=DATA_FILE):

    global objects

    dfile = open(lfile, 'rb')
    unpickler = pickle.Unpickler(dfile)
    data = unpickler.load() 
    dfile.close()

    objects = data


# En caso de no existir el archivo de datos, se crea un nuevo archivo
# con las colecciones de datos vacias

if not exists(DATA_FILE):

    objects = {
        'clientes': ListaClientes(),
        'prendas': ListaPrendas(),
        'configuracion': Configuracion(),
        'NEW_PRENDA_ID': 0,
        'CLIENTE_CASUAL': Cliente("0", 'cliente_casual', '', '', '', '')
    }

    save()
