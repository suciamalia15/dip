from transaksi import Transaksi
from kartu_debit import KartuDebit
from kartu_kredit import KartuKredit

debit_card = KartuDebit()
credit_card = KartuKredit()

trx_via_dc = Transaksi(debit_card)
trx_via_cc = Transaksi(credit_card)

trx_via_dc.do_payment(5000)
trx_via_cc.do_payment(1000)