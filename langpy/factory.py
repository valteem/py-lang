"""
Factory design pattern example

Adopted from https://github.com/design-patterns-for-humans/en-US-python?tab=readme-ov-file#-factory-method
"""

class FileReader:
    def read_file(self, file_path):
        pass

class CSVReader(FileReader):
    def read_file(self, file_path):
        return "CSV file content"

class XMLReader(FileReader):
    def read_file(self, file_path):
        return "XML file content"
    
class App:
    def create_file_reader(self): # factory method
        pass
    def get_file_content(self, file_path):
        reader = self.create_file_reader()
        return reader.read_file(file_path)

class AppCSV(App):
    def create_file_reader(self):
        return CSVReader()
    
class AppXML(App):
    def create_file_reader(self):
        return XMLReader()