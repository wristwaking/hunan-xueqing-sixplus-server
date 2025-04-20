from openai import OpenAI
import dotenv

dotenv.load_dotenv(".env")

client = OpenAI(
    api_key="sk-iPyYij2RCiphfjkt5601827cD5914916A99a047e0d010627",
    base_url="https://api.xiaoai.plus/v1"
)


def chat_answer(model, content):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": content}
        ]
    )
    return {"result": response.choices[0].message.content, "token": response.usage.total_tokens}


if __name__ == "__main__":
    print(chat_answer("gpt-4", "你好"))
