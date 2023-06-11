import pyowm
from datetime import datetime
import pytz
import tkinter as tk

## imports ^^

owm = pyowm.OWM("API KEY HERE")# api key
weather_mgr = owm.weather_manager()

def get_weather():# gets weather + timezone info of an area
    place = "London, GB"# place to get weather info
    timezone = pytz.timezone("Europe/London")# sets the place for the timezone
    current_time = datetime.now(timezone).strftime("%H:%M:%S")
    observation = weather_mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature("celsius")["temp"]
    status = w.detailed_status
    wind_speed = w.wind("miles_hour")["speed"]
    wind_speed2=round(wind_speed,1)
    wind_direction=w.wind()["deg"]
    rain = w.rain
    clouds = w.clouds
    v = w.visibility_distance
    if rain == {}:
        rain = "None"
    weather_info = f" Place: {place}\n\n Time: {current_time}\n\n Temperature: {temp}°C\n\n Status: {status}\n\n Wind speed (mph): {wind_speed2}\n\n Wind direction: {wind_direction} degrees \n\n Rain: {rain}\n\n Cloud coverage: {clouds}%\n\n Visibility: {v} metres"# displays the weather info
    return weather_info

def update_weather_label():
    weather_info = get_weather()
    weather_label.config(text=weather_info)
    root.after(1000, update_weather_label)  # update every second

root = tk.Tk()
root.title("Weather Station")# title

# set background color
bg_color = "black"

canvas = tk.Canvas(root, width=500, height=500, bg=bg_color)
canvas.pack()

frame = tk.Frame(root, bg="black")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

welcome_label = tk.Label(frame, text="Weather Statistics", font=("Arial", 15), pady=10, bg="black", fg="white")
welcome_label.pack()

weather_label = tk.Label(frame, font=("Arial", 10), justify=tk.LEFT, bg="black",fg="white")
weather_label.pack()

update_weather_label()  # initial

root.configure(bg=bg_color)
root.mainloop()
