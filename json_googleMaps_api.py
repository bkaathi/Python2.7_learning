import requests

while 1:
    address = raw_input("Address: ")
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    param = {'address': address, 'key': ''}
    json_data = requests.get(url, param).json()
#    print json_data

    json_status = json_data["status"]
    if json_status == 'OK':
        print "API Status: " + json_status
        full_address = json_data["results"][0]["formatted_address"]
        print "Full Address: " + str(full_address)
        for each in json_data["results"][0]["address_components"]:
            print each["long_name"]

        latitude = json_data["results"][0]["geometry"]["location"]["lat"]
        longitude = json_data["results"][0]["geometry"]["location"]["lng"]

        print "Latitude: " + str(latitude)
        print "Longitude: " + str(longitude)




















'''
while 1:
    address = raw_input("Address: ")
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + address
    print url
    json_data = requests.get(url).json()
#     print json_data

 geo_s ='https://maps.googleapis.com/maps/api/geocode/json'
 
    param = {'address': address, 'key': 'YOUR_KEY'}

    response = requests.get(geo_s, params=param)

'''
