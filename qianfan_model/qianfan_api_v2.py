from qianfan import Qianfan
import dotenv

dotenv.load_dotenv()
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

system = "结果用纯英语返回，不带有任何中文，内容不超过100个词。"


def is_emoji_system(is_emoji):
    if is_emoji:
        return system + "带有许多emoji表情，穿插在文字中。"
    else:
        return system


def ask_model(history_chat_data, is_emoji, user_id):
    messages = [{
        "role": "user",
        "user_id": user_id,
        "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请根据我们的问答历史，提问新的问题！"
    }] + history_chat_data
    completion = client.chat.completions.create(model="ernie-4.0-8k", messages=messages, system=is_emoji_system(is_emoji))
    return completion.choices[0].message.content


def analysis_model(history_chat_data, is_emoji, user_id):
    messages = [{
        "role": "user",
        "user_id": user_id,
        "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请问简要评价我的最新那条回答的回答情况，进行分析下英语语法和回答质量！"
    }] + history_chat_data
    completion = client.chat.completions.create(model="ernie-4.0-8k", messages=messages, system=is_emoji_system(is_emoji))
    return completion.choices[0].message.content


if __name__ == "__main__":
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

    completion = client.chat.completions.create(
        model="ernie-4.0-8k",  # 指定特定模型
        messages=[
            {'role': 'system', 'content': '平台助手'},
            {'role': 'user', 'content': '你好'}
        ]
    )

    print(completion.choices[0].message.content)