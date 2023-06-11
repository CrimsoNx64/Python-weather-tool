import pyowm
from datetime import datetime
import pytz
import tkinter as tk

## imports ^^

owm = pyowm.OWM("API KEY") # api ket
weather_mgr = owm.weather_manager()

def gui():
    root = tk.Tk()
    root.title("Weather Station")

    bg_color = "black"

    canvas = tk.Canvas(root, width=500, height=500, bg=bg_color)
    canvas.pack()

    frame = tk.Frame(root, bg="black")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    welcome_label = tk.Label(frame, text="Weather Statistics", font=("Arial", 15), pady=10, bg="black", fg="white")
    welcome_label.pack()

    weather_label = tk.Label(frame, font=("Arial", 10), justify=tk.LEFT, bg="black", fg="white")
    weather_label.pack()

    root.configure(bg=bg_color)
    root.after(1000, lambda: update_weather_label(weather_label, root))  # updates every second
    root.mainloop()

def get_weather():
  place = "London" # place of weather
  
  #timezone of place
  timezone = pytz.timezone("Europe/London")
  current_time = datetime.now(timezone).strftime("%H:%M:%S")

  #weather observations
  observation = weather_mgr.weather_at_place(place)
  w = observation.weather
  temp = w.temperature("celsius")["temp"]
  status = w.detailed_status
  wind_speed = w.wind("miles_hour")["speed"]
  wind_speed2 = round(wind_speed, 1)
  wind_direction = w.wind().get("deg", "Unknown")
  rain = w.rain
  clouds = w.clouds
  v = w.visibility_distance
  if rain == {}:
        rain = "None"
  else:
    rain = w.rain["1h"]

  #displays weather info
  weather_info = f"Place: {place}\n\nTime: {current_time}\n\nTemperature: {temp}°C\n\nStatus: {status}\n\nWind speed (mph): {wind_speed2}\n\nWind direction: {wind_direction} degrees\n\nRain (mm / hour): {rain}\n\nCloud coverage: {clouds}%\n\nVisibility: {v} metres"
  return weather_info

def update_weather_label(weather_label, root):
    weather_info = get_weather()
    weather_label.config(text=weather_info)
    root.after(1000, lambda: update_weather_label(weather_label, root))  # updates every second

gui() 
