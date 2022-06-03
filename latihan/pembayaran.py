from abc import ABC, abstractmethod

class KartuPembayaran(ABC):
    
    @abstractmethod
    def do_transaction(self, total: int):
        pass