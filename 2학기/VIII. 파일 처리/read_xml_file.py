# p.244
import xml.etree.ElementTree as ET

f = open("order.xml", encoding="UTF-8")
string = f.read()
tree = ET.ElementTree(ET.fromstring(string))
root = tree.getrot()
print(root.tag)