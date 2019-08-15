import json
import wikipedia

class json_file:
    def __init__(self, name_of_file):
        self.name = name_of_file
        self.сounter = 0

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.name, 'r') as f:
            length_of_file = len(json.load(f))
        with open(self.name, 'r') as f:
            countries = json.load(f)[self.сounter-length_of_file]
            country = countries['name']['common']
            try:
                page_country = wikipedia.page(country)
                dict_country_wiki_url = {country: page_country.url}
            except wikipedia.exceptions.DisambiguationError:
                try:  
                    page_country = wikipedia.page(countries['name']['official'])
                    dict_country_wiki_url = {country: page_country.url}
                except wikipedia.exceptions.DisambiguationError:
                    page_country = wikipedia.page(countries['name']['official']+' (country)')
                    dict_country_wiki_url = {country: page_country.url}
        with open(r'countries_wiki_url.txt', 'a+', encoding='utf-8') as write_countries_file:
            write_countries_file.write(str(dict_country_wiki_url)+'\n')
        self.сounter += 1
        if self.сounter == length_of_file:
            raise StopIteration
        return country, page_country

for item in json_file('countries.json'):
    print(item)