import urllib
import random

orderid = random.randint(1,99999999999)
data = urllib.urlencode({"consumer_key":"1234:1234","amount":"1000","email":"info@mail.com","name":"buyer","orderid":orderid,"callback":"http://127.0.0.1/simple/callback.php","mobile":"09120000000","description":"Description"})
#u = urllib.urlopen("http://192.168.1.42/fuck.php", data)
u = urllib.urlopen("http://rashapay.com/srv/rest/rpaypaymentrequest", data)

read =u.read()
print(read)
