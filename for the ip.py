import requests

IPAddress=input("Enter your IP-Address:")
api_Key="at_04UW5XsImL3dM8a1OWvjtNLR3wOzC"
url=f"https://geo.ipify.org/api/v2/country,city?apiKey=at_04UW5XsImL3dM8a1OWvjtNLR3wOzC&ipAddress={IPAddress}"

response=requests.get(url)

if response.status_code == 200:
    data=response.json()
    # print(data)

    a=data.get('ip')
    b=data.get('location')
    c=b.get('lat')
    d=b.get('lng')
    e=b.get('country')
    f=b.get('region')
    g=b.get('city')
    h=b.get('timezone')
    i=b.get('geonameId')
    # print(f"This is the Location of the IP: {b}")
    print(f"This is the IP address: {a}")
    print(f"This is the Lat: {c}")
    print(f"This is the lng: {d}")
    print(f"This is the Country: {e}")
    print(f"This is the Region: {f}")
    print((f"This is the City: {g}"))
    print(f"This is the Timezone of the IP: {h}")
    print(f"This is the GeonameID of the IP: {i}")

    IP=data.get("as")
    ip=IP.get('domain')
    route=IP.get('route')
    name=IP.get('name')

    print(f"This is the Domain of the IP {ip}")
    print(f"This is the Route of the IP {route}")
    print((f"This the name of the IP {name}"))

elif response.status_code == 404:
    print("This APi page is having some issues")

else:
    print("Invalid Input")