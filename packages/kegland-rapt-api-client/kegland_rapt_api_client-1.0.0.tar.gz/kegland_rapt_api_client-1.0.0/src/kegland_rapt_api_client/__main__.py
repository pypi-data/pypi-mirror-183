# __main__.py

from kegland_rapt_api_client import client

# Go to https://app.rapt.io/ and create API secrets there first!
RAPT_API_USERNAME = "[RAPT_USERNAME]"
RAPT_API_SECRET = "[RAPT_API_SECRET]"

def main():
    rapt = client.KeglandRaptAPIClient(
        RAPT_API_USERNAME, 
        RAPT_API_SECRET, 
        verbose=False
    )

    """

    # Hydrometers

    ### Get all registered hydrometers
    hydrometers = rapt.query_api("GET", "/Hydrometers/GetHydrometers")

    ### Get information about specific registered hydrometer
    hydrometer = rapt.query_api("GET", "/Hydrometers/GetHydrometer", {"hydrometerId": hydrometers[0]["id"]})

    # Fermentation chamber
    
    ### Get all registered fermentation chambers
    chambers = rapt.query_api("GET", "/FermentationChambers/GetFermentationChambers")

    ### Get information about specific registered fermentation chamber
    chamber = rapt.query_api("GET", "/FermentationChambers/GetFermentationChambers", {"fermentationChamberId": chambers[0]["id"]})

    ### Set target temperature for specific registered fermentation chamber
    chamber = rapt.query_api("POST", "/FermentationChambers/SetTargetTemperature", {"fermentationChamberId": chambers[0]["id"], "target": "1.0"})

    # Brewzilla

    ### Get all registered brewzillas
    brewzillas = rapt.query_api("GET", "/BrewZillas/GetBrewZillas")

    ### Get information about specific registered brewzilla 
    brewzilla = rapt.query_api("GET", "/BrewZillas/GetBrewZilla", {"brewZillaId": brewzillas[0]["id"]})

    ### Set target temperature for specific registered brewzilla
    brewzilla = rapt.query_api("POST", "/BrewZillas/SetTargetTemperature", {"brewZillaId": brewzillas[0]["id"], "target": "20.0"})

    ### Enable heating on  specific registered brewzilla
    brewzilla = rapt.query_api("POST", "/BrewZillas/SetHeatingEnabled", {"brewZillaId": brewzillas[0]["id"], "state": "true"})

    """

if __name__ == "__main__":
    main()