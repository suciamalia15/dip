from barang_elektronik import barangElektronik

class saklar:

    def __init__(self, item: BarangElektronik, keaktifan: bool = False):
        self.__item = iten
        self.__keaktifan =__keaktifan

    def berubah(self):
        if self.__keaktifan:
            self.__item.berhenti()
            self.__keaktiffan = False
        else:
            self.__item.beroprasi()
            self.__keaktifan = True

