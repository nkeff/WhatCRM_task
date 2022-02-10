from base64 import b64decode
import json
import time
import requests

from config import Config

config = Config()


requests_counter = 0
while True:

    # Ищем свободный чат
    get_chat_url = f"{config.base_url}chat/spare?crm=TEST&domain=test"
    get_chat_response = requests.request("GET", get_chat_url, headers=config.headers)


    # обработка ошибок
    if get_chat_response.status_code == 200 and not get_chat_response.json().get('error_code'):
        config.save_chat_info(json.dumps(get_chat_response.json(), indent=1))
    else:
        if requests_counter > 20:
            print("timeout error")
            exit()

        requests_counter += 1
        print(get_chat_response.json())
        time.sleep(5)
        continue
    

    requests_counter = 0
    # Инициализируем чат
    init_chat_url = f"{config.base_url}instance{config.instance}/status?token={config.token}"
    init_chat_response = requests.request("GET", init_chat_url, params=config.params, headers=config.headers)

    print('counter:', requests_counter, '| status:', init_chat_response.json().get('state'))
    
    if init_chat_response.json().get('state') == 'got qr code':
        config.save_qr_code(init_chat_response.get('qrCode')) 

    requests_counter += 1
    if requests_counter > 10:
        print("timeout error")
        exit()
    time.sleep(5)


# сохраняем картинку qr кода
with open('qr.png', 'bw') as f:
    f.write(b64decode(config.QR_code.split(',')[1]))

print("image 'qr.png' saved!")