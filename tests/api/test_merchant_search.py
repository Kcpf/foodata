from unittest import TestCase

from foodata.api.merchant_search import MerchantSearch

class TestMerchantSearch(TestCase):

    def setUp(self):
        self.merchant_searcher = MerchantSearch()

    def test_search_by_location(self):
        merchant_list, _, _ = self.merchant_searcher.get_merchants_by_location(-23.006152, -43.3430155)
    
        self.assertTrue(len(merchant_list) != 0)
        self.assertTrue(type(getattr(merchant_list[0], "name")) == str)
        
    def test_search_by_name(self):
        merchant_list, _, _ = self.merchant_searcher.get_merchants_by_name("la fruteria", -23.006152, -43.3430155)
    
        self.assertTrue(len(merchant_list) != 0)
        self.assertTrue(type(getattr(merchant_list[0], "name")) == str)
    
    def test_search_full_data(self):
        merchant = self.merchant_searcher.get_merchant_full_data("934828fc-fcc3-439b-ae33-91525e6a3456")

        self.assertTrue(type(getattr(merchant, "name")) == str )