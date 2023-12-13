#---WINDOWS STARTING----###########################
import tkinter as tk
from tkinter import PhotoImage
# import request#####################################################
#----WINDOWS LOOP AND POPPING OUT
windows=tk.Tk()
windows.title("TRACKING E-TECH")
windows.geometry("450x695")
 # -----DEF FUCTION FOR IPTRACKER---#
def ip_tracker():
    import requests

    IPAddress = str(entry.get())
    api_Key = "at_04UW5XsImL3dM8a1OWvjtNLR3wOzC"
    url = f"https://geo.ipify.org/api/v2/country,city?apiKey=at_04UW5XsImL3dM8a1OWvjtNLR3wOzC&ipAddress={IPAddress}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # print(data)

        a = data.get('ip')
        b = data.get('location')
        c = b.get('lat')
        d = b.get('lng')
        e = b.get('country')
        f = b.get('region')
        g = b.get('city')
        h = b.get('timezone')
        i = b.get('geonameId')
        # print(f"This is the Location of the IP: {b}")
        ai=(f"This is the IP address: {a}\n")
        ci=(f"This is the Lat: {c}\n")
        di=(f"This is the lng: {d}\n")
        ei=(f"This is the Country: {e}\n")
        fi=(f"This is the Region: {f}\n")
        gi=((f"This is the City: {g}\n"))
        hi=(f"This is the Timezone of the IP: {h}\n")
        ii=(f"This is the GeonameID of the IP: {i}\n")

        # IP = data.get("as")
        # ip = IP.get('domain')
        # route = IP.get('route')
        # name = IP.get('name')
        #
        # ipi=(f"This is the Domain of the IP {ip}\n")
        # routei=(f"This is the Route of the IP {route}\n")
        # namei=(f"This the name of the IP {name}\n")

        return ai+ci+di+ei+fi+gi+hi+ii

    elif response.status_code == 404:
        print("This APi page is having some issues")

    else:
        print("Invalid Input")


def tracker_display():
    greeting=ip_tracker()
    #---THE TEXT FIELD WHERE THE TEXT WILL BE DISPLAYED---########################gf
    greeting_display= tk.Text(master= windows,height=21,width=45,fg="Green")
    greeting_display.grid(column=0,row=13)
    greeting_display.insert(tk.END, str(greeting))

def Voice():
    import pyttsx3 as pk
    voicee=ip_tracker()
    engine = pk.init()
    engine.say(f"{voicee}")
    engine.runAndWait()


def Geolocation():
    from geopy.geocoders import Nominatim
    # Create a geocoder instance
    geolocator = Nominatim(user_agent="my_app")

    lat = str(ientry.get())
    log = str(iiientry.get())

    # Reverse geocode coordinates
    location = geolocator.reverse(f"{lat} ,{log}")  # latitude, longitude

    # Extract address information
    address = location.raw['address']
    tourism = address.get("tourism")
    road = address.get("road")
    suburb = address.get("suburb")
    state= address.get("state")

    aa=f"{suburb} is the suburb of the device\n"
    bb=f"{road} the road of the device\n"
    cc=f"{tourism} is the tourism of the device\n"
    dd=f"{state} is the state of the device\n"

    return aa+bb+cc+dd

    # Print address details
    # print(address)
def outputgeo():
    output = Geolocation()
    # ---THE TEXT FIELD WHERE THE TEXT WILL BE DISPLAYED---########################gf
    output_display = tk.Text(master=windows, height=21, width=55, fg="Green")
    output_display.grid(column=0, row=13)
    output_display.insert(tk.END, str(output))

def voicegeo():
    import pyttsx3 as pk
    vocals = Geolocation()
    engine = pk.init()
    engine.say(f"{vocals}")
    engine.runAndWait()

# #---PICTURE OF THE SOFTWARE---#######################
logo = PhotoImage(file="images.png")
logo_label = tk.Label(image=logo)
logo_label.grid(column=0,row=0)

#---LABEL OF THE THE SOFTWARE---###############################
label=tk.Label(text="Kindly Note if you use this software illegally you can be tracked\n"
                    "Kindly input the user! IP-ADDRESS for tracking\n",fg="RED")
label.grid(column=0,row=1)

iiientrylabel = tk.Label(text="IP-ADDRESS:",fg="Green")
iiientrylabel.grid(column=0, row=2)

entrylabel = tk.Label(text="LATITUDE:", fg="Green")
entrylabel.grid(column=0, row=4)

entrylabelx = tk.Label(text="LONGITUDE:", fg="Green")
entrylabelx.grid(column=0, row=7)
#

#-----ENTRY----#---JUST LIKE A USER INPUT BOX---##########################
entry=tk.Entry()
entry.grid(column= 0,row=3)
#----SECOND ENTRY FOR THE LAT AND LOG GEOLOCATION---#########################
ientry=tk.Entry()
ientry.grid(column=0,row=5)
#----THIRD ENTRY-----#
iiientry=tk.Entry()
iiientry.grid(column=0,row=8)


#----BUTTONS OF THE CODE----#
ibuttons=tk.Button(text="IP TRACKER",command = tracker_display,fg="Light Green",bg="Black")
ibuttons.grid(column=0,row=9)

iibuttons=tk.Button(text="Voice for IP",bg="Yellow",fg="Blue",command=Voice)
iibuttons.grid(column=0,row=10)

buttonss=tk.Button(text="GEO-LOCAION",bg="Green",fg="Black",command=outputgeo)
buttonss.grid(column=0,row=11)

ubuttons=tk.Button(text="Voice for GEO",bg="Yellow",fg="Blue",command=voicegeo)
ubuttons.grid(column=0,row=12)

#----TO KEEP THE WINDOWS OUT SO IT WON'T JUST POP ONCE LET THE WINDOWS KEEP LOOPING---###########
windows.mainloop()


