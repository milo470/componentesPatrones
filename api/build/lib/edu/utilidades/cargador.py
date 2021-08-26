import importlib
from os import scandir, path
from zipfile import *
import os

_MODULO_ = 0
_INTERFACE_ = 1
_PAQUETE_ = 2
_CLASE_ = 3


class Fachada:
    def __init__(self, rueda, paquete, clase):
        self.rueda = rueda
        self.paquete = paquete
        self.clase = clase


class Cargador(importlib.machinery.PathFinder):
    proyecto = ""
    DB = dict()

    def __init__(self, proyecto, directorios):
        self.proyecto = proyecto
        self._montar_ruedas(directorios)

    def __get_implementaciones(self, arch):
        z = ZipFile(arch)
        lineas = []
        for name in z.namelist():
            if name.endswith(".inf"):
                f = z.open(name, 'r')
                for linea in f:
                    cad = str(linea, encoding='utf-8')
                    cad = ' '.join([line.strip() for line in cad.strip().splitlines()])
                    lineas.append(cad.split(','))
                return lineas

    def _montar_ruedas(self, directorios):
        for dir_i in directorios:
            ruta = path.join(self.proyecto, dir_i)
            for arch in scandir(ruta):
                if arch.is_file():
                    if ".whl" in arch.name:
                        lista = self.__get_implementaciones(arch)
                        for l_i in lista:
                            self.DB.setdefault(l_i[_MODULO_] + '.' + l_i[_INTERFACE_],
                                               Fachada(arch, l_i[_PAQUETE_], l_i[_CLASE_]))
                else:
                    self._montar_ruedas(dir)

    def _from_(self, ruta_modulo):
        self.ruta_modulo = ruta_modulo
        return self

    def _import_(self, interface_clase):
        fachada: Fachada = self.DB.get(self.ruta_modulo + '.' + interface_clase)
        if fachada is not None:
            import zipimport
            imp = zipimport.zipimporter(fachada.rueda)
            cad = fachada.paquete.replace(".", os.sep)
            paquete = imp.load_module(cad)
            clase = getattr(paquete, fachada.clase)
        else:
            modulo = importlib.import_module(self.ruta_modulo)
            clase = getattr(modulo, interface_clase)
        return clase
