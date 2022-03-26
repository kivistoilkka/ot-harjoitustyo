import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    def test_saldo_vahenee_oikein_rahaa_otettaessa_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_saldo_ei_muutu_rahaa_otettaessa_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_metodi_ota_rahaa_palauttaa_True_jos_rahat_riittavat(self):
        vastaus = self.maksukortti.ota_rahaa(10)
        self.assertEqual(vastaus, True)

    def test_metodi_ota_rahaa_palauttaa_False_jos_rahat_eivat_riitta(self):
        vastaus = self.maksukortti.ota_rahaa(100)
        self.assertEqual(vastaus, False)