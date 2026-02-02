import unittest
from Log_message_19_01_2025 import LogNormalizer,LogParser 

class TestLogService(unittest.TestCase):
    def test_normalize(self):
        normalizer = LogNormalizer()
        raw = "2024-11-01\tINFO  AuthService   User logged in"
        clean = normalizer.normalize(raw)
        self.assertEqual(clean, "2024-11-01 INFO AuthService User logged in")
    def test_parse_valid_log(self):
        parser = LogParser()
        log = "2024-11-01 INFO AuthService User logged in"
        result = parser.Extract(log)
        self.assertEqual(result["timestamp"], "2024-11-01")
        self.assertEqual(result["level"], "INFO")
        self.assertEqual(result["service"], "AuthService")
        self.assertEqual(result["message"], "User logged in")
    def test_parse_invalid_log(self):
        parser = LogParser()
        log = "This is not a valid log"
        result = parser.Extract(log)
        self.assertEqual(result["timestamp"], None)
        self.assertEqual(result["level"], "UNKNOWN")
        self.assertEqual(result["service"], None)
        self.assertEqual(result["message"], log)
if __name__ == "__main__":
    unittest.main()
