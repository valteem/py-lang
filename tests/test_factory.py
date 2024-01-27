import pytest

from langpy.factory import AppCSV, AppXML

def test_factory():

    a_csv = AppCSV()
    assert a_csv.get_file_content("some file path") == "CSV file content"

    a_xml = AppXML()
    assert a_xml.get_file_content("some file path") == "XML file content"