import time
from hashlib import md5

import requests

phone = "12345678910"


def send():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://xc.caict.ac.cn',
        'Connection': 'keep-alive',
        'Referer': 'https://xc.caict.ac.cn/',
        'Sec-Fetch-Dest': 'empty',  # noqa
        'Sec-Fetch-Mode': 'cors',  # noqa
        'Sec-Fetch-Site': 'same-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    p090983d = phone
    s324234m = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    s234234s = md5(("MOFXTCJq8bOhlSi" + s324234m).encode()).hexdigest()  # noqa
    q435434f = md5(s324234m.encode()).hexdigest()
    json_data = {
        'p090983d': p090983d,
        's324234m': s324234m,
        's234234s': s234234s,
        'q435434f': q435434f,
    }

    response = requests.post('https://xcweb02.caict.ac.cn:8088/dYvFMYL8/h8A2xuUsHKoMz', headers=headers, json=json_data)

    print(response.text)


if __name__ == "__main__":
    while True:
        try:
            send()
        except Exception as e:
            print(e)
        time.sleep(90)
