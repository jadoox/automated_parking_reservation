import requests
import configparser
from pprint import pprint
from datetime import datetime

config = configparser.ConfigParser()
config.read('.config.ini')
URL_DISC = config['default']['URL']

url_disc= URL_DISC
url_disc = url_disc.split(',')

try:

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    for gata in url_disc:
        req = requests.get(gata)

        if "Registreringsnummer" in req.text:
            print("parkering tillganglig")
            f = open("rydsvagenlog.txt", "a")
            f.write(str(dt_string) + " parkering tillgänglig\n")
            f.close()
            requests.post(url_disc, data = {"content": "NU FINNS PARKERING I RYD!"})

        else:
            print("parkering ej tillganglig")
            f = open("rydsvagenlog.txt", "a")
            f.write(str(dt_string) + " parkering EJ tillgänglig\n")
            f.close()

except Exception as e:
    print(e)
