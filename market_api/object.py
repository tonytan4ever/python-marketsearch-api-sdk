
class VinHistoryOutput:
    def __init__(self,
                 id,
                 price,
                 miles,
                 data_source,
                 vdp_url,
                 seller_type,
                 inventory_type,
                 trim_r,
                 last_seen_at,
                 last_seen_at_date,
                 scraped_at,
                 scraped_at_date,
                 first_seen_at,
                 first_seen_at_date,
                 source,
                 seller_name,
                 city,
                 state,
                 zip,
                 status_date
                 ):
        self.id = id
        self.price = price
        self.miles = miles
        self.data_source = data_source
        self.vdp_url = vdp_url
        self.seller_type = seller_type
        self.inventory_type = inventory_type
        self.trim_r = trim_r
        self.last_seen_at = last_seen_at
        self.last_seen_at_date = last_seen_at_date
        self.scraped_at = scraped_at
        self.scraped_at_date = scraped_at_date
        self.first_seen_at = first_seen_at
        self.first_seen_at_date = first_seen_at_date
        self.source = source
        self.seller_name = seller_name
        self.city = city
        self.state = state
        self.zip = zip
        self.status_date = status_date
