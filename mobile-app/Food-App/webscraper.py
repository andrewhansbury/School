from selenium import webdriver
import mysql.connector


driver = webdriver.Chrome()
driver.get("https://www.southern.edu/administration/food/index.html")

titles = driver.find_elements_by_xpath(
    "/html/body/div[2]/div/div/main/div[2]/div/div/div")
x = 0
for title in titles:
    print(f"{x}: ", title)
    x += 1
    title.click()


# conn = mysql.connector.connect(host="sql5.freemysqlhosting.net", user="sql5449228",
#                                password="APtb7nqKgv", database="sql5449228")

# mycursor = conn.cursor()

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)
