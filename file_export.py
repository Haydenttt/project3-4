import pymysql
import configparser
import csv
import xlwt
import codecs

def export_files(c):
    cf = configparser.ConfigParser()
    cf.read("sqlconfig.conf")
    host = cf.get("db", "host")
    user = cf.get("db", "user")
    password = cf.get("db", "password")
    db_name = cf.get("db", "database")
    port = cf.get("db", "port")
    con = pymysql.connect(host=host, user=user, password=password, db=db_name, port=int(port))
    cursor = con.cursor()
    sql = 'select * from %s' % c
    cursor.execute(sql)
    fileds = [filed[0] for filed in cursor.description]
    all_data = cursor.fetchall()
    book = xlwt.Workbook()
    sheet = book.add_sheet('baiduResult')
    for col, field in enumerate(fileds):
        sheet.write(0, col, field)
        row = 1
    for data in all_data:
        for col, field in enumerate(data):
            sheet.write(row, col, field)
        row += 1
    book.save('C:/Users/tanglj31/PycharmProjects/project3-4/baiduResult.xls')

    with codecs.open('baidu.csv', 'w', 'utf-8') as out:
        csv_write = csv.writer(out, dialect='excel')
        csv_Header = ["num", "title"]
        csv_write.writerow(csv_Header)
        for data in all_data:
            csv_write.writerow(data)
        out.close()