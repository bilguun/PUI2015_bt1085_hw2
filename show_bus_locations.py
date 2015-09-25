import sys
import os
import json
import datetime
import urllib
import unicodecsv

if __name__ == '__main__':
    url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json"
    params = {}
    params['key'] = sys.argv[1]
    params['LineRef'] = sys.argv[2]
    params['VehicleMonitoringDetailLevel'] = 'calls'
    url_values = urllib.urlencode(params)

    response = urllib.urlopen(url + "?" + url_values)
    data = json.loads(response.read())

    print("Bus Line : %s" % (params['LineRef']))
    vehicleActivity = data['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']

    numberOfBuses = len(vehicleActivity)
    print("Number of Active Buses : %s" % (numberOfBuses))

    for i in range(0, numberOfBuses):
        print("Bus %s is at latitude %s and longitude %s" %
              (i,
               vehicleActivity[i]['MonitoredVehicleJourney'][
                   'VehicleLocation']['Latitude'],
               vehicleActivity[i]['MonitoredVehicleJourney'][
                   'VehicleLocation']['Longitude']
               )
              )
