import tkinter as tk
from tkinter import *
import requests
api_key = 'Enter Your API key from openweathermap.org'


def on_submit():
    user_input = entry.get()
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    if weather_data.json()['cod'] == '404':
        result_label.config(text="No City Found")
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        result_label.config(text=f"The weather in {user_input} is: {weather}\nThe temperature in {user_input} is: {temp}ºF",fg='red')

app = tk.Tk()
app.title("Simple Weather App")
app.geometry("400x200")
app.resizable('false','false')

Label(app,text="Weather App",font=(20)).pack(pady=5)

Label(app,text="Enter a Name of City Below:").pack(pady=5)

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

submit_button = tk.Button(app, text="Submit", command=on_submit)
submit_button.pack(pady=5)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)


app.mainloop()

