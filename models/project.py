import uuid
import xml.etree.ElementTree as ET


class Project(object):
    def __init__(self, name, tree):
        self.tree = tree
        self.root = tree.getroot()
        self.id = str(uuid.uuid4())
        self._name = name

    @classmethod
    def from_xml(cls, filename):
        tree = ET.parse(filename)
        return cls(filename, tree)

    def layers(self):
        for layer in self.root.iter("maplayer"):
            yield layer.find("layername").text

    @property
    def name(self):
        return self._name
