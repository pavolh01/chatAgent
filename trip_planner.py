import requests




def get_hotel_gaia_id(query):
    url = "https://hotels-com-provider.p.rapidapi.com/v2/regions"

    querystring = {
        "query": query,
        "domain": "AE",
        "locale": "en_GB"
    }

    headers = {
        "X-RapidAPI-Key": "4e3d252e58msh85ba9a1f818a542p10a6a9jsn6715ccabbe79",
        "X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    obj = response.json()

    if 'data' in obj and len(obj['data']) > 0:
        return obj['data'][0]['gaiaId']
    else:
        return None





def get_hotels_data(num):
    url = "https://hotels-com-provider.p.rapidapi.com/v2/hotels/search"

    querystring = {
        "region_id": num,
        "locale": "en_GB",
        "checkin_date": "2024-09-26",
        "sort_order": "REVIEW",
        "adults_number": "1",
        "domain": "AE",
        "checkout_date": "2024-09-27",
        "children_ages": "4,0,15",
        "lodging_type": "HOTEL,HOSTEL,APART_HOTEL",
        "price_min": "10",
        "star_rating_ids": "3,4,5",
        "meal_plan": "FREE_BREAKFAST",
        "page_number": "1",
        "price_max": "500",
        "amenities": "WIFI,PARKING",
        "payment_type": "PAY_LATER,FREE_CANCELLATION",
        "guest_rating_min": "8",
        "available_filter": "SHOW_AVAILABLE_ONLY"
    }

    headers = {
        "X-RapidAPI-Key": "4e3d252e58msh85ba9a1f818a542p10a6a9jsn6715ccabbe79",
        "X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        obj = response.json()
        if "properties" in obj:
            new_list = [obj["properties"][i]["name"] for i in range(5)]
            return new_list
        else:
            return []  # If 'properties' key is not present in the response
    else:
        return []  # If the request fails for some reason

def get_weather_info(city):
    # Replace with your own OpenWeatherMap API key
    api_key = "227e2003708e91a9aecae779f62dcb10"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Specify units as metric for Celsius
    }
    
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        weather_info = f"Weather in {city}: {weather_description}, Temperature: {temperature}°C"
        print(weather_info)
        return weather_info
    else:
        print(f"Unable to retrieve weather information for {city}")
        return None

class TripPlanner:
    def __init__(self):
        self.destination = None
        self.budget = None
        self.start_date = None
        self.end_date = None

    def initiate_conversation(self):
        self.destination = input("Where would you like to travel? ")
        self.get_user_input()

    def get_user_input(self):
        self.budget = float(input("Enter your budget in USD: "))
        self.start_date = input("Enter your start date (YYYY-MM-DD): ")
        self.end_date = input("Enter your end date (YYYY-MM-DD):")

    def suggest_itinerary(self):
        print(f"\nTrip Plan to {self.destination}:")
        print(f"Budget: ${self.budget}")
        print(f"Duration: {self.start_date} to {self.end_date}")

        weather_info = get_weather_info(self.destination)
        # Example usage:

        print(get_hotel_gaia_id(self.destination))
        if weather_info:
            self.ask_for_flight_booking()

    def ask_for_flight_booking(self):
        response = input("Would you like to find an accomodation for your trip? (yes/no): ")
        if response.lower() == 'yes':
            print("Searching for best hotels around...")
            hotel_names = get_hotels_data(get_hotel_gaia_id(self.destination))

            print(hotel_names)
            # Here, add your logic or function call to search for flights
        else:
            print("Accomodation search skipped.")

def main():
    planner = TripPlanner()
    planner.initiate_conversation()
    planner.suggest_itinerary()

if __name__ == "__main__":
    main()
