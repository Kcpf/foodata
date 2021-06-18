from foodata.api.merchant_search import MerchantSearch


merchant_search = MerchantSearch()
result = merchant_search.get_merchants_by_location(-23.006152, -43.3430155)

print(result[0][0].id)
print(result[0][0].getMenu()[1].name)

print(merchant_search.get_merchant_full_data("934828fc-fcc3-439b-ae33-91525e6a3456").name)