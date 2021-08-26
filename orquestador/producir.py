from edu.utilidades.produccion import Produccion
import os

Produccion(False).desplegar("componentes.xml",os.path.dirname(os.path.abspath(__file__)))
