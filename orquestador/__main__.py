import sys
import os
from os.path import join

ruta = os.path.abspath(os.path.curdir)
rueda = join(join(ruta, 'api'), 'api.whl')
sys.path.append(rueda)

from edu.orquestador import Orquestador

if __name__ == "__main__":
    orq = Orquestador(ruta)
    orq.moderarComponentes()
