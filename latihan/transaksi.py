from kartu_pembayaran import KartuPembayaran

class Transaksi:

    def __init__(self, media: KartuPembayaran):
        self.__media = media 

    def do_payment(self, total: int):
        self.__media.do_transaction(total)
        