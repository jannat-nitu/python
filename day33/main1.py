from datetime import datetime
import requests
import smtplib
import time
lat = 51.919437
lang = 19.145136
my_email = "jnitu7227@gmail.com"
password = "zdherbajjbfxoypr"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if lat - 5 <= iss_latitude <= lat +5 and lang - 5 <= iss_longitude <= lang + 5:
        return True

def is_night():
    parameters = {
        "lat": lat,
        "lng": lang,
        "formatted": 0
    }

    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)

    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)

    time = datetime.now().hour
    if time >= sunset or time <=sunrise:
        return True
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="cushantanu@gmail", 
            msg="Subject:Look up\n\nThe ISS is above you in the sky.")