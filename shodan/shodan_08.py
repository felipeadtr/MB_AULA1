#!/usr/bin/python

import shodan
shodan_mykey='nkGd8uVE4oryfUVvioprswdKGmA5InzZ'
shodan_api = shodan.Shodan(shodan_mykey)
#shodan_item='Microsoft-IIS/8.0 country:"BR"'
shodan_item='Microsoft-IIS/8.0'
shodan_result = shodan_api.search(shodan_item)

def shodan_search():
    print('Buscar por:', shodan_item)
    print('Numero de ocorrencias:',shodan_result['total'])


shodan_search()
