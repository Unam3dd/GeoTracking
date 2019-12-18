#!/usr/bin/python3
#-*- coding:utf-8 -*-

import folium
import sys

def get_map(longitude,latitude):
    my_map = folium.Map(location=[longitude,latitude], zoom_start=12)
    folium.Marker([longitude,latitude],popup='Target').add_to(my_map)
    my_map.save("victimmap%s_%s.html" % (longitude,latitude))

if __name__ == '__main__':
    if len(sys.argv) <3:
        print("usage : %s <longitude> <latitude>" % (sys.argv[0]))
    else:
        get_map(sys.argv[1],sys.argv[2])