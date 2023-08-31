import requests

def weather():
    print("Welcome to the Weather App!")
    print("This app allows you to get the weather forecast for the next 3 days.")
    while True:
        city = input("Enter the name of the city: ")
        try:
            days=int(input("How many days of forecast do you want (up to 3): "))
        except ValueError:
            print("Please enter a valid choice!")
            continue

        if days<=0 or days>3:
            print("Please enter a valid choice!")
            continue
        
        try:
            response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={YOUR_API_KEY}&q={city}&days={days}")
            response.raise_for_status()
            data = response.json()

            forecast_days = data['forecast']['forecastday']
            
            for forecast in forecast_days:
                date = forecast['date']
                max_temp = forecast['day']['maxtemp_c']
                min_temp = forecast['day']['mintemp_c']
                avg_humidity = forecast['day']['avghumidity']
                avg_wind_speed = forecast['day']['maxwind_kph']
                condition = forecast['day']['condition']['text']

                print(f"\nDate: {date}")
                print(f"Max Temperature: {max_temp}°C")
                print(f"Min Temperature: {min_temp}°C")
                print(f"Avg Humidity: {avg_humidity}%")
                print(f"Avg Wind Speed: {avg_wind_speed} kph")
                print(f"Condition: {condition}")
                print("------------------------")
            
            again = input("Would you like to enter another city (Y/N) : ")
            while again.lower() not in ("y", "n"):
                print("Enter a valid choice!")
                again = input("Would you like to enter another city (Y/N) : ")

            if again.lower()=="y":
                continue
            
            elif again.lower()=="n":
                print("Thank You for using the Weather App. Goodbye!")
                break
            
        except requests.exceptions.RequestException as e:
            print("An error occurred while making the request:", e)
        
        except KeyError:
            print("Error: Unable to retrieve data for the given city.")
            again = input("Would you like to enter another city (Y/N) : ")
            while again.lower() not in ("y", "n"): 
                print("Enter a valid choice!")
                again = input("Would you like to enter another city (Y/N) : ")

            if again.lower()=="y":
                continue
            
            elif again.lower() == "n":
                print("Thank You for using the Weather App. Goodbye!")
                break

weather()