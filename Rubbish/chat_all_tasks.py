from semantic_kernel.Rubbish.testwordtoyuyin import text_to_speech, API_KEY, SECRET_KEY


messages = [
    {"role": "system", "content":
"""
    你是一个老人陪护机器人，你的名字叫“大白”。你正在与一位中国独居老人聊天。
    要求：
    一、你需要根据与这位独居老人聊天，请你学会倾听，顺着老人的思路与他聊天，缓解这位老人的孤独感，提高这位老人的幸福感。同时，你有责任根据老人的基本情况给老人一些健康的生活建议。

    二、由于老人比较习惯与老人聊天，请你模仿一位老头的语气与这位老人聊天，并尽量成为老人的朋友。
    注意：
    1.由于老人理解能力有限，请以短句输出回答，要求回答结果在30字以内。
    2.请你以倾听和回答老人为重，不要过多发挥主观能动性。
"""}
]



def chat_langchain(input):
    global status
    status=1 #表示说话
    messages.append({"role": "user", "content": input})
    from semantic_kernel.语音对讲.hey_siri import LLm
    LLm.chat(messages)


def chat_agent(input):
    messages.append({"role": "user", "content": input})


def chat_usual(input):
        global status
        status = 1  # 表示说话
        from zhipuai import ZhipuAI
        client = ZhipuAI(api_key="")  # 填写您自己的APIKey
        messages.append({"role": "user", "content": input})
        response = client.chat.completions.create(
            model="glm-4",  # 填写需要调用的模型名称
            messages=messages
        )
        result = response.choices[0].message.content
        print("回答为：" + result)
        text_to_speech(result, API_KEY, SECRET_KEY)