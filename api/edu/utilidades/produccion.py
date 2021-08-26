import os, shutil
import xml.etree.ElementTree as ET


class Produccion:
    origen = ""
    destino = ""
    nombre = ""
    ext = ""

    def __init__(self, instalando=True):
        self.instalando = instalando

    def desplegar(self, componentes="componentes.xml", dir_base=__file__):
        ruta = os.path.join(dir_base, componentes)
        root = ET.parse(ruta).getroot()
        os.chdir(dir_base)
        for componente_i in root.findall('componente'):
            self.nombre = componente_i.find("nombre").text
            self.ext = componente_i.find("ext").text
            self.origen = componente_i.find("origen").text
            self.destino = componente_i.find("destino").text
            if self.instalando: self.instalar()  # para ser reconocido nada mas
            self.distribuir()
            self.destinar()
            self.limpiar(dir_base)

    def instalar(self):
        os.system('python setup.py install')

    def distribuir(self):
        os.system('python setup.py bdist_wheel')

    def destinar(self):
        try:
            os.makedirs(self.destino)
        except:
            pass
        for parent, _, filenames in os.walk(self.origen):
            for fn in filenames:
                if fn.lower().endswith("." + self.ext):
                    nombre = self.nombre + '.' + self.ext
                    os.rename(os.path.join(parent, fn), os.path.join(parent, nombre))
                    try:
                        os.remove(os.path.join(self.destino, nombre))
                    except:
                        pass
                    shutil.move(os.path.join(parent, nombre), self.destino)

    def limpiar(self, dir_trabajo):
        try:
            shutil.rmtree(dir_trabajo + "\\dist")
        except:
            pass
        try:
            shutil.rmtree(dir_trabajo + "\\build")
        except:
            pass
        try:
            shutil.rmtree(dir_trabajo + "\\" + self.nombre + ".egg-info")
        except:
            pass
