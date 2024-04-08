import tkinter as tk
import requests 

def get_weather():
    city = entry_city.get()
    api_key = "2c671aa95ba91210f1b9d0eb733352f4"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].capitalize()
        
        result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nDescription: {description}", fg="white", bg="#3f8edd")
    else:
        result_label.config(text="City not found", fg="white", bg="red")

window = tk.Tk()
window.title("Weather Forecast")
window.geometry("300x250")
window.configure(bg="#6eb5ff")

label_city = tk.Label(window, text="Enter City or Zip Code:", bg="#6eb5ff")
label_city.grid(row=0, column=0, padx=10, pady=10)

entry_city = tk.Entry(window)
entry_city.grid(row=0, column=1, padx=10, pady=10)

get_weather_button = tk.Button(window, text="Get Weather", command=get_weather, bg="#1e6bb8", fg="white")
get_weather_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="", bg="#3f8edd", fg="white")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
