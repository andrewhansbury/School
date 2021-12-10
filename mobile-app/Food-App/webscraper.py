
from selenium import webdriver
import mysql.connector


driver = webdriver.Chrome()
driver.get("https://www.southern.edu/administration/food/index.html")

titles = driver.find_elements_by_xpath(
    "/html/body/div[2]/div/div/main/div[2]/div/div/div")
x = 0

for title in titles:
    print(f"{x}: ", title.text)
    x += 1
    title.click()


class Day:
    def __init__(self) -> None:
        self.breakfast = None
        self.lunch = None
        self.dinner = None


menu = []
Sunday = Day()
Monday = Day()
Tuesday = Day()
Wednesday = Day()
Thursday = Day()
Friday = Day()
Saturday = Day()


# test = driver.find_element_by_xpath(
#     "/html/body/div[2]/div/div/main/div[2]/div/div/div[2]")
days_meals = driver.find_elements_by_xpath(
    "/html/body/div[2]/div/div/main/div[2]/div/div/div")

for day in days_meals:
    text = day.text

    # print(test.text)
    print("*"*60)

# print(test.text)

# conn = mysql.connector.connect(host="sql5.freemysqlhosting.net", user="sql5449228",
#                                password="APtb7nqKgv", database="sql5449228")

# mycursor = conn.cursor()

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
