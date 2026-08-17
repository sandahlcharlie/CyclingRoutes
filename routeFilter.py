import gpxpy
from geopy.distance import geodesic
import os
import shutil

def routeFilter(inputFolder):
    # Get the destination to look for routes too and from
    destinoLat = input("Input destination latitude: ")
    destinoLon = input("Input destination longitude: ")
    radius = 250
    
    for filename in os.listdir(inputFolder, homeLat, homeLon):
    if not filename.endswith(".gpx"):
        continue

        gpxData = gpxpy.parse(open(os.path.join(inputFolder, filename)))

        points = gpxData.tracks[0].segments[0].points

        start = points[0]
        end = points[-1]

        startHome = geodesic((start.latitude, start.longitude), (homeLat, homeLon)).meters <= 250
        endDestino = geodesic((end.latitude, end.longitude), (destinoLat, destinoLon)).meters <= 250

        startDestino = geodesic((start.latitude, start.longitude), (destinoLat, destinoLon)).meters <= 250
        endHome = geodesic((end.latitude, end.longitude), (homeLat, homeLon)).meters <= 250

        if (startHome and endDestino) or (startDestino and endHome):
            shutil.copy(os.path.join(inputFolder, filename), os.path.join(outputFolder, filename))
            print(f"Saved: {filename}")









