## qianfan~=0.3.7.1

import qianfan
import dotenv

dotenv.load_dotenv()
chat_comp = qianfan.ChatCompletion()

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
    resp = chat_comp.do(model="ERNIE-Bot-4", messages=messages, system=is_emoji_system(is_emoji))
    if resp.code == 200:
        return resp.body.get("result")
    else:
        return False


def analysis_model(history_chat_data, is_emoji, user_id):
    messages = [{
        "role": "user",
        "user_id": user_id,
        "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请问简要评价我的最新那条回答的回答情况，进行分析下英语语法和回答质量！"
    }] + history_chat_data
    resp = chat_comp.do(model="ERNIE-Bot-4", messages=messages, system=is_emoji_system(is_emoji))
    if resp.code == 200:
        return resp.body.get("result")
    else:
        return False


if __name__ == "__main__":
    history = []
    result = ask_model(history_chat_data=history, is_emoji=True, user_id="test")
    print(result)
    # print(qianfan_ask("问题；What is the past tense of the verb “to run”?, 我的回答：run。请问简要评价我的回答情况，带有许多emoji表情"))
