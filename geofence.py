import math

def calculate_distance_meters(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    # Forced to use Haversine formula to calc location because Graphene Blocks all location services. This seems to be working
    # And I don't want to try to get around Graphene's extremely good location service blocking. So this will do for now.
    R = 6371000

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2.0) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2.0) ** 2
    
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return distance

def determine_state(phone_lat: float, phone_lon: float, home_lat: float, home_lon: float) -> str:
    distance = calculate_distance_meters(phone_lat, phone_lon, home_lat, home_lon)
    print(f"DEBUG: Phone is {distance:.2f} meters from target.")
    
    if distance <= 150.0:
        return "home"
    return "not_home"