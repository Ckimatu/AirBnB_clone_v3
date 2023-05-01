#!/usr/bin/python3

"""index file for app"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def api_status():
    """return api status"""

    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def obj_stats():
    """retrieves the number of each object by type"""

    my_dict = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(my_dict)
