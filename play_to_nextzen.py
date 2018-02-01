# -*- coding: utf-8 -*-

import os
import re
import json
import requests
# import yaml
# import ruamel.yaml as yaml
# yaml = YAML()



dir = "./"
def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            full_path = os.path.join(root, name)
            parse_files(full_path)
            r.append(full_path)
    return r
    
def parse_files(file):   
#     match = "(.*)url:(.*)"
#     match = "(.*)resources(.*)"
#     match = "(.*)s3(.*)" # checking for data sources in buckets that might go away

    match_mz = "tile.mapzen.com/mapzen"
    update_mz = "tile.nextzen.org/tilezen"
    match_carto = "mapzen.com/carto"
    update_carto = "tilezen.org/carto"
#     print("looking in " + file)
#     play = open(file, "r")
#     for line in file:
#         print(line)
#         if re.search(match, line):
#             print("match!")
    print("found mapzen.com urls:") 
    print(file.count("mapzen.com"))
    
    if re.search(match_mz, file):
        print("swapping " + update_mz) 
    nextzen = file.replace(match_mz, update_mz)  

    if re.search(match_carto, file):
        print("swapping " + update_carto)        
    nextzen = nextzen.replace(match_carto, update_carto)  
    
#     print(nextzen) 
    return nextzen  
# def parse_yaml(r):
#     scene = yaml.load(r)
#     print(scene["sources"]["url"])
 
            
data = json.load(open('22.json'))  
for i in data:
    id = i['id']
    url = i['entrypoint_url']
    lat = i['view_lat']
    lng = i['view_lng']
    zoom = i['view_zoom']
    name = i['name'].replace("/", "-")
    print(name,lat,lng,zoom,url) 
    r = requests.get(url)
    print(r)
    filename = "{} {}.yaml".format(id,name)
    print(filename)
    nextzen = parse_files(r.text)
#     print(nextzen)
    
# experiments in parsing YAML to manipulate keys and what not
    
#    try:
#     scene = yaml.load(r.content) # <- parses yaml, but doesn't like emoji 
#     except yaml.YAMLError, exc:
#         print "Error in configuration file:", exc    
    
#     print(scene["sources"])

#     try: # <- this works
#         print(scene["sources"]) # <- this works
#     except KeyError: # <- this works
#         print("no source") # <- this works
        
#     except yaml.YAMLError as error:
#         print(error)
    
#     print(scene["sources"][0])
    
#     parse_yaml(r.text)


    file = open(filename,"w")
    file.write(nextzen)
    file.close() 

# print(data)

# list_files(dir)
    
# https://stackoverflow.com/questions/19932130/python-iterate-through-folders-then-subfolders-and-print-filenames-with-path-t
# http://palewi.re/posts/2008/04/05/python-recipe-open-a-file-read-through-it-print-each-line-matching-a-search-term/
