# WebScraperIMN
Script that returns information from the IMN which is the national meteorological agency of Costa Rica, while also implementig an API using Flask.

## Overview
This script retrieves meteorological information from IMN (Instituto Meteorológico Nacional), which does not provide a public API for accessing its data. 
The script scrapes the information presented on the IMN website for a given station and returns it as a JSON object.

## Script Usage
To use this script, simply call the getInfo() function with the name of the meteorological station as an argument. 
The function will return a JSON object containing the meteorological information for the requested station.

## API Usage
The API endpoint will be located at localhost:2000/result. This endpoint accepts both POST and GET requests. 
The request body should be a JSON object containing the parameter "station" which is the name of the meteorological station to retrieve information for.
You can find the station's name by following these steps:

Go to: https://www.imn.ac.cr/estaciones-automaticas and select a station.

Next: Inspect the website and find the iframe with the "datos" id.

Finally: In the iframe you will find src=/especial/tablas/cartagotec.html, the name of the station is the text between the last / and the .html.

## Note
Please note that this script relies on web scraping to retrieve data from the IMN website, which may be subject to change without notice. 
Use of this script is at your own risk and is not endorsed or supported by IMN.
