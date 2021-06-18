class Facet(object):
    def __init__(self, facet):
        self.price_range = facet["priceRange"]
        self.features = facet["features"]
        self.tags = facet["tags"]
        self.available = facet["available"]
        self.delivery_fee = facet["deliveryFee"]
        self.delivery_time = facet["deliveryTime"]
        self.distance = facet["distance"]
        self.user_rating = facet["userRating"]
        self.categories = facet["categories"]
        self.takeout_time = facet["takeoutTime"]