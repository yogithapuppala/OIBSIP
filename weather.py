from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox


# declaring labels for window

win = Tk()
# title for window
win.title("BASIC WEATHER APP")
win.configure(bg="#D3A8AE")
#setting window size
win.geometry("700x500")
title_label = Label(win, text="BASIC WEATHER APP", bg="#B76E79", font={'bold', 30})
city_label = Label(win, text="Enter City Name: ", font={'bold, 20'}, fg="black", bg="#D3A8AE")
city_text = StringVar()
city_entry = Entry(win, textvariable=city_text, font={'bold', 25})
location_label = Label(win, text="Location", font={'bold', 28}, fg="black", bg="#D3A8AE")
temp_label = Label(win, text="", font={'bold', 28}, fg="black", bg="#D3A8AE")
weather_label = Label(win, text="", font={'bold', 28}, fg="black", bg="#D3A8AE")
# search_btn = Button(win, text="GET WEATHER RESULTS", width=20, command=search_city)


# extracting api key from the file
file1 = "config.ini"
config = ConfigParser()
config.read(file1)
api_key = config['gfg']['api']
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# define a function to get weather details
def get_weather(cityname):
    result = requests.get(url.format(cityname, api_key))

    if result:
        json = result.json()
        cityname = json['name']
        countryname = json['sys']
        temp_in_kelvin = json['main']['temp']
        temp_in_celcius = temp_in_kelvin-273.15
        weather_details = json['weather'][0]['main']
        final_res = [cityname, countryname, temp_in_kelvin,     temp_in_celcius, weather_details]
        return final_res
    else:
        print("No Content Found")


# function to search for the city
def search_city():
    cityname = city_text.get()
    weather_details = get_weather(cityname)
    if weather_details:
        location_label['text'] = '{}, {}'.format(weather_details[0], weather_details[1])
        temp_label['text'] = str(weather_details[3]) + " Degree Celsius"
        weather_label['text'] = weather_details[4]
    else:
        messagebox.showerror("Error", "Cannot find {}".format(cityname))
    

def clear_values():
    city_entry.delete(0, END)
    location_label["text"] = ""
    temp_label["text"] = ""
    weather_label["text"] = ""




search_btn = Button(win, text="GET WEATHER RESULTS", width=20, command=search_city, bg="#D3A8AE", fg="white")
reset_btn = Button(win, text="RESET", width=20, command=clear_values, bg="#D3A8AE", fg="white")

#arranging widgets on window
title_label.place(x=250, y=20, anchor=CENTER)
city_label.place(x =50, y=50)
city_entry.place(x=200, y=50)
reset_btn.place(x=250, y=100, anchor=CENTER)
search_btn.place(x=550, y=100, anchor=CENTER)
location_label.place(x=20, y=150)
temp_label.place(x=20, y=180)
weather_label.place(x=20, y=200)

win.mainloop()
