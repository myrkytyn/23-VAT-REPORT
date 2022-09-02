import xml.etree.ElementTree as ET

def generate_xml(tin, c_doc_cnt, period_month, period_year, d_fill, hfill, hnamesel, hksel):
    root = ET.Element("DECLAR")
    root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:noNamespaceSchemaLocation","J1201013.XSD")
    DECLARHEAD=ET.Element("DECLARHEAD")
    root.append(DECLARHEAD)
    ET.SubElement(DECLARHEAD, "TIN").text=tin
    ET.SubElement(DECLARHEAD, "C_DOC").text="J12"
    ET.SubElement(DECLARHEAD, "C_DOC_SUB").text="010"
    ET.SubElement(DECLARHEAD, "C_DOC_VER").text="13"
    ET.SubElement(DECLARHEAD, "C_DOC_TYPE").text="0"
    #100 - Номер документу в періоді, порядковий номер кожного однотипного документу в цьому періоді
    ET.SubElement(DECLARHEAD, "C_DOC_CNT").text=c_doc_cnt
    ET.SubElement(DECLARHEAD, "C_REG").text="9"
    ET.SubElement(DECLARHEAD, "C_RAJ").text="15"
    ET.SubElement(DECLARHEAD, "PERIOD_MONTH").text=period_month
    ET.SubElement(DECLARHEAD, "PERIOD_TYPE").text="1"
    ET.SubElement(DECLARHEAD, "PERIOD_YEAR").text=period_year
    ET.SubElement(DECLARHEAD, "C_STI_ORIG").text="915"
    ET.SubElement(DECLARHEAD, "C_DOC_STAN").text="1"
    ET.SubElement(DECLARHEAD, "LINKED_DOCS").set("xsi:nil","true")
    ET.SubElement(DECLARHEAD, "D_FILL").text=d_fill
    ET.SubElement(DECLARHEAD, "SOFTWARE").text="MEDOC"

    DECLARBODY=ET.Element("DECLARBODY")
    root.append(DECLARBODY)
    ET.SubElement(DECLARBODY, "R01G1").set("xsi:nil","true")
    ET.SubElement(DECLARBODY, "R03G10S").set("xsi:nil","true")
    ET.SubElement(DECLARBODY, "HORIG1").text="1"
    ET.SubElement(DECLARBODY, "HTYPR").text="11"
    ET.SubElement(DECLARBODY, "HFILL").text=hfill
    ET.SubElement(DECLARBODY, "HNUM").text="1"
    ET.SubElement(DECLARBODY, "HNUM1").set("xsi:nil","true")
    ET.SubElement(DECLARBODY, "HNAMESEL").text=hnamesel
    ET.SubElement(DECLARBODY, "HNAMEBUY").text="Неплатник"
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HNUM2").set("xsi:nil","true")
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel
    ET.SubElement(DECLARBODY, "HKSEL").text=hksel

    tree = ET.ElementTree(root)
    tree.write("file.xml", encoding="windows-1251", xml_declaration=True)

if __name__ == "__main__":
    generate_xml("1","1","1","1","1")