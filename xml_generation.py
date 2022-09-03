import xml.etree.ElementTree as ET
from loguru import logger
import os


def generate_xml(tin, period_month, period_year, d_fill, hfill, hnamesel, hksel, htinsel, hbos, hkbos, iiko_name, xml_target_path):
    root = ET.Element("DECLAR")
    root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root.set("xsi:noNamespaceSchemaLocation", "J1201013.XSD")
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
#    ET.SubElement(DECLARBODY, "RXXXXG3S").text
#    ET.SubElement(DECLARBODY, "RXXXXG4").text
#    ET.SubElement(DECLARBODY, "RXXXXG32").text
#    ET.SubElement(DECLARBODY, "RXXXXG33").text (nil)
#    ET.SubElement(DECLARBODY, "RXXXXG4S").text
#    ET.SubElement(DECLARBODY, "RXXXXG105_2S").text
#    ET.SubElement(DECLARBODY, "RXXXXG5").text
#    ET.SubElement(DECLARBODY, "RXXXXG6").text
#    ET.SubElement(DECLARBODY, "RXXXXG008").text
#    ET.SubElement(DECLARBODY, "RXXXXG009").text (nil)
#    ET.SubElement(DECLARBODY, "RXXXXG010").text
#    ET.SubElement(DECLARBODY, "RXXXXG11_10").text
#    ET.SubElement(DECLARBODY, "RXXXXG011").text
    ET.SubElement(DECLARBODY, "HBOS").text = hbos
    ET.SubElement(DECLARBODY, "HKBOS").text = hkbos
    ET.SubElement(DECLARBODY, "R003G10S").set("xsi:nil", "true")

    tree = ET.ElementTree(root)
    if not os.path.exists(f"../{xml_target_path}"):
        os.makedirs(f"../{xml_target_path}")
    try:
        tree.write(f"../{xml_target_path}{hfill}_{iiko_name}.xml", encoding="windows-1251", xml_declaration=True)
    except Exception as e:
        logger.error(f"Error saving {xml_target_path}{hfill}_{iiko_name}.xml file")
        logger.error(e)
        return
    