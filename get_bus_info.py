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

    f = open(sys.argv[3], 'w')
    w = unicodecsv.writer(f, encoding='utf-8')
    w.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])

    vehicleActivity = data['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']

    for bus in vehicleActivity:
        bus = bus['MonitoredVehicleJourney']
        w.writerow([
            bus['VehicleLocation']['Latitude'],
            bus['VehicleLocation']['Longitude'],
            bus['OnwardCalls']['OnwardCall'][0]['StopPointName']
            if 'OnwardCalls' in bus
            else "N/A",
            bus['OnwardCalls']['OnwardCall'][0]['Extensions'][
                'Distances']['PresentableDistance']
            if 'OnwardCalls' in bus
            else "N/A"
        ])
