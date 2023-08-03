# General libraries
import os
import json
import sys
import pprint
import folium


def find_centroid(bboxes):
    total_x = 0
    total_y = 0
    num_bboxes = len(bboxes)

    for k in bboxes.keys():
        x_min, y_min, x_max, y_max = bboxes[k]
        total_x += (x_min + x_max) / 2
        total_y += (y_min + y_max) / 2

    centroid_x = total_x / num_bboxes
    centroid_y = total_y / num_bboxes

    return centroid_x, centroid_y


# def showMap_BBOX(items):
    
#     bbox_list = []
#     for item in items: 
#         # print(f'Get bbox of {item.id} (datetime={item.properties["datetime"]})')
#         bbox_list.append(item.bbox)
#     # print(bbox_list)
    
#     centroid_x, centroid_y = find_centroid(bbox_list)

#     # Create a folium map centered on a specific location (e.g., California)
#     map_center = [centroid_y, centroid_x]
#     mymap = folium.Map(location=map_center, zoom_start=7)

#     # Create separate FeatureGroups for each bounding box layer
#     for i, bbox in enumerate(bbox_list):
#         feature_group = folium.FeatureGroup(name=f'BBOX {i+1}')
#         mymap.add_child(feature_group)

#         # Extract the coordinates
#         min_lon, min_lat, max_lon, max_lat = bbox

#         # Calculate the center of the bounding box
#         center_lat = (min_lat + max_lat) / 2
#         center_lon = (min_lon + max_lon) / 2

#         # Create a rectangle using the bounding box coordinates
#         rect = folium.Rectangle(
#             bounds=[(min_lat, min_lon), (max_lat, max_lon)],
#             color='blue',
#             fill=True,
#             fill_color='blue',
#             fill_opacity=0.3,
#             tooltip=f'BBOX {i+1}'
#         )

#         # Add the rectangle to the feature group
#         rect.add_to(feature_group)

#     # Add LayerControl to the map
#     folium.LayerControl().add_to(mymap)

#     return mymap

def showMap_BBOX(items):
    
    bbox_list = {}
    for item in items: 
        # print(f'Get bbox of {item.id} (datetime={item.properties["datetime"]})')
        bbox_list[item.id] = item.bbox
    # pprint.pprint(bbox_list)
    
    centroid_x, centroid_y = find_centroid(bbox_list)

    # Create a folium map centered on a specific location (e.g., California)
    map_center = [centroid_y, centroid_x]
    mymap = folium.Map(location=map_center, zoom_start=7, width=700, height=600)

    # Create separate FeatureGroups for each bounding box layer
    for i, k in enumerate(bbox_list.keys()):
        feature_group = folium.FeatureGroup(name=k)
        mymap.add_child(feature_group)

        # Extract the coordinates
        min_lon, min_lat, max_lon, max_lat = bbox_list[k]

        # Calculate the center of the bounding box
        center_lat = (min_lat + max_lat) / 2
        center_lon = (min_lon + max_lon) / 2

        # Create a rectangle using the bounding box coordinates
        rect = folium.Rectangle(
            bounds=[(min_lat, min_lon), (max_lat, max_lon)],
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.3,
            tooltip=k
        )

        # Add the rectangle to the feature group
        rect.add_to(feature_group)

    # Add LayerControl to the map
    folium.LayerControl().add_to(mymap)

    return mymap