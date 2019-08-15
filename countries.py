import json
from pprint import pprint
import wikipedia

list_wiki = []
with open('countries.json') as countries_file:
    countries = json.load(countries_file)
    print(len(countries))
    c=0
    for item in countries:
        c+=1
        country = item['name']['common'] 
        try:
            page_country = wikipedia.page(country)
            print(c, country, page_country.url)
            dict_country_wiki_url = {country: page_country.url}
            list_wiki.append(dict_country_wiki_url)
        except wikipedia.exceptions.DisambiguationError:
            try:  
                page_country = wikipedia.page(item['name']['official'])
                print(c, country, page_country.url)
                list_wiki.append(dict_country_wiki_url)
            except wikipedia.exceptions.DisambiguationError:
                page_country = wikipedia.page(item['name']['official']+' (country)')
                print(country, page_country.url)
                list_wiki.append(dict_country_wiki_url)
        with open(r'countries_wiki_url.txt', 'a+', encoding='utf-8') as write_countries_file:
            write_countries_file.write(str(dict_country_wiki_url)+'\n')        
    print(list_wiki)
    
    