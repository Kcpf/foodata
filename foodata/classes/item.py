from foodata.classes.choice import Choice


class Item(object):
    def __init__(self, item):
        self.id = item.get("id", None)
        self.code = item.get("code", None)
        self.description = item.get("description", None)
        self.details = item.get("details", None)
        self.logo_url = item.get("logoUrl", None)
        self.taxonomy_name = item.get("taxonomyName", None)
        self.need_choices = item.get("needChoices", None)
        self.unit_price = item.get("unitPrice", None)
        self.unit_min_price = item.get("unitMinPrice", None)
        self.unit_original_price = item.get("unitOriginalPrice", None)
        self.order = item.get("order", None)
        self.availability = item.get("availability", None)
        self.pos_code = item.get("posCode", None)
        self.opening_hours = item.get("openingHours", None)
        self.discovery_tags = item.get("discoveryTags", None)
        self.tags = item.get("tags", None)
        self.operation_modes = item.get("operationModes", None)
        self.product_tags = item.get("productTags", None)
        self.product_info = item.get("productInfo", None)
        self.enabled = item.get("enabled", None)

        if self.need_choices:
            self.choices = [Choice(c) for c in item.get("choices", [])]