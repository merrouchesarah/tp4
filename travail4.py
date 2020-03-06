#!/usr/bin/env python
import xml.etree.ElementTree as xml

def readFile(fname):
    with open(fname,"r") as f:
        file = f.readlines()
    for line in file:
        data = line.split()
        print(data[0])


def createXML(filename):
    root = xml.Element("etudiants")
    etudiant = xml.Element("etudiant")
    root.append(etudiant)

    with open("data.txt","r") as f:
        file = f.readlines()
    for line in file:
        data = line.split()
        #matricule = xml.SubElement(etudiant,"matricule")
        print(data[0])
        #matricule.text = data[0]

    nom = xml.SubElement(etudiant, "nom")
    nom.text = ""

    prenom = xml.SubElement(etudiant, "prenom")
    prenom.text = ""

    tree = xml.ElementTree(root)
    with open(filename,"wb") as fh:
        tree.write(fh)

if __name__ == "__main__":
    createXML("etudiants.xml")
    #readFile("data.txt")