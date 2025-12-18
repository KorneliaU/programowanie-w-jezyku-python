import requests
import argparse
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
    def __str__(self):
        return (
            f"Brewery: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"City: {self.city}\n"
            f"Country: {self.country}\n"
            f"Website: {self.website_url}\n"
        )
parser = argparse.ArgumentParser(description="Fetch breweries from OpenBreweryDB")
parser.add_argument(
    "--city",
    type=str,
    required=False,
    help="City name to filter breweries"
)
args = parser.parse_args()
url = "https://api.openbrewerydb.org/v1/breweries"
params = {"per_page": 20}
if args.city:
    params["by_city"] = args.city
response = requests.get(url, params=params)
data = response.json()
breweries = []
for item in data:
    brewery = Brewery(
        brewery_id=item.get("id"),
        name=item.get("name"),
        brewery_type=item.get("brewery_type"),
        city=item.get("city"),
        country=item.get("country"),
        website_url=item.get("website_url")
    )
    breweries.append(brewery)
for brewery in breweries:
    print(brewery)