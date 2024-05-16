import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from datetime import datetime
import threading

# Logger Levels
DEBUG = "DEBUG"
INFO = "INFO"
ERROR = "ERROR"


# Formatter Interface
class Formatter(ABC):
    @abstractmethod
    def format(self, level, message, timestamp):
        pass


# JSON Formatter
class JSONFormatter(Formatter):
    def format(self, level, message, timestamp):
        log_entry = {
            "level": level,
            "message": message,
            "timestamp": timestamp
        }
        return json.dumps(log_entry)


# XML Formatter
class XMLFormatter(Formatter):
    def format(self, level, message, timestamp):
        log_entry = ET.Element("log")
        ET.SubElement(log_entry, "level").text = level
        ET.SubElement(log_entry, "message").text = message
        ET.SubElement(log_entry, "timestamp").text = timestamp
        return ET.tostring(log_entry, encoding="unicode")


# Writer Interface
class Writer(ABC):
    @abstractmethod
    def write(self, message):
        pass


# Console Writer
class ConsoleWriter(Writer):
    def write(self, message):
        print(message)


# File Writer
class FileWriter(Writer):
    def __init__(self, file_name):
        self.file_name = file_name

    def write(self, message):
        with open(self.file_name, "a") as file:
            file.write(message + "\n")


# Logger Factory
class LoggerFactory:
    @staticmethod
    def create_logger(formatter, writer):
        return Logger(formatter, writer)


# Logger Singleton
class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self, formatter, writer):
        self.formatter = formatter
        self.writer = writer

    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = self.formatter.format(level, message, timestamp)
        self.writer.write(formatted_message)

    def debug(self, message):
        self.log(DEBUG, message)

    def info(self, message):
        self.log(INFO, message)

    def error(self, message):
        self.log(ERROR, message)


# Example Usage
if __name__ == "__main__":
    json_formatter = JSONFormatter()
    xml_formatter = XMLFormatter()

    console_writer = ConsoleWriter()
    file_writer = FileWriter("app.log")

    json_console_logger = LoggerFactory.create_logger(json_formatter, console_writer)
    xml_file_logger = LoggerFactory.create_logger(xml_formatter, file_writer)

    json_console_logger.debug("This is a debug message.")
    json_console_logger.info("This is an info message.")
    json_console_logger.error("This is an error message.")

    xml_file_logger.debug("This is a debug message.")
    xml_file_logger.info("This is an info message.")
    xml_file_logger.error("This is an error message.")
