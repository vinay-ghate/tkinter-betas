import tkinter as tk
from tkinter import *
import bs4
import requests
import time


def get_Score():
    site = requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
    data = bs4.BeautifulSoup(site.content,"html.parser")
    matchData = data.find('div',class_='cb-mtch-lst').getText()
    matchData.replace('xa0',"")
    matchlist = matchData.split("   ")
    for m in matchlist:
        while "  " in m:
            m = m.replace("  "," ")
    return f"Match = {matchlist[1][0:-5]}\nLocation = {matchlist[2]}\nScore = {matchlist[4]}"

def on_submit():
    result_label.config(text=get_Score(), fg="red")
    app.after(1000, on_submit)

app = tk.Tk()
app.title("Live Cricket Score")
app.geometry("400x200")
app.resizable('false','false')

Label(app,text="Live Cricket Score",font=(20)).pack(pady=5)


submit_button = tk.Button(app, text="Refresh Score", command=on_submit)
submit_button.pack(pady=5)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)


app.mainloop()