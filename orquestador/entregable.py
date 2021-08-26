import os, shutil
import xml.etree.ElementTree as ET
from distutils import dir_util


class Entregable:

    def entregar(self, componentes="entregables.xml", dir_base=__file__):
        root = ET.parse(componentes).getroot()
        for e_i in root.findall('entregable'):
            origen = e_i.find("origen").text
            destino = e_i.find("destino").text
            if origen == '.':
                origen = os.getcwd()
            for d_i in e_i.findall('directorio'):
                print(d_i.text)
                ori = os.path.join(origen, d_i.text)
                dir_util.copy_tree(ori, os.path.join(destino, d_i.text))
            for a_i in e_i.findall('archivo'):
                print(a_i.text)
                shutil.copy2(os.path.join(origen, a_i.text), destino)


if __name__ == "__main__":
    oe = Entregable()
    oe.entregar("entregables.xml", __file__)
