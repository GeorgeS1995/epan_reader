import logger
import configuration
import requests
from requests.auth import HTTPBasicAuth
import xmlparser
import pyperclip
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

lh = logger.log_init()
cfg = configuration.Props()
lh.info("start epan reader")

cfg.load()
lh.debug("load config")
ssl = cfg.get_ssl()
user = cfg.get_login()
password = cfg.get_password()
addr = cfg.getAddress()
port = cfg.get_port()
if cfg.get_ssl() == '':
    ssl = False
    lh.warning("ssl check disabled")
r_url = "https://{}:{}/TicketClassificationWebService/ticket-classification".format(addr, port)

while True:
    barcode = input("Enter barcode: ")

    r_param = {"requestid": 0, "barcode": barcode}
    try:
        response = requests.get(r_url, params=r_param, auth=HTTPBasicAuth(user, password), verify=ssl)
        response.raise_for_status()
    except requests.exceptions.ReadTimeout:
        lh.error("request read timeout")
        continue
    except requests.exceptions.ConnectTimeout:
        lh.error("request connection timeout")
        continue
    except requests.exceptions.ConnectionError as err:
        lh.error("connection error: {}".format(err))
        continue
    except requests.exceptions.HTTPError as err:
        lh.error("HTTP error. {}".format(err))
        continue
    except requests.exceptions as err:
        lh.error("Unhandled error: {}", err)
        continue
    xml = xmlparser.request_parser(response.content)
    try:
        lh.info("epan successfuly read and add to clipboard \n epan: {}".format(xml["epan"]))
        pyperclip.copy(xml["epan"])
    except KeyError as err:
        lh.error("epan not founc. xml: {}".format(err))