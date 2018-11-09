from flask import Flask, make_response, send_from_directory
import webdriver
import file_export
app = Flask(__name__)

# search bar
@app.route('/search/<string:keyword>', methods=['GET'])
def search(keyword):
    print(keyword)
    webdriver.baidu(keyword)
    # show 'received' beneath search bar when search page is responsive
    rspns=make_response('received')
    # 跨域请求
    rspns.headers['Access-Control-Allow-Origin']='*'
    return rspns

# @app.route('/download/<string:filename>', methods=['GET','POST'])
# def download(filename):
#     test.export_excel("baidu")
#     if filename=="baiduResult":
#         return send_from_directory('', 'baiduResult.xls', as_attachment=True)
#     else:
#         return send_from_directory('', 'BaiduResult.csv', as_attachment=True)

@app.route('/excel/', methods=['GET', 'POST'])
def excel():
    file_export.export_files("baidu")
    return send_from_directory('', 'baiduResult.xls', as_attachment=True)

@app.route('/csv/', methods=['GET', 'POST'])
def csv():
    file_export.export_files("baidu")
    return send_from_directory('', 'BaiduResult.csv', as_attachment=True)

    # show 'received' beneath search bar when search page is responsive
    # rspns=make_response('received')
    # 跨域请求
    # rspns.headers['Access-Control-Allow-Origin']='*'
    # return rspns

# show file list
# @app.route('/fetch',methods=['GET','POST'])
# def fetch():
#     return

# file download
# @app.route('.download',methods=['GET','POST'])

# @app.route('/search',methods=['POST'])
# def get_keyword():
#     if request.method == 'POST':
#         keyword = request.form['keyword']
#     baidu.baidu_search(keyword)
#     return send_from_directory('','hh.xls')

if __name__ == '__main__':
    app.run()