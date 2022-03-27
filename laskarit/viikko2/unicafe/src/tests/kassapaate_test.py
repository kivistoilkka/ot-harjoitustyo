import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    # Alustus oikein
    def test_rahamaara_on_alussa_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_edulliset_on_alussa_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myydyt_maukkaat_on_alussa_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Edullisesti käteisellä, onnistuvat ostot
    def test_edullisesti_kateisella_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisesti_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
    
    def test_edullisesti_kateisella_myydyt_lounaat_kasvavat(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    # Edullisesti käteisellä, epäonnistuvat ostot
    def test_edullisesti_kateisella_ei_riittavalla_summalla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisesti_kateisella_ei_riittavalla_summalla_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_edullisesti_kateisella_ei_riittavalla_summalla_lounaat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Maukkaasti käteisellä, onnistuvat ostot
    def test_maukkaasti_kateisella_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaasti_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
    
    def test_maukkaasti_kateisella_myydyt_lounaat_kasvavat(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    # Maukkaasti käteisellä, epäonnistuvat ostot
    def test_maukkaasti_kateisella_ei_riittavalla_summalla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaasti_kateisella_ei_riittavalla_summalla_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)

    def test_maukkaasti_kateisella_ei_riittavalla_summalla_lounaat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # Edullisesti kortilla, onnistuvat ostot
    def test_edullisesti_kortilla_summa_veloitetaan_kortilta_ja_palautetaan_True(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(vastaus, True)
        self.assertEqual(self.kortti.saldo, 760)
    
    def test_edullisesti_kortilla_myydyt_lounaat_kasvavat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisesti_kortilla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    # Edullisesti kortilla, epäonnistuvat ostot
    def test_edullisesti_kortilla_ei_riittavalla_summalla_kortin_summa_ei_muutu_ja_palautetaan_False(self):
        self.kortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(vastaus, False)
        self.assertEqual(self.kortti.saldo, 200)
    
    def test_edullisesti_kortilla_ei_riittavalla_summalla_myydyt_lounaat_ei_muutu(self):
        self.kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    # Maukkaasti kortilla, onnistuvat ostot
    def test_maukkaasti_kortilla_summa_veloitetaan_kortilta_ja_palautetaan_True(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(vastaus, True)
        self.assertEqual(self.kortti.saldo, 600)
    
    def test_maukkaasti_kortilla_myydyt_lounaat_kasvavat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukkaasti_kortilla_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    # Maukkaasti kortilla, epäonnistuvat ostot
    def test_maukkaasti_kortilla_ei_riittavalla_summalla_kortin_summa_ei_muutu_ja_palautetaan_False(self):
        self.kortti = Maksukortti(200)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(vastaus, False)
        self.assertEqual(self.kortti.saldo, 200)
    
    def test_maukkaasti_kortilla_ei_riittavalla_summalla_myydyt_lounaat_ei_muutu(self):
        self.kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    # Rahan lataaminen kortille
    def test_rahaa_ladatessa_kortin_saldo_muuttuu_positiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo, 1500)
    
    def test_rahaa_ladatessa_kortin_saldo_ei_muutu_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kortti.saldo, 1000)
    
    def test_rahaa_ladatessa_kassan_rahamaara_muuttuu_positiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100500)
    
    def test_rahaa_ladatessa_kassan_rahamaara_ei_muutu_negatiivisella_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)