from geocoders.geocoder import Geocoder
from api import API


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:

        node = API.get_area(area_id)
        adress = node.name

        while node := API.get_area(node.parent_id):

            adress = node.name + " "  + adress

        return adress