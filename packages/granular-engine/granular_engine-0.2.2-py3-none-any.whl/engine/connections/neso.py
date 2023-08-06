import requests 


__all__ = ["Neso"]


class Neso:
    def __init__(self, callisto=None, org=None):
        self.callisto = callisto 
        self.org = org 

    def get_sensors(self):
        sensor_url = f'{self.callisto.host}/neso/api/v1/sensor'

        response  = requests.get(sensor_url, headers=self.callisto.headers)

        if response.status_code == 200:
            sensors = response.json()['data']
            return {sensor["id"]: sensor for sensor in sensors}

        else:
            print(f"Sensor details cannot be retrieved")
            return None