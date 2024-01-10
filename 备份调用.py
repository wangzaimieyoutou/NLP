
import json
import re
import time
import pandas as pd
import requests
from tqdm import tqdm

import config

def s_QA(text,qt):
    try:
        token = "****"
        url = "https://api.zhishuyun.com/chatgpt4-browsing?token="
        headers = {
            "content-type": "application/json"
        }
        promt = "你好，你是一个客服，下面我会给你一段企业网银业务的客服对话，对话内容如下：\n"
        payload = {
            "question": promt +qt+text,
            "stateful": False
        }
        response = requests.post(url + token, json=payload, headers=headers)
        res = json.loads(response.text)
        r = res['answer']
        r = re.sub(config.blank_row_pattern, '\n', r)
        r = r.replace(" ", "")
        return r
    except Exception as e:
        return "GPT4服务异常！！！！" + str(e)


# texts=pd.read_csv('qt.txt')
# text=str(texts)
# a=s_QA(text)
# print(a)
def bach_tt():
    qt=pd.read_csv('qt.txt')
    load_path = "train.xlsx"
    save_path = "id_res_key.xlsx"
    data = pd.read_excel(load_path)
    texts = list(data["对话内容"])
    res = []
    for text in tqdm(texts):
        res.append(s_QA(text,qt))


    data["GPT4生成结果"] = res
    data.to_excel(save_path, index=False)

# text=pd.read_csv('qt.txt')
# qt=pd.read_csv('text_train.txt')
# text=str(text)
# qt=str(qt)
# a=s_QA(text,qt)
# print(a)
if __name__ == '__main__':
    bach_tt()
    a=bach_tt()
    print(a)
    #bach_tt(text)
    # text = "0"
    # res = s_key(text)
    # print(res.strip())
    # r = s_tt(text)
    # print(r)