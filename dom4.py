DATA_FILE = "listetudiants.xml"
import xml.dom.minidom as minidom
import sys
def main():
    try:
        xmldoc = minidom.parse(DATA_FILE)
    except:
        print("Can't Open the file")
        sys.exit()
    print (xmldoc.toxml())

    return 0
