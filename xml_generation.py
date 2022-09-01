import xml.etree.ElementTree as ET

def generate_xml(tin,c_doc,c_doc_sub,c_doc_ver,c_doc_type,c_doc_cnt,c_reg,c_raj,period_month,period_type,period_year,c_sti_orig,c_doc_stan,d_fill):
    root = ET.Element("DECLAR")
    root.set("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:noNamespaceSchemaLocation","J1201013.XSD")
    DECLARHEAD=ET.Element("DECLARHEAD")
    root.append(DECLARHEAD)
    ET.SubElement(DECLARHEAD, "TIN").text=tin
    ET.SubElement(DECLARHEAD, "C_DOC").text="J12"
    ET.SubElement(DECLARHEAD, "C_DOC_SUB").text=
    ET.SubElement(DECLARHEAD, "C_DOC_VER").text=c_doc_ver
    ET.SubElement(DECLARHEAD, "C_DOC_TYPE").text=c_doc_type
    ET.SubElement(DECLARHEAD, "C_DOC_CNT").text=c_doc_cnt
    ET.SubElement(DECLARHEAD, "C_REG").text=c_reg
    ET.SubElement(DECLARHEAD, "C_RAJ").text=c_raj
    ET.SubElement(DECLARHEAD, "PERIOD_MONTH").text=period_month
    ET.SubElement(DECLARHEAD, "PERIOD_TYPE").text=period_type
    ET.SubElement(DECLARHEAD, "PERIOD_YEAR").text=period_year
    ET.SubElement(DECLARHEAD, "C_STI_ORIG").text=c_sti_orig
    ET.SubElement(DECLARHEAD, "C_DOC_STAN").text=c_doc_stan
    ET.SubElement(DECLARHEAD, "LINKED_DOCS").set("xsi:nil","true")
    ET.SubElement(DECLARHEAD, "D_FILL").text=d_fill
    ET.SubElement(DECLARHEAD, "SOFTWARE").text="MEDOC"

    DECLARBODY=ET.Element("DECLARBODY")
    root.append(DECLARBODY)

    tree = ET.ElementTree(root)
    tree.write("file.xml", encoding="windows-1251", xml_declaration=True)

if __name__ == "__main__":
    generate_xml("1","1","1","1","1","1","1","1","1","1","1","1","1","1")