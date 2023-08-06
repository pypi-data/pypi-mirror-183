import geopy
import geopy.distance
import pandas as pd
import requests
import sklearn.preprocessing

STATIONS_URL = "https://www.mvg.de/api/fahrinfo/location/queryWeb?q="


def get_stations():
    """
    Gets all stations in the MVV, including their coordinates and means of transport available there.
    """
    req = requests.get(STATIONS_URL)
    data = req.json()
    stations = pd.DataFrame(data["locations"])
    
    stations = stations[(stations.place == "München") & (stations.type == "station")]
    stations = stations.rename(columns={"latitude": "lat", "longitude": "lon", "products": "types"})
    stations = stations.filter(["name", "lat", "lon", "types"])
    stations = stations.reset_index(drop=True)
    
    mlb = sklearn.preprocessing.MultiLabelBinarizer()
    types = mlb.fit_transform(stations.types)
    stations_enc = stations.join(pd.DataFrame(types, columns=mlb.classes_)).drop(["types"], axis="columns")
    stations_enc = stations_enc.rename(columns=str.lower)
    
    return stations_enc


def get_nearest_stations(adress, stations):
    geocoder = geopy.geocoders.Nominatim(user_agent="Station Calculator", proxies=proxies)
    location = geocoder.geocode(adress)
    nearest_stations = stations.loc[:]
    nearest_stations["distance"] = nearest_stations.apply(lambda x: round(geopy.distance.distance((location.latitude, location.longitude), (x.lat, x.lon)).meters), axis="columns")
    nearest_stations = nearest_stations.sort_values(by="distance")
    bus = nearest_stations[nearest_stations.bus == 1].iloc[0].distance
    tram = nearest_stations[nearest_stations.tram == 1].iloc[0].distance
    subahn = nearest_stations[(nearest_stations.sbahn == 1) | (nearest_stations.ubahn == 1)].iloc[0].distance
    bahn = nearest_stations[nearest_stations.bahn == 1].iloc[0].distance
    return {"bus": bus, "tram": tram, "s-bahn / u-bahn": subahn, "zug": bahn}                