import requests

def get_weather(api_key,city):
    #this url is the location from where we will fetch the data
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    #the parametes which will be sent with the base url
    #final url: http://api.openweathermap.org/data/2.5/weather?q=kolkata&appid=eb22c2a067ed531a86575498bad22fe9&units=metric
    params = {
        'q': city,
        'appid': api_key,
        'units':'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            return [data, response.status_code]
        else:
            return None
            # return ["Weather data not available", response.status_code]
        
    except Exception as e:
        return None
        # return ["Weather data not available", response.status_code]

if __name__=="__main__":
    print(get_weather('eb22c2a067ed531a86575498bad22fe9','kolkata'))