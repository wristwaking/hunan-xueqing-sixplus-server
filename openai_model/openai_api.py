import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key="bacai-eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2JpbGUiOiIxNTUwNTEwMTU1MCIsImV4cCI6MTcyMDgwODc2MDgzOCwiaWF0IjoxNzE3Njg2Njk2fQ.iw2xJK2USf-oodl1XVhWU342oPpnfqWi1SsF9kXpIUs",
    base_url="https://api.baicaigpt.com/v1"
)


def ask_model(history_chat_data, is_emoji, user_id):
    if is_emoji:

        messages = [{
            "role": "user",
            "user_id": user_id,
            "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请根据我们的问答历史，提问新的问题！(结果用纯英语返回，不带有任何中文，带有许多emoji表情，穿插在文字中，内容不超过100个词。)"
        }] + history_chat_data
    else:
        messages = [{
            "role": "user",
            "user_id": user_id,
            "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请根据我们的问答历史，提问新的问题！(结果用纯英语返回，不带有任何中文，内容不超过100个词。)"
        }] + history_chat_data

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    print(response)
    return response.choices[0].message.content


def analysis_model(history_chat_data, is_emoji, user_id):
    if is_emoji:
        messages = [{
            "role": "user",
            "user_id": user_id,
            "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请问简要评价我的最新那条回答的回答情况，进行分析下英语语法和回答质量！(结果用纯英语返回，不带有任何中文，带有许多emoji表情，穿插在文字中，内容不超过100个词。)"
        }] + history_chat_data
    else:
        messages = [{
            "role": "user",
            "user_id": user_id,
            "content": "现在我要进行一场英语测试，你是提问者，我是回答者！请问简要评价我的最新那条回答的回答情况，进行分析下英语语法和回答质量！(结果用纯英语返回，不带有任何中文，内容不超过100个词。)"
        }] + history_chat_data
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    print(response)
    return response.choices[0].message.content

if __name__ == "__main__":
    history = []
    result = ask_model(history_chat_data=history, is_emoji=True, user_id="test")
    print(result)
