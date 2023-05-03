from unidecode import unidecode
from bs4 import BeautifulSoup
from flask import request, Flask

import requests
import re

'''
Create Application Using Flask
'''

app = Flask(__name__)
@app.route('/result', methods = ['POST', 'GET'])

def result():
    
    body = request.get_json()

    if 'station' not in body:

        return {'Error': 'Not "Station" Parameter'}

    return getInfo(body['station'])

    
'''
Get Information From IMN
'''
    
def getInfo(station):

    try:
        
        htmlText = requests.get('https://www.imn.ac.cr/especial/tablas/' + station + '.html').content.decode('UTF-8')
        soup = BeautifulSoup(htmlText, 'lxml')
        tables = soup.findAll('table')

        dayDataHeaders = tables[1].findAll('th')
        dayData = tables[1].findAll('td')
        currentDataHeaders = tables[2].findAll('th')
        currentData = tables[2].findAll('td')

        jsonData = {}
        jsonData['fecha'] = re.sub(r'[, \n\r]+', '', dayData[0].text)[0:10]
        jsonData['hora'] = re.sub(r'[, \n\r]+', '', dayData[0].text)[11:22]

        for i in range(1, len(dayData)):
            jsonData[unidecode((dayDataHeaders[i].text)).lower()] = re.sub(r'[ \n\r]+', '', dayData[i].text).replace(',', '.')

        for i in range(1, len(currentData)):
            jsonData[unidecode((currentDataHeaders[i].text)).lower()] = re.sub(r'[ \n\r]+', '', currentData[i].text).replace(',', '.')
            

        return jsonData
    
    except:
        
        return {'Error': 'Station Not Found'}

if __name__ == '__main__':
    
    app.run(port = 2000)

    
