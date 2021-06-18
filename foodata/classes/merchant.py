from foodata.api.menu_search import MenuSearch


class Merchant(object):
    def __init__(self, merchant):
        self.id = merchant.get("id", None)
        self.short_id = merchant.get("shortId", None)
        self.name = merchant.get("name", None)
        self.description = merchant.get("description", None)
        self.company_code = merchant.get("companyCode", None)
        self.address = merchant.get("address", None)
        self.phone = merchant.get("phoneIf", None)
        self.resources = merchant.get("resources", None)
        self.slug = merchant.get("slug", None)
        self.user_rating = merchant.get("userRating", None)
        self.user_rating_count = merchant.get("userRatingCount", None)
        self.price_range = merchant.get("priceRange", None)
        self.main_category = merchant.get("mainCategory", None)
        self.features = merchant.get("features", None)
        self.tags = merchant.get("tags", None)
        self.payment_codes = merchant.get("paymentCodes", None)
        self.minimum_order_value = merchant.get("minimumOrderValue", None)
        self.delivery_fee = merchant.get("deliveryFee", None)
        self.delivery_time = merchant.get("deliveryTime", None)
        self.distance = merchant.get("distance", None)
        self.available = merchant.get("available", None)
        self.takeout_time = merchant.get("takeoutTime", None)
        self.preparation_time = merchant.get("preparationTime", None)
        self.delivery_methods = merchant.get("deliveryMethods", None)
        self.merchant_chain = merchant.get("merchantChain", None)
        self.groups = merchant.get("groups", None)
        self.shifts = merchant.get("shifts", None)
        self.configs = merchant.get("configs", None)
        self.type = merchant.get("type", None)
        self.locale = merchant.get("locale", None)
        self.documents = merchant.get("documents", None)
        self.menu = None
    
    def getMenu(self):
        assert self.id != None

        menu_searcher = MenuSearch()
        self.menu = menu_searcher.get_menu_from_restaurant(self.id) 
        return self.menu 