import connexion
from flask import request, jsonify


class ApiDefinition:
    backend = None

    def __init__(self, api_file):
        self.api_file = api_file
        self.connexion_app = connexion.FlaskApp(__name__, specification_dir='')
        self.connexion_app.add_api(self.api_file, resolver=self.function_resolver, base_path='/')

    def function_resolver(self, operation_id):
        if '.' in operation_id:
            _, function_name = operation_id.rsplit('.', 1)
        else:
            function_name = operation_id

        function = getattr(self, function_name)
        return function

    def getAllCountriesName(self):
        data = self.backend.get_all_country_list()
        return jsonify(data)

    def getCountryByName(self, countryName):
        data = self.backend.get_By_name(countryName)
        return jsonify(data)

    def getCityByCountryName(self, countryName):
        arg = request.args
        cityName = arg['cityName']
        data = self.backend.get_city_by_countryname(countryName, cityName)
        return jsonify(data)


