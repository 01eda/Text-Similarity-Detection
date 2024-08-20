from rouge_score import rouge_scorer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit

class rogue(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ROUGE SKORU HESAPLAMA UYGULAMASI")
        # ekran tasarım kısmı ve metinleri aldığımız kısım
        self.hoca_ozeti_text = QTextEdit()
        self.algoritmaozet_text = QTextEdit()
        self.hesapla_butonu = QPushButton("Benzerlik Oranını Hesapla")
        self.skor = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("ALGORİTMA İLE BULDUĞUMUZ ÖZET:"))
        layout.addWidget(self.hoca_ozeti_text)
        layout.addWidget(QLabel("GERÇEK ÖZET:"))
        layout.addWidget(self.algoritmaozet_text)
        layout.addWidget(self.hesapla_butonu)
        layout.addWidget(self.skor)

        self.hesapla_butonu.clicked.connect(self.rouge_skoru_hesapla)

        self.setLayout(layout)

    def rouge_skoru_hesapla(self):
        hocaozeti = self.hoca_ozeti_text.toPlainText()
        bizimozet = self.algoritmaozet_text.toPlainText()
        #rogue skoru otomatik hesapladığımız yer 
        otomatik_hesaplanan_scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
        skorlar = otomatik_hesaplanan_scorer.score(hocaozeti, bizimozet)
        rouge_l_skoru = skorlar['rougeL'].fmeasure

        self.skor.setText(f"HESAPLANMIŞ ROUGE-L Skoru: {rouge_l_skoru}")


if __name__ == "__main__":
    uygulama = QApplication([])
    pencere = rogue()
    pencere.show()
    uygulama.exec_()
