from abc import ABC, abstractmethod


class IEntrada(ABC):
    @abstractmethod
    def recibirInformacion(self):
        pass


class ISalida(ABC):
    @abstractmethod
    def enviarInformacion(self):
        pass


class IGestiona(ABC):
    @abstractmethod
    def gestionarUsuario(self):
        pass


class IReserva(ABC):
    def reservarParqueadero(self):
        pass


class ITutorial(ABC):
    @abstractmethod
    def desplegarMultimedia(self):
        pass

class IModerador(ABC):
    @abstractmethod
    def moderarComponentes(self):
        pass