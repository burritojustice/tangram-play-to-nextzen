# tangram-play-to-nextzen

This Python 3 script downloads your Tangram Play files and updates mapzen.com URLs to nextzen.org.


# get your metadata

- log into Tangram Play (hurry! like, today, Feb 1)
- Do you know your developer ID? (It's a number.) If not, open https://mapzen.com/api/developer.json after you log in.
- Download https://mapzen.com/api/scenes/YOUR_DEVELOPER_ID (that's your blob of json that points to all your YAML scene files). You should have a file that looks like `22.json` on your desktop.

# install dependencies

You may need to install the `requests` module:

`pip3 install requests`

# run the script

`python3 play_to_nextzen.py YOUR_USER_ID.json`

It will download all your scene files from mapzen.com, replace tile.mapzen.com and mapzen.com/carto URLs with their nextzen.org equivalents, and save them to disk with the scene file number and a meaningful name (if you added one in the description field).

# TO DO

- done! ~try to use `fileinput` to read the json filename as a command line argument~   
- doesn't do anything with API keys (stay tuned to nextzen.org for that)
- doesn't yet look for old-style `vector.mapzen.com/osm` URLs
- save static geojson files locally?
- IANAD so sorry the code is ugly
