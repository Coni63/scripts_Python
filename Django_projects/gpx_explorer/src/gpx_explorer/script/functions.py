import gpxpy
import gpxpy.gpx
import os
from django.conf import settings

import gmplot
from django.conf import settings

def analyse_gpx(file, index=-1):
    gpx = gpxpy.parse(file)
    data = {}
    data["length2D"] = gpx.length_2d()
    data["length3D"] = gpx.length_3d()
    c = gpx.get_uphill_downhill()
    data["pos_climb"] = c.uphill
    data["pos_climb"] = c.downhill
    gpx.smooth()
    d = gpx.get_uphill_downhill()
    data["pos_climb_smooth"] = d.uphill
    data["neg_climb_smooth"] = d.downhill
    data["duration"] = gpx.get_duration()
    data["average_speed"] = 3.6*data["length3D"]/data["duration"]
    data["elevation_extreme"] = gpx.get_elevation_extremes()
    #print(data["elevation_extreme"])

    raw_data_lat = []
    raw_data_lon = []
    raw_data_alt = []
    for track_idx, track in enumerate(gpx.tracks):
        for seg_idx, segment in enumerate(track.segments):
            for point_idx, point in enumerate(segment.points):
                raw_data_lat.append(point.latitude)
                raw_data_lon.append(point.longitude)
                raw_data_alt.append(point.elevation)

    #gmap = gmplot.GoogleMapPlotter(raw_data_lat[0], raw_data_lon[0], 14)
    #gmap.scatter(raw_data_lat, raw_data_lon, 'k', marker=True)

    #gmap.draw(os.path.join(settings.MEDIA_ROOT, str(index) + ".html"))

    return data
    """
    run_data = []
    for track_idx, track in enumerate(gpx.tracks):
        track_name = track.name
        track_time = track.get_time_bounds().start_time
        track_length = track.length_3d()
        track_duration = track.get_duration()
        track_speed = track.get_moving_data().max_speed

        for seg_idx, segment in enumerate(track.segments):
            segment_length = segment.length_3d()
            for point_idx, point in enumerate(segment.points):
                run_data.append([track_idx, track_name,
                                 track_time, track_length, track_duration, track_speed,
                                 seg_idx, segment_length, point.time, point.latitude,
                                 point.longitude, point.elevation, segment.get_speed(point_idx)])
    return run_data
    """

if __name__ == '__main__':
    with open('test.gpx', 'r') as f:
        print(analyse_gpx(f))