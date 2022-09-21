import xml.etree.ElementTree as ET
from loguru import logger
import os


def generate_root():
    root = ET.Element("DECLAR")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:noNamespaceSchemaLocation", "J1201013.XSD")
    return root


def generate_head(root, tin, period_month, period_year, d_fill):
    DECLARHEAD = ET.Element("DECLARHEAD")
    root.append(DECLARHEAD)
    ET.SubElement(DECLARHEAD, "TIN").text = tin
    ET.SubElement(DECLARHEAD, "C_DOC").text = "J12"
    ET.SubElement(DECLARHEAD, "C_DOC_SUB").text = "010"
    ET.SubElement(DECLARHEAD, "C_DOC_VER").text = "13"
    ET.SubElement(DECLARHEAD, "C_DOC_TYPE").text = "0"
#    ET.SubElement(DECLARHEAD, "C_DOC_CNT").text=c_doc_cnt
    ET.SubElement(DECLARHEAD, "C_REG").text = "9"
    ET.SubElement(DECLARHEAD, "C_RAJ").text = "15"
    ET.SubElement(DECLARHEAD, "PERIOD_MONTH").text = period_month
    ET.SubElement(DECLARHEAD, "PERIOD_TYPE").text = "1"
    ET.SubElement(DECLARHEAD, "PERIOD_YEAR").text = period_year
    ET.SubElement(DECLARHEAD, "C_STI_ORIG").text = "915"
    ET.SubElement(DECLARHEAD, "C_DOC_STAN").text = "1"
    ET.SubElement(DECLARHEAD, "LINKED_DOCS").set("xsi:nil", "true")
    ET.SubElement(DECLARHEAD, "D_FILL").text = d_fill
    ET.SubElement(DECLARHEAD, "SOFTWARE").text = "MEDOC"


def generate_body(root, hfill, hnamesel, hksel, htinsel):
    DECLARBODY = ET.Element("DECLARBODY")
    root.append(DECLARBODY)
    ET.SubElement(DECLARBODY, "R01G1").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R03G10S").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "HORIG1").text = "1"
    ET.SubElement(DECLARBODY, "HTYPR").text = "11"
    ET.SubElement(DECLARBODY, "HFILL").text = hfill
    ET.SubElement(DECLARBODY, "HNUM").text = "1"
    ET.SubElement(DECLARBODY, "HNUM1").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "HNAMESEL").text = hnamesel
    ET.SubElement(DECLARBODY, "HNAMEBUY").text = "Неплатник"
    ET.SubElement(DECLARBODY, "HKSEL").text = hksel
    ET.SubElement(DECLARBODY, "HNUM2").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "HTINSEL").text = htinsel
    ET.SubElement(DECLARBODY, "HKS").text = "1"
    ET.SubElement(DECLARBODY, "HKBUY").text = "100000000000"
    ET.SubElement(DECLARBODY, "HFBUY").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "HTINBUY").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "HKB").set("xsi:nil", "true")
#    ET.SubElement(DECLARBODY, "R04G11").text = r04g11
#    ET.SubElement(DECLARBODY, "R03G11").text = r03g11
#    ET.SubElement(DECLARBODY, "R03G7").text = r03g7
    ET.SubElement(DECLARBODY, "R03G109").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R03G14").set("xsi:nil", "true")
#    ET.SubElement(DECLARBODY, "R01G7").text=r01g7
    ET.SubElement(DECLARBODY, "R01G109").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R01G14").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R01G9").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R01G8").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R01G10").set("xsi:nil", "true")
    ET.SubElement(DECLARBODY, "R02G11").set("xsi:nil", "true")
    return DECLARBODY


def generate_b_part(DECLARBODY, dish, row, qnt, price):
    RXXXXG3S = ET.SubElement(DECLARBODY, "RXXXXG3S")
    RXXXXG3S.text = dish
    RXXXXG3S.set("ROWNUM", row)

    #RXXXXG4=ET.SubElement(DECLARBODY, "RXXXXG4")
    #RXXXXG4.text = zed
    #RXXXXG4.set("ROWNUM", row)

    RXXXXG32 = ET.SubElement(DECLARBODY, "RXXXXG32")
    RXXXXG32.set("ROWNUM", row)
    RXXXXG32.set("xsi:nil", "true")

    RXXXXG33 = ET.SubElement(DECLARBODY, "RXXXXG33")
    RXXXXG33.set("ROWNUM", row)
    RXXXXG33.set("xsi:nil", "true")

    RXXXXG4S = ET.SubElement(DECLARBODY, "RXXXXG4S")
    RXXXXG4S.set("ROWNUM", row)
    RXXXXG4S.text = "порц"

    RXXXXG105_2S = ET.SubElement(DECLARBODY, "RXXXXG105_2S")
    RXXXXG105_2S.set("ROWNUM", row)
    RXXXXG105_2S.text = "3011"

    RXXXXG5 = ET.SubElement(DECLARBODY, "RXXXXG5")
    RXXXXG5.set("ROWNUM", row)
    RXXXXG5.text = qnt

    RXXXXG6 = ET.SubElement(DECLARBODY, "RXXXXG6")
    RXXXXG6.set("ROWNUM", row)
    RXXXXG6.text = price

    RXXXXG008 = ET.SubElement(DECLARBODY, "RXXXXG008")
    RXXXXG008.set("ROWNUM", row)
    RXXXXG008.text = "20"

    RXXXXG009 = ET.SubElement(DECLARBODY, "RXXXXG009")
    RXXXXG009.set("ROWNUM", row)
    RXXXXG009.set("xsi:nil", "true")

    #RXXXXG010 = ET.SubElement(DECLARBODY, "RXXXXG010")
    #RXXXXG010.set("ROWNUM", row)
    #RXXXXG010

    #RXXXXG11_10 = ET.SubElement(DECLARBODY, "RXXXXG11_10")
    #RXXXXG11_10.set("ROWNUM", row)
    #RXXXXG11_10
    
    RXXXXG011 = ET.SubElement(DECLARBODY, "RXXXXG011")
    RXXXXG011.set("ROWNUM", row)
    RXXXXG011.set("xsi:nil", "true")


def generate_ending(DECLARBODY, hbos, hkbos):
    ET.SubElement(DECLARBODY, "HBOS").text = hbos
    ET.SubElement(DECLARBODY, "HKBOS").text = hkbos
    ET.SubElement(DECLARBODY, "R003G10S").set("xsi:nil", "true")


def generate_xml(root):
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    return tree
