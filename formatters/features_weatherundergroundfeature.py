import math
import json

from django.template.loader import render_to_string

def format(probe_name, json_payload):
    item = json.loads(json_payload)
    
    weather = item["WEATHER"]
    
    temp_c = item["TEMPERATURE"]
    temp_f = (temp_c * 1.8) + 32
    
    dewp_c = item["DEWPOINT"]
    dewp_f = (dewp_c * 1.8) + 32
    
    pressure = item["PRESSURE"]
    pressure_trend = item["PRESSURE_TREND"]
    
    return "{0}: {1:.1f}&deg;F - Dewpoint: {2:.1f}&deg;F - Pressure: {3} ({4})".format(weather, temp_f, dewp_f, pressure, pressure_trend)

def visualize(probe_name, readings):
    temp_report = []
    dewp_report = []
    
    pressure_report = []
    
    for reading in readings:
        payload = json.loads(reading.payload)
        
        timestamp = payload["TIMESTAMP"]
        
        temp_f = round(((payload["TEMPERATURE"] * 1.8) + 32), 1)
        dewp_f = round(((payload["DEWPOINT"] * 1.8) + 32), 1)
        pressure = payload["PRESSURE"]
        
        temp_dict = {}
        temp_dict["y"] = temp_f
        temp_dict["x"] = timestamp
        temp_report.append(temp_dict)
        
        dewp_dict = {}
        dewp_dict["y"] = dewp_f
        dewp_dict["x"] = timestamp
        dewp_report.append(dewp_dict)
        
        pressure_dict = {}
        pressure_dict["y"] = pressure
        pressure_dict["x"] = timestamp
        pressure_report.append(pressure_dict)
        
    return render_to_string(
        'visualization_weather.html', 
        { 
            'probe_name' : probe_name, 
            'readings' : readings, 
            'temp_report' : json.dumps(temp_report), 
            'dewp_report' : json.dumps(dewp_report),
            'pressure_report' : json.dumps(pressure_report)
         }
    )
