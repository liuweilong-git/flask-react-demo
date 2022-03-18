from flask import Flask, request
import config
import json

app = Flask(__name__)

app.config.from_object(config)


#api接口前缀
apiPrefix = '/api/v1/'


@app.route(apiPrefix + 'updateStaff', methods=['POST'])
def updateStaff():
    data = request.get_data(as_text=True)
    # re = DBUtil.addOrUpdateStaff(data)
    # if re['code'] >= 0: # 数据保存成功，移动附件
    #     FileUtil.fileMoveDir(re['id'])
    re ={"code":0}
    return json.dumps(re)
    # return 'Hello World!'


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!！'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
