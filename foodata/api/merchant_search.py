import requests

from foodata.api.helpers import headers_first, payload
from foodata.classes.merchant import Merchant
from foodata.classes.facet import Facet


class MerchantSearch(object):
    def __init__(self):
        self.merchants = None
        self.facets = None
        self.total = None
    
    def _merchant_to_object(self, merchantJson):
        return Merchant(merchantJson)
    
    def _facet_to_object(self, facetJson):
        return Facet(facetJson)

    def _merchant_search_by_location(self, latitude, longitude, page):
        url = f"https://marketplace.ifood.com.br/v2/merchants?latitude={latitude}&longitude={longitude}&channel=IFOOD&page={page}"

        try:
            response = requests.request("GET", url, headers=headers_first, data=payload).json()
            self.merchants = response["merchants"]
            self.facets = response["facets"]
            self.total = response["total"]
        except Exception:
            raise Exception("A problem has ocurred during Merchant Search By Location Request")

    def _merchant_search_by_name(self, latitude, longitude, name, page):
        name = "+".join(name.split())
        url = f"https://marketplace.ifood.com.br/v2/search/merchants?latitude={latitude}&longitude={longitude}&channel=IFOOD&term={name}&page={page}"

        try:
            response = requests.request("GET", url, headers=headers_first, data=payload).json()
            self.merchants = response["merchants"]["data"]
            self.facets = response["merchants"]["facets"]
            self.total = response["merchants"]["total"]
        except Exception:
            raise Exception("A problem has ocurred during Merchant Search By Name Request")
    
    def _merchant_search_full_data(self, merchant_id):
        url = f"https://marketplace.ifood.com.br/v1/merchants/{merchant_id}/extra"

        try:
            response = requests.request("GET", url, headers=headers_first, data=payload).json()
            self.merchants = response
        except Exception:
            raise Exception("A problem has ocurred during Merchant Search Full Data Request")

    def get_merchants_by_name(self, name, latitude, longitude, page = 0):
        self._merchant_search_by_name(latitude, longitude, name, page)
        merchants = [self._merchant_to_object(merc) for merc in self.merchants]
        facets = self._facet_to_object(self.facets)

        return merchants, facets, self.total

    def get_merchants_by_location(self, latitude, longitude, page = 0):
        self._merchant_search_by_location(latitude, longitude, page)
        merchants = [self._merchant_to_object(merc) for merc in self.merchants]
        facets = self._facet_to_object(self.facets)

        return merchants, facets, self.total
    
    def get_merchant_full_data(self, merchant_id):
        self._merchant_search_full_data(merchant_id)
        
        return self._merchant_to_object(self.merchants)
