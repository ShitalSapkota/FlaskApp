import psycopg2


class Backend:

    def __init__(self, host, port, username, password, db):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db = db

        conn_str = f"host={self.host} port={self.port} dbname={self.db} user={self.username} password={self.password}"

        try:
            self.client = psycopg2.connect(conn_str)

        except Exception as ex:
            print(f"Error Occurred, Error is {ex}")

    def get_all_country_list(self):
        cur = self.client.cursor()
        query = "SELECT * FROM country"
        cur.execute(query)
        response = cur.fetchall()
        value = []
        for p in range(len(response)):
            a = list(response[p])
            value.append(a)
        disc = []
        attribute = ["id", "country_name", "population", "area", "latitude", "longitude"]
        for j in value:
            store = dict(zip(attribute, j))
            disc.append(store)
        # temp_name = []
        # for p in range(len(response)):
        #     a = list(response[p])
        #     value.append(a)
        #     temp_name.append("user" + str(p + 1))
        # disc = {}
        # attribute = ["id", "country_name", "population", "area", "latitude", "longitude"]
        # for j in range(len(temp_name)):
        #     store = dict(zip(attribute, value[j]))
        #     disc[temp_name[j]] = store
        return disc

    def get_By_name(self, countryName):
        cur = self.client.cursor()
        query = "SELECT * FROM country where country_name = '" + countryName + "'"
        cur.execute(query)
        response = cur.fetchall()
        value = []
        for p in range(len(response)):
            a = list(response[p])
            value.append(a)
        disc = []
        attribute = ["id", "country_name", "population", "area", "latitude", "longitude"]
        for j in value:
            store = dict(zip(attribute, j))
            disc.append(store)
        return disc

    def get_city_by_countryname(self, countryName, cityName):
        cur = self.client.cursor()
        query = f"SELECT * FROM cities INNER JOIN country ON cities.country_id = country.id " \
                f"where country.country_name = '{countryName}' and cities.city_name = '{cityName}'"
        cur.execute(query)
        response = cur.fetchall()
        value = []
        for p in range(len(response)):
            a = list(response[p])
            value.append(a)
        disc = []
        attribute = ["cid", "city_name", "country_id", "population", "area", "latitude", "longitude"]
        for j in value:
            store = dict(zip(attribute, j))
            disc.append(store)
        return disc
