#!/bin/bash

echo "Indoor Test Bypassing Graphene Blocks Hopefully"

# Random Coordinates to test
LAT="40.0083"
LON="-105.2698"

echo "Sending"

# Send via ngrok for test
curl -X POST https://c7c6-128-138-65-177.ngrok-free.app/location \
     -H "Content-Type: application/json" \
     -d "{\"latitude\": $LAT, \"longitude\": $LON}"
