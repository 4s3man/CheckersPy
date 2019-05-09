import urllib.request
from ast import literal_eval
import json

def captcha_is_ok(request):
    secret_key = "6LfQTqIUAAAAANVt8PZn2kP5Oqz99mk8mt8zITWh"
    captcha = request.form.get('g-recaptcha-response')
    server_ip = request.host.split(':')[0]
    response = urllib.request.urlopen("https://www.google.com/recaptcha/api/siteverify?secret=" + secret_key + "&response=" + captcha + "&remoteip=" + server_ip).read(1000)
    try:
        return json.loads(response.decode("utf-8")).get('success', 0) == 1
    except Exception:
        print('exception')
        return False
