# -*- coding: utf-8 -*-
__title__ = 'geonamescache'
__version__ = '1.4.0'
__author__ = 'Ramiro Gómez'
__license__ = 'MIT'


import json

from importlib import resources

from . import geonamesdata


class GeonamesCache:

    us_states = geonamesdata.us_states
    continents = None
    countries = None
    cities = None
    cities_items = None
    cities_by_names = {}
    us_counties = None

    def __init__(self, min_city_population=15000):
        self.min_city_population = min_city_population

    def get_dataset_by_key(self, dataset, key):
        return dict((d[key], d) for c, d in list(dataset.items()))

    def get_continents(self):
        if self.continents is None:
            self.continents = self._load_data(
                self.continents, 'continents.json')
        return self.continents

    def get_countries(self):
        if self.countries is None:
            self.countries = self._load_data(self.countries, 'countries.json')
        return self.countries

    def get_us_states(self):
        return self.us_states

    def get_countries_by_names(self):
        return self.get_dataset_by_key(self.get_countries(), 'name')

    def get_us_states_by_names(self):
        return self.get_dataset_by_key(self.get_us_states(), 'name')

    def get_cities(self):
        """Get a dictionary of cities keyed by geonameid."""

        if self.cities is None:
            self.cities = self._load_data(self.cities, f'cities{self.min_city_population}.json')
        return self.cities

    def get_cities_by_name(self, name):
        """Get a list of city dictionaries with the given name.

        City names cannot be used as keys, as they are not unique.
        """

        if name not in self.cities_by_names:
            if self.cities_items is None:
                self.cities_items = list(self.get_cities().items())
            self.cities_by_names[name] = [dict({gid: city})
                for gid, city in self.cities_items if city['name'] == name]
        return self.cities_by_names[name]

    def get_us_counties(self):
        if self.us_counties is None:
            self.us_counties = self._load_data(self.us_counties, 'us_counties.json')
        return self.us_counties

    def search_cities(self, query, attribute='alternatenames', case_sensitive=True):
        """Search all city records and return list of records, that match query for given attribute."""

        results = []
        for key, record in self.get_cities().items():
            if case_sensitive:
                if query in record[attribute]:
                    results.append(record)
            else:
                if isinstance(record[attribute], list):
                    if any(
                        getattr(query, 'casefold')() == getattr(value, 'casefold')()
                        for value in record[attribute]
                    ):
                        results.append(record)
                elif (
                    getattr(query, 'casefold')()
                    in getattr(record[attribute], 'casefold')()
                ):
                    results.append(record)
        return results

    def _load_data(self, datadict, datafile):
        if datadict is None:
            datadict = json.loads(resources.files(__name__).joinpath('data', datafile).read_text())
        return datadict