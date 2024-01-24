import unittest
from datetime import datetime
from is_veren_s import isi_kaydet, kayit_var_mi

class TestIsVerenS(unittest.TestCase):

    def test_isi_kaydet(self):
        # Test işlevini işaretlemek için geçerli girdilerle bir iş kaydetme işlemi
        result = isi_kaydet("Test Başlık", "Test Açıklama", 1000, datetime.now())
        self.assertIsNone(result)  # Başarılı bir şekilde None dönmeli

    def test_kayit_var_mi(self):
        # Mevcut bir kaydın kontrolü
        result = kayit_var_mi("instagram")
        self.assertTrue(result)  # Kayıt mevcut olduğu için True dönmeli

if __name__ == "__main__":
    unittest.main()
