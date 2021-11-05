from selenium import webdriver
import mysql.connector


# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")

conn = mysql.connector.connect(host="localhost", user="andrewhansbury",
                               password="m99c.xent", database="andrewhansbury_Menu")

mycursor = conn.cursor()

mycursor.execute()

for x in mycursor:
    print(x)
