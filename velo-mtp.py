#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 10:41:04 2023

@author: maxbld
"""

import folium
import requests
import time

while True:

    api_url = "https://portail-api-data.montpellier3m.fr/bikestation?limit=100"
    
    response = requests.get(api_url)
    
    response.status_code
    
    response_dic = response.json()
    
    # pprint(response_dic)
    
    m = folium.Map(location=(43.6081480, 3.878778), zoom_start=13)
    
    for station in response_dic:
        name = station["address"]["value"]["streetAddress"]
        coords = [station["location"]["value"]["coordinates"][1], station["location"]["value"]["coordinates"][0]]
        availablebike = station["availableBikeNumber"]["value"]
        freeslots = station["freeSlotNumber"]["value"]
        status = station["status"]["value"]
        
        if availablebike > 4:
            folium.Marker(
                    location=coords,
                    tooltip=name,
                    popup=f"<b>Station-vélo {name}</b><br>Vélos disponibles : {availablebike}</br><br>Slots disponibles : {freeslots}</br>",
                    icon=folium.Icon(color='green')).add_to(m)
        
        elif availablebike <=4 and availablebike>0:
            folium.Marker(
                    location=coords,
                    tooltip=name,
                    popup=f"<b>Station-vélo {name}</b><br>Vélos disponibles : {availablebike}</br><br>Slots disponibles : {freeslots}</br>",
                    icon=folium.Icon(color='orange')).add_to(m)
            
        elif availablebike == 0:
            folium.Marker(
                    location=coords,
                    tooltip=name,
                    popup=f"<b>Station-vélo {name}</b><br>Vélos disponibles : {availablebike}</br><br>Slots disponibles : {freeslots}</br>",
                    icon=folium.Icon(color='red')).add_to(m)
            
    m.save("velo-mtp-map.html")
    
    time.sleep(120)
