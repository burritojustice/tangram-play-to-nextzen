# tangram-play-to-nextzen

This script downloads your Tangram Play files and updates mapzen.com URLs to nextzen.org.


# get your metadata

- log into Tangram Play (hurry!)
- do you know your developer ID? (It's a number.) If not, open https://mapzen.com/api/developer.json (you need to be logged in)
- download https://mapzen.com/api/scenes/YOUR_DEVELOPER_ID (that's your blob of json that points to all your YAML scene files)

# add your developer ID to the script

- change line 56 to your developer ID `data = json.load(open('YOUR_DEVELOPER_ID.json'))`

# run the script

`python3 play_to_nextzen.py`

It will download all your scene files from mapzen.com, replace tile.mapzen.com and mapzen.com/carto URLs with their nextzen.org equivalents, and save them to disk with the scene file number and a meaningful name (if you added one in the description field).

# TO DO

- doesn't yet look for old-style `vector.mapzen.com/osm` URLs
- IANAD so sorry the code is ugly
