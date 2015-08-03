import uuid
import xml.etree.ElementTree as ET


class Layer(object):
    def __init__(self, node):
        self.id = str(uuid.uuid4())
        self.node = node

    @classmethod
    def from_node(cls, node):
        return cls(node)

    @property
    def details(self):
        return {ch.tag: ch.text for ch in self.node}

    @property
    def name(self):
        return self.node.find("layername").text

    def __repr__(self):
        return self.name


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
        for layernode in self.root.iter("maplayer"):
            yield Layer.from_node(layernode)

    @property
    def name(self):
        return self.root.get("projectname") or self._name

    def __repr__(self):
        return self.name
