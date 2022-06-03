from kartu_pembayaran import KartuPembayaran

class KartuDebit(KartuPembayaran):
    
    def do_transaction(self, total: int):
        print(f"Transaksi dengan kartu debit sebesar: {total}")