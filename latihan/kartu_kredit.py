from kartu_pembayaran import KartuPembayaran

class KartuKredit(KartuPembayaran):
    
    def do_transaction(self, total: int):
        print("transaksi dengan kartu kredit sebesar: {total}")