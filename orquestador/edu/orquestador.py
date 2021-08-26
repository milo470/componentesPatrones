from api.edu.utilidades.cargador import Cargador

from api.edu.cableado.api import IEntrada, ISalida, ITutorial, IReserva, IGestiona, IModerador

import tkinter as tk


class Orquestador(IModerador):

    def __init__(self, ruta):
        self.ruta = ruta

    def moderarComponentes(self):
        crg = Cargador(self.ruta, ['back', 'front'])

        try:
            entr: IEntrada = crg._from_(IEntrada.__module__)._import_(IEntrada.__name__)()
            entr.recibirInformacion()

            salid: ISalida = crg._from_(ISalida.__module__)._import_(ISalida.__name__)()
            salid.enviarInformacion()

            gest: IReserva = crg._from_(IReserva.__module__)._import_(IReserva.__name__)()
            gest.reservarParqueadero()

            multi: ITutorial = crg._from_(ITutorial.__module__)._import_(ITutorial.__name__)()
            multi.desplegarMultimedia()


        except Exception as e1:
            master = tk.Tk()
            tk.Message(master, text="no hay GUI").pack()
            tk.mainloop()

        try:
            core: IGestiona = crg._from_(IGestiona.__module__)._import_(IGestiona.__name__)()
            core.gestionarUsuario()
        except Exception as e2:
            master = tk.Tk()
            tk.Message(master, text="no hay Core").pack()
            tk.mainloop()
