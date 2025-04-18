import json
from datetime import datetime

from bson import ObjectId
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_pymongo import PyMongo

import problem_init
import qianfan_api
from read_data import PROBLEM_LIST, XING_PROBLEM_LIST, XUE_PROBLEM_LIST, WEI_PROBLEM_LIST, KUA_PROBLEM_LIST

import pandas as pd
import io
from openpyxl import Workbook

app = Flask(__name__)
CORS(app)

# 配置 MongoDB 连接
app.config['MONGO_URI'] = 'mongodb://localhost:27017/hnu'
mongo = PyMongo(app)


# print(PROBELM_LIST)

def generate_excel(data):
    # 创建一个 Excel 工作簿和工作表
    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    # 将数据写入工作表
    for row_num, row_data in enumerate(data, 1):
        ws.append(row_data)

        # 将工作簿保存到 BytesIO 流中
    excel_data = io.BytesIO()
    wb.save(excel_data)
    excel_data.seek(0)  # 重置流的位置到开头

    # 设置 HTTP 响应头，以便浏览器知道这是一个 Excel 文件
    response = make_response(excel_data.read())
    response.headers["Content-Disposition"] = "attachment; filename=data.xlsx"
    response.headers["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    return response


def insert_mongo_data(user: str, content: str):
    collection = mongo.db.message
    # 获取当前日期和时间
    now = datetime.now()
    # 格式化日期和时间
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    collection.insert_one({'time': formatted_time, 'user': user, 'content': content})  #


@app.route('/json', methods=['GET'])
def get_data():
    # 查询 MongoDB
    data = mongo.db.message.find()
    # 将 ObjectId 转换为字符串
    result = []
    for d in data:
        # 处理ObjectId
        d['_id'] = str(d['_id'])
        result.append(d)
    return jsonify(result)


@app.route('/excel', methods=['GET'])
def get_data_excel():
    data = mongo.db.message.find()
    # 将 ObjectId 转换为字符串
    result = []
    for d in data:
        # 处理ObjectId
        d['_id'] = str(d['_id'])
        result.append(d)
    # 将查询结果转换为 DataFrame
    df = pd.DataFrame(result)
    # 生成 Excel 文件并返回
    return generate_excel(df.values.tolist())


@app.route('/problem', methods=['POST'])
def randon_problem():
    # index = int(request.args.get('index'))
    # problem = random.choice(PROBELM_LIST)
    data = request.get_json()
    user_id = data.get('user_id', "")
    index = data.get('index', "")
    subject = data.get('subject', "")
    history = data.get("history", [])
    emoji = data.get('emoji', False)

    if not history:
        problem = problem_init.init_problem(subject)
    else:
        problem = qianfan_api.ask_model(history, emoji, user_id)
    # if subject == "学校生活与学术讨论":
    #     problem = XUE_PROBLEM_LIST[index % len(XUE_PROBLEM_LIST)]
    # elif subject == "兴趣爱好与日常活动":
    #     problem = XING_PROBLEM_LIST[index % len(XING_PROBLEM_LIST)]
    # elif subject == "跨文化交流与观点分享":
    #     problem = KUA_PROBLEM_LIST[index % len(KUA_PROBLEM_LIST)]
    # elif subject == "未来规划与职业发展":
    #     problem = WEI_PROBLEM_LIST[index % len(WEI_PROBLEM_LIST)]
    # else:
    #     # 题目循环取余操作
    #     problem = PROBLEM_LIST[index % len(PROBLEM_LIST)]
    # 记录机器人数据
    result = {'code': 200, 'data': problem}
    return jsonify(result)


@app.route('/answer', methods=['POST'])
def answer_problem():
    data = request.get_json()
    user_id = data.get('user_id', "")
    problem = data.get('problem', "")
    answer = data.get('answer', "")
    history = data.get('history', [])
    emoji = data.get('emoji', False)
    # 记录使用者数据
    # 千帆大模型分析回答质量
    analysis = qianfan_api.analysis_model(history, emoji, user_id)
    # 记录机器人数据
    result = {'code': 200, 'data': analysis}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)

"""
this.answer
http://hnu.willwaking.com/server

http://hnu.willwaking.com/server

http://192.168.0.104:3000

"""
