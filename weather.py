import tkinter as tk
from tkinter import messagebox
import requests


API_KEY = "b184aad6363623803dc1cab94914fff1"


def get_weather():
    city = city_entry.get().strip()

    if city == "":
        messagebox.showerror("Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        
        print(data)

        
        if response.status_code != 200:
            messagebox.showerror("Error", data.get("message", "Unknown Error"))
            return

        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"]
        wind = data["wind"]["speed"]

        result.config(
            text=f"""
City : {city_name}

Temperature : {temp} °C

Humidity : {humidity} %

Pressure : {pressure} hPa

Wind Speed : {wind} m/s

Weather : {weather.title()}
"""
        )

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "No Internet Connection")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------

root = tk.Tk()
root.title("Weather App")
root.geometry("450x450")
root.config(bg="skyblue")

title = tk.Label(
    root,
    text="Weather Application",
    font=("Arial", 20, "bold"),
    bg="skyblue"
)
title.pack(pady=10)

city_entry = tk.Entry(
    root,
    font=("Arial", 16),
    width=25
)
city_entry.pack(pady=10)

btn = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    command=get_weather
)
btn.pack(pady=10)

result = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="skyblue",
    justify="left"
)
result.pack(pady=20)

root.mainloop()



