# This is intended to be full of static helper methods
import xml.etree.ElementTree as ET
from typing import Union, Optional, List, Dict, Tuple
import re

class TableauRestXml:
    tableau_namespace = 'http://tableau.com/api'
    ns_map = {'t': 'http://tableau.com/api'}
    ns_prefix = '{' + ns_map['t'] + '}'
    # ET.register_namespace('t', ns_map['t'])
    # Generic method for XML lists for the "query" actions to name -> id dict
    @staticmethod
    def convert_xml_list_to_name_id_dict(xml_obj: ET.Element) -> Dict:
        d = {}
        for element in xml_obj:
            e_id = element.get("id")
            # If list is collection, have to run one deeper
            if e_id is None:
                for list_element in element:
                    e_id = list_element.get("id")
                    name = list_element.get("name")
                    d[name] = e_id
            else:
                name = element.get("name")
                d[name] = e_id
        return d

    # Repeat of above method with shorter name
    @staticmethod
    def xml_list_to_dict(xml_obj: ET.Element) -> Dict:
        d = {}
        for element in xml_obj:
            e_id = element.get("id")
            # If list is collection, have to run one deeper
            if e_id is None:
                for list_element in element:
                    e_id = list_element.get("id")
                    name = list_element.get("name")
                    d[name] = e_id
            else:
                name = element.get("name")
                d[name] = e_id
        return d

    @staticmethod
    def luid_name_dict_from_xml(xml_obj: ET.Element) -> Dict:
        d = {}
        for element in xml_obj:
            e_id = element.get("id")
            # If list is collection, have to run one deeper
            if e_id is None:
                for list_element in element:
                    e_id = list_element.get("id")
                    name = list_element.get("name")
                    d[e_id] = name
            else:
                name = element.get("name")
                d[e_id] = name
        return d

    @staticmethod
    def luid_content_url_dict_from_xml(xml_obj: ET.Element) -> Dict:
        d = {}
        for element in xml_obj:
            e_id = element.get("id")
            # If list is collection, have to run one deeper
            if e_id is None:
                for list_element in element:
                    e_id = list_element.get("id")
                    name = list_element.get("contentUrl")
                    d[e_id] = name
            else:
                name = element.get("contentUrl")
                d[e_id] = name
        return d

    # This corrects for the first element in any response by the plural collection tag, which leads to differences
    # with the XPath search currently
    @staticmethod
    def make_xml_list_iterable(xml_obj: ET.Element) -> List[ET.Element]:
        pass

    # 32 hex characters with 4 dashes
    @staticmethod
    def is_luid(val: str) -> bool:
        luid_pattern = r"[0-9a-fA-F]*-[0-9a-fA-F]*-[0-9a-fA-F]*-[0-9a-fA-F]*-[0-9a-fA-F]*"
        if len(val) == 36:
            if re.match(luid_pattern, val) is not None:
                return True
            else:
                return False
        else:
            return False