from edu.utilidades.produccion import Produccion
import os

Produccion().desplegar("componentes.xml", os.path.dirname(os.path.abspath(__file__)))
