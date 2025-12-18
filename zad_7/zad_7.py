import requests
class Brewery:
    def __init__(
        self,
        brewery_id: str,
        name: str,
        brewery_type: str,
        city: str,
        country: str,
        website_url: str
    ):
        self.brewery_id = brewery_id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country
        self.website_url = website_url


    def __str__(self) -> str:
        return (
            f"Brewery: {self.name}, "
            f"type: {self.brewery_type}, "
            f"city: {self.city}, "
            f"country: {self.country}"
            f"website_url: {self.website_url}"
        )
url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"
response = requests.get(url)

data = response.json()
breweries = []

for item in data:
    brewery = Brewery(
        brewery_id=item.get("id"),
        name=item.get("name"),
        city=item.get("city"),
        country=item.get("country"),\
        brewery_type=item.get("brewery_type"),
        website_url=item.get("website_url")
    )
    breweries.append(brewery)
for brewery in breweries:
    print(brewery)