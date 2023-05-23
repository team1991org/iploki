import requests

logo = '''
  .____                                       .__        
|    |   _____    _____   ___________  _____|__|_______
|    |   \__  \  /     \_/ __ \_  __ \/ ____/  \___   /
|    |___ / __ \|  Y Y  \  ___/|  | \< <_|  |  |/    /   İPLOOKUP TOOL
|_______ (____  /__|_|  /\___  >__|   \__   |__/_____ \     By Lamer Qız / @h3art_exe
        \/    \/      \/     \/          |__|        \/
'''

print(logo)



ip_address = input("Please enter an IP address (If you leave it blank, your own IP address will be used.): ")
if ip_address == "":
    response = requests.get("https://ipinfo.io/json")
else:
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")

if response.status_code != 200:
    print("Failed to get IP address information.  Please check the IP address.")
else:
    data = response.json()
    print(f"IP adress: {data['ip']}")
    print(f"Location:{data['loc']}")
    print(f"Country: {data['country']}")
    print(f"City: {data['city']}")
    print(f"Internet Service Provider: {data['org']}")
