import xml.etree.ElementTree as ET

from pyhabbo.models.hotlooks import HotLook, HotLooks
from pyhabbo.resources.base import BaseResource


class ListsResource(BaseResource):
    def list_hotlooks(self) -> HotLooks:
        xml_text = self._transport.request_text("GET", "/lists/hotlooks")
        root = ET.fromstring(xml_text)

        looks = [
            HotLook(
                gender=element.attrib["gender"],
                figure=element.attrib["figure"],
                figure_hash=element.attrib["hash"],
            )
            for element in root.findall("habbo")
        ]

        return HotLooks(avatar_url=root.attrib.get("url", ""), looks=looks)
