#!/usr/bin/python3
"""serialization and deserialization using 
XML as an alternative format to JSON.
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding= 'utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:
        data[child.tag] = child.text

    return (data)
