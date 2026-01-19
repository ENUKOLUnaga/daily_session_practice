"""
Problem 1: Log Message Normalization Service
You are building a backend service that ingests raw application logs coming from multiple systems.
 The logs are inconsistent in format, contain noise characters, and sometimes embed metadata inside free text.
Design a module that:
Cleans and normalizes log messages

Extracts structured information from text

Stores processed logs efficiently for fast lookups

Supports future extension for new log formats without modifying existing logic

The solution must be testable with unit tests that validate parsing accuracy and edge cases.
"""
import re
class LogNormalizer:
    #Removing extra characters and spaces by ascii escape sequence
    def normalize(self, log):
        log = re.sub(r"[^\x20-\x7E]", " ", log)
        log = re.sub(r"\s+", " ", log).strip()
        return log
#extract structured information from the log
class LogParser:
    def Extract(self, log):
        pattern = r"(\S+)\s+(INFO|WARN|ERROR|DEBUG)\s+(\S+)\s+(.*)"
        match = re.match(pattern, log)
        if match:
            return {
                "timestamp": match.group(1),
                "level": match.group(2),
                "service": match.group(3),
                "message": match.group(4)
            }
        return {
            "timestamp": None,
            "level": "UNKNOWN",
            "service": None,
            "message": log
        }
#Store logs in list
class LogStore:
    def __init__(self):
        self.logs = []
    def add(self, log):
        self.logs.append(log)
    def find_by_level(self, level):
        return [log for log in self.logs if log["level"] == level]
class LogProcessor:
    def __init__(self):
        self.normalizer = LogNormalizer()
        self.parser = LogParser()
        self.store = LogStore()
    def process(self, log):
        clean_log = self.normalizer.normalize(log)
        extract_log = self.parser.Extract(clean_log)
        self.store.add(extract_log)
        return extract_log
#Main program
if __name__ == "__main__":
    processor = LogProcessor()
    log = input("Enter log message:")
    result = processor.process(log)
    print("\nProcessed Log:")
    for key, value in result.items():
        print(f"{key}: {value}")
