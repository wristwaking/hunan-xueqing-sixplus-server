## 湖南大学 XUEQING PLUS.6 英语问卷调研机器人服务器端
湖南大学英语问卷调研chat-6升级版机器人服务器端源码。通过openai大模型实现会话持久型问答功能。通过mongodb数据库实现会话数据持久化存储。
github 仓库地址：https://github.com/wristwaking/hunan-xueqing-chat-server.git

## 服务器配置信息
```
http://81.69.248.158/
系统账号：root
系统密码：mahaocheng
宝塔账号：edgehacker
宝塔密码：linenazi1314520
```

## 配置 mongodb 数据库
```python
mongodb 数据库：xueqing
mongodb 数据库 用户：xueqing
```

## nginx 配置路由
```nginx configuration
location / {
  try_files $uri $uri /index.html;
}

location /server/ {  
    proxy_pass http://localhost:3006/;  
    proxy_set_header Host $host;  
    proxy_set_header X-Real-IP $remote_addr;  
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  
    proxy_set_header X-Forwarded-Proto $scheme;  
}
```

## 配置千帆大模型 v2
API_KEY 配置地址：https://console.bce.baidu.com/iam/#/iam/apikey/list

```
模型名称	模型版本	model 参数值	是否支持function call功能	是否支持web_search
ERNIE X1	ERNIE-X1-32K	ernie-x1-32k	否	否
ERNIE X1	ERNIE-X1-32K-Preview	ernie-x1-32k-preview	否	否
ERNIE 4.5	ERNIE-4.5-8K-Preview	ernie-4.5-8k-preview	否	是
ERNIE 4.0	ERNIE-4.0-8K-Latest	ernie-4.0-8k-latest	是	是
ERNIE 4.0	ERNIE-4.0-8K-Preview	ernie-4.0-8k-preview	是	是
ERNIE 4.0	ERNIE-4.0-8K	ernie-4.0-8k	是	是
ERNIE 4.0 Turbo	ERNIE-4.0-Turbo-8K-Latest	ernie-4.0-turbo-8k-latest	是	是
ERNIE 4.0 Turbo	ERNIE-4.0-Turbo-8K-Preview	ernie-4.0-turbo-8k-preview	是	是
ERNIE 4.0 Turbo	ERNIE-4.0-Turbo-8K	ernie-4.0-turbo-8k	是	是
ERNIE 4.0 Turbo	ERNIE-4.0-Turbo-128K	ernie-4.0-turbo-128k	是	是
Llama-4-Maverick	Llama-4-Maverick-17B-128E-Instruct	llama-4-maverick-17b-128e-instruct	否	否
Llama-4-Scout	Llama-4-Scout-17B-16E-Instruct	llama-4-scout-17b-16e-instruct	否	否
ERNIE 3.5	ERNIE-3.5-8K-Preview	ernie-3.5-8k-preview	是	是
ERNIE 3.5	ERNIE-3.5-8K	ernie-3.5-8k	是	是
ERNIE 3.5	ERNIE-3.5-128K	ernie-3.5-128k	是	是
ERNIE Speed	ERNIE-Speed-8K	ernie-speed-8k	否	否
ERNIE Speed	ERNIE-Speed-128K	ernie-speed-128k	否	否
ERNIE Speed	ERNIE-Speed-Pro-128K	ernie-speed-pro-128k	是	否
ERNIE Lite	ERNIE-Lite-8K	ernie-lite-8k	否	否
ERNIE Lite	ERNIE-Lite-Pro-128K	ernie-lite-pro-128k	是	否
ERNIE Tiny	ERNIE-Tiny-8K	ernie-tiny-8k	否	否
ERNIE Character	ERNIE-Character-8K	ernie-char-8k	否	否
ERNIE Character	ERNIE-Character-Fiction-8K	ernie-char-fiction-8k	否	否
ERNIE-Novel-8K	ERNIE-Novel-8K	ernie-novel-8k	否	否
DeepSeek-V3	DeepSeek-V3-250324	deepseek-v3	否	否
DeepSeek-V3	DeepSeek-V3-241226	deepseek-v3-241226	否	否
DeepSeek-Reasoner	DeepSeek-R1	deepseek-r1	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Qwen-32B	deepseek-r1-distill-qwen-32b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Qwen-14B	deepseek-r1-distill-qwen-14b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Qwen-7B	deepseek-r1-distill-qwen-7b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Qwen-1.5B	deepseek-r1-distill-qwen-1.5b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Llama-70B	deepseek-r1-distill-llama-70b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Llama-8B	deepseek-r1-distill-llama-8b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Qianfan-Llama-70B	deepseek-r1-distill-qianfan-llama-70b	否	否
DeepSeek-R1-Distill	DeepSeek-R1-Distill-Qianfan-Llama-8B	deepseek-r1-distill-qianfan-llama-8b	否	否
QwQ-32B	QwQ-32B	qwq-32b	否	否
```


常见问题
```
qianfan.errors.APIError: api return error, req_id: as-rs1tupzce1 code: invalid_appId, msg: No permission to use the appId
```
解决方案：配置千帆 ModelBuilder API_KEY 选择全部资源

```python
from qianfan import Qianfan

client = Qianfan(
    # 方式一：使用安全认证AK/SK鉴权
    # 替换下列示例中参数，安全认证Access Key替换your_iam_ak，Secret Key替换your_iam_sk，如何获取请查看https://cloud.baidu.com/doc/Reference/s/9jwvz2egb
    # access_key="your_iam_ak",
    # secret_key="your_iam_sk",
    # app_id="", # 选填，不填写则使用默认appid

    # 方式二：使用API Key值鉴权
    # 替换下列示例中参数，your_APIKey，如何获取API Key请查看https://cloud.baidu.com/doc/WENXINWORKSHOP/s/Um2wxbaps#步骤二-获取api-key
    api_key="bce-v3/ALTAK-PmM6xUgp4CAq1zYbZ4734/264a6bea31eb365949d79e2d82c6616621914e4c",
    app_id="app-WOxYkh15"  # 选填，不填写则使用默认appid
)

# completion = client.chat.completions.create(
#     model="ernie-3.5-8k",  # 指定特定模型
#     messages=[
#         {'role': 'system', 'content': '平台助手'},
#         {'role': 'user', 'content': '你好'}
#     ],
#     stream=True
# )

# for r in completion:
#     print(r)

completion = client.chat.completions.create(
    model="ernie-3.5-8k",  # 指定特定模型
    messages=[
        {'role': 'system', 'content': '平台助手'},
        {'role': 'user', 'content': '你好'}
    ]
)

print(completion)
```

## 环境安装

创建 requirements.txt
```
pipreqs . --encoding==utf8 --force
INFO: Not scanning for jupyter notebooks.
WARNING: Import named "Flask" not found locally. Trying to resolve it at the PyPI server.
WARNING: Import named "Flask" was resolved to "Flask:3.1.0" package (https://pypi.org/project/Flask/).
Please, verify manually the final list of requirements.txt to avoid possible dependency confusions.
WARNING: Import named "openai" not found locally. Trying to resolve it at the PyPI server.
WARNING: Import named "openai" was resolved to "openai:1.75.0" package (https://pypi.org/project/openai/).

```
服务器端安装依赖
```
pip install -r requirements.txt
```


## 常见部署环境问题

`AttributeError: module 'pyarrow' has no attribute '__version__'` 这个错误表明你尝试从 `pyarrow` 模块中访问一个不存在的属性 `__version__`。通常情况下，Python 的库和模块会提供一个 `__version__` 属性来查询它们的版本号，但 `pyarrow` 模块可能没有直接暴露这个属性。

**更新 `pyarrow`**

```bash
pip install --upgrade pyarrow
```