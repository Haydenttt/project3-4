from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
# from bs4 import BeautifulSoup
import pymysql
import csv
import xlwt
import configparser

# # prepare for Database Connection
# # host = 'localhost'
# username = input("Please Input Database Username:\n")
# password = input("Please Input Database Password:\n")

# try:
#     db1 = pymysql.connect("localhost", username, password, "testdb",charset='utf8')
#     # use cursor() to create 'cursor object' making following execution
#     cursor = db1.cursor()
#     print("Connection Successful!")
#     # return username, password
# except Exception:
#     print("Username or Password Error, Process Terminating.")
#     # optimized for cmd window execution
#     time.sleep(2)

def baidu(keyword):
    # Use Configiration file to implement database connection
    cf = configparser.ConfigParser()
    cf.read("sqlconfig.conf")
    # kvs=cf.items("db")
    host = cf.get("db","host")
    user = cf.get("db","user")
    password = cf.get("db","password")
    db = cf.get("db","database")
    port = cf.get("db","port")
    db1 = pymysql.connect(host=host,user=user,password=password,db=db,port=int(port))
    cursor = db1.cursor()
    print("Connection Successful")
    # csv

    # setup a counting number as global augument for def search(keyword) section to use
    global num
    num = 0

    def search(keyword):

            driver = webdriver.Chrome()
            driver.get('https://www.baidu.com')
            driver.find_element_by_id('kw').send_keys(keyword)
            driver.find_element_by_id('su').click()
            # wait until the 1st result page loaded, on occasion that elements below'nextpage' could be located
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'foot')))

            global num
            # call the global argument 'num' when first used in this def section
            while True:
                # use xpath to parse link title in tag<h3>, on the current page
                content_h3 = driver.find_elements_by_xpath("//*/h3")
                try:
                    # look through the current page, orderly extract all headlines in tag<h3>, name it as WebsiteName
                    for WebsiteName in content_h3:
                        num = num+1
                        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        # print(current_time)
                        savetodb1(num, WebsiteName.text, current_time)
                        output = (num, WebsiteName.text)
                        print(output, current_time)
                        # csv
                        writeIn = open('BaiduResult.csv', 'a', newline='')
                        csv_write = csv.writer(writeIn, dialect='excel')
                        csv_write.writerow(output)
                        # csv file saved in 'C:\Users\tanglj31\PycharmProjects\project3-4'

                        # excel
                        for j in range(0, len(output)):
                            sheet.write(num, j, output[j])
                    # finish write-in session when all done
                    writeIn.close()
                    # book.save('C:/Users/tanglj31/PycharmProjects/project3-4/baiduResult.xls')
                    print("Result Successfully Saved to Database")
                except Exception:
                    num = num-1
                    print("Result not saved to Database")

                # if(driver.find_element_by_xpath("//*[@id='page']/a[last()]")):
                #     driver.find_element_by_xpath("//*[@id='page']/a[last()]").click()
                # 'nextpage btn' of the nextpage was expected, however, even when current page not flipped, 'nextpage btn' of the current page will still be located. Thus, the following sentence is not properly functioned as expected.
                #     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, '下一页>')))
                try:
                    # the page before clicking next page
                    page1 = driver.find_element_by_link_text('下一页>')
                    page1.click()
                    # the page after clicking next page, could still be page 1 if not fully loaded
                    page2 = driver.find_element_by_link_text('下一页>')
                    # if page1 = page2, meaning page 2 not loaded as expected, if not, exit and start next circulation
                    while (page1 == page2):
                        # refresh page 2 to locate 'nextpage' button every 0.5s within 10s max
                        page2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT,'下一页>')))
                except Exception:
                    print("Searching Timeout")
                    break
                # commit to database to run
                db1.commit()
            print("Searching Completed")

    def db1_initiate():
        try:
            # use execute() to execute SQL，delete table if already existed
            cursor.execute("DROP TABLE IF EXISTS baidu")
            # execute sql sentence， Name title bar as following
            sql = """CREATE TABLE baidu (Num  CHAR(255), WebsiteName  CHAR(255), CurrentTime  CHAR(255))"""
            cursor.execute(sql)
            print("Table Successfully Created")
        except Exception:
            db1.rollback()
            print("Table Not Created")

    def savetodb1(number, name, time1):
        # objects in 'insert into' sentence must be identical with  'Create Table' title bar sentence
        sql = """INSERT INTO baidu(Num, WebsiteName, CurrentTime)
             VALUES ('%s','%s','%s')""" % (number, name , time1)
        try:
            cursor.execute(sql)
        except Exception:
            # rollback when error occurs
            db1.rollback()



# if __name__ == '__main__':
#     showcase = input("Please search keywords:\n")
    db1_initiate()
    # csv
    # open the designated file, create one if not found
    writeIn = open('BaiduResult.csv', 'w', newline='')
    # start write-in mode
    csv_write = csv.writer(writeIn, dialect='excel')
    # name the 1st row
    csv_Header = ["No.", "Headline"]
    # write in the 1st row
    csv_write.writerow(csv_Header)
    writeIn.close()

    # excel
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # create and name a new sheet
    sheet = book.add_sheet('result_page', cell_overwrite_ok=True)
    # name the 1st row as header
    excel_Header = ["No.", "Headline"]
    # write in header orderly
    for k in range(0, len(excel_Header)):
        sheet.write(0, k, excel_Header[k])
    search(keyword)
    db1.close()
# if __name__ == '__main__':
#     baidu("kkk")

# to be solved: database connection pool, multi-threading(not suitable in Selenium-Webdriver)