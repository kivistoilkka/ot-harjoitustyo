class Kassapaate:
    edullisen_hinta = 240
    maukkaan_hinta = 400

    def __init__(self):
        self.kassassa_rahaa = 100000
        self.edulliset = 0
        self.maukkaat = 0

    def syo_edullisesti_kateisella(self, maksu):
        if maksu >= Kassapaate.edullisen_hinta:
            self.kassassa_rahaa += Kassapaate.edullisen_hinta
            self.edulliset += 1
            return maksu - Kassapaate.edullisen_hinta
        return maksu

    def syo_maukkaasti_kateisella(self, maksu):
        if maksu >= Kassapaate.maukkaan_hinta:
            self.kassassa_rahaa += Kassapaate.maukkaan_hinta
            self.maukkaat += 1
            return maksu - Kassapaate.maukkaan_hinta
        return maksu

    def syo_edullisesti_kortilla(self, kortti):
        if kortti.ota_rahaa(Kassapaate.edullisen_hinta):
            self.edulliset += 1
            return True
        return False

    def syo_maukkaasti_kortilla(self, kortti):
        if kortti.ota_rahaa(Kassapaate.maukkaan_hinta):
            self.maukkaat += 1
            return True
        return False

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa >= 0:
            kortti.lataa_rahaa(summa)
            self.kassassa_rahaa += summa
