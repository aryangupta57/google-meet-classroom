from flask import Flask, render_template, request
import pandas as pd
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
import time
import datetime
from threading import Thread
from constant import CHROME_DRIVER_PATH, BASE_URL, COMMANDS


def splitIn12(arr):
    res = []
    for x in range(0, len(arr), 12):
        res.append(arr[x : x + 12])
    return res


def scrap(username, password):
    time.sleep(10)
    webD = wb.Chrome(CHROME_DRIVER_PATH)
    webD.get(BASE_URL)

    login = webD.find_element_by_xpath(
        '//*[@id="page-content"]/section[1]/div/div[1]/div[2]/div/a/button/span'
    )
    login.click()

    enterMail = webD.find_element_by_xpath('//*[@id="identifierId"]')
    enterMail.send_keys(username)
    enterMail.send_keys(Keys.ENTER)
    time.sleep(4)

    enterPassword = webD.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input'
    )
    enterPassword.send_keys(password)
    enterPassword.send_keys(Keys.ENTER)

    # core
    reset = 0
    first = True
    data_list = []
    running = True

    while running:
        counter = 0
        time.sleep(1)
        chats = webD.find_elements_by_class_name("GDhqjd")
        for msg in chats:
            counter = counter + 1
            try:
                word = msg.find_element_by_class_name("oIy2qc").text
                name = msg.find_element_by_class_name("YTbUzc").text
            except:
                word = "Message eror"
                name = "You"
            if word == "!stop":
                running = False
            elif word == "!me" and counter > reset:
                try:
                    dataFrame = pd.DataFrame(data_list)
                    topActivity = dataFrame["Name"].value_counts()
                    freq = topActivity[name]
                    resulText = "Hey {} your activity level is {}".format(name, freq)
                    enter = webD.find_element_by_xpath(
                        '//*[@id="ow3"]/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea'
                    )
                    enter.click()
                    enter.send_keys(resulText)
                    enter.send_keys(Keys.ENTER)
                except:
                    print("Unexpected Error")
            elif first == True:
                file_csv_dict = {
                    "Name": name,
                    "Message": word,
                    "Time": datetime.datetime.now(),
                }
                data_list.append(file_csv_dict)
                first = False
            elif counter <= reset:
                pass
            else:
                file_csv_dict = {
                    "Name": name,
                    "Message": word,
                    "Time": datetime.datetime.now(),
                }
                data_list.append(file_csv_dict)

        if first == False and counter > reset:
            df_temp = pd.DataFrame(data_list)
            df_temp.to_csv("current_session.csv", index=False)
            topAct = df_temp["Name"].value_counts()
        reset = counter

    df = pd.DataFrame(data_list)
    overallDataFrame = pd.read_csv("overall.csv")
    overallDataFrame = overallDataFrame.append(df)
    overallDataFrame.to_csv("overall.csv", index=False)


def async_slow_function(username, password):
    thr = Thread(target=scrap, args=[username, password])
    thr.start()
    return thr


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        username = result.get("email")
        password = result.get("passw")
        async_slow_function(username, password)
        return render_template("command.html", username=username, commands=COMMANDS)


@app.route("/analysis")
def analysis():
    df = pd.read_csv("overall.csv")
    df2 = df["Name"].value_counts().rename_axis("names").reset_index(name="counts")
    barGraphData = df2.to_dict("records")
    final = splitIn12(barGraphData)
    return render_template("graph.html", graphicBig=final)


@app.route("/realTime")
def realtime():
    df = pd.read_csv("current_session.csv")
    df2 = df["Name"].value_counts().rename_axis("names").reset_index(name="counts")
    barGraphData = df2.to_dict("records")
    final = splitIn12(barGraphData)
    return render_template("graph.html", graphicBig=final)


if __name__ == "__main__":
    app.run()
