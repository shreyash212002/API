from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store for road curvature and front vehicle distance
data_store = {
    "curvature_angle": None,  # Stores the curvature of the road as angle
    "front_vehicle_distance": None  # Stores the distance from the front vehicle
}

# Endpoint to store road curvature as angle
@app.route('/api/store/curvature', methods=['POST'])
def store_curvature():
    try:
        angle = request.json.get('angle')
        if angle is None:
            return jsonify({"error": "Angle is required"}), 400

        # Store the curvature angle in data_store
        data_store["curvature_angle"] = angle
        return jsonify({"message": "Curvature angle stored successfully", "curvature_angle": angle}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to store distance from the front vehicle
@app.route('/api/store/distance', methods=['POST'])
def store_distance():
    try:
        distance = request.json.get('distance')
        if distance is None:
            return jsonify({"error": "Distance is required"}), 400

        # Store the front vehicle distance in data_store
        data_store["front_vehicle_distance"] = distance
        return jsonify({"message": "Distance stored successfully", "front_vehicle_distance": distance}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve the stored curvature and distance
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # Return the stored curvature and distance
        return jsonify({
            "curvature_angle": data_store.get("curvature_angle"),
            "front_vehicle_distance": data_store.get("front_vehicle_distance")
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point of the Flask app
if __name__ == '__main__':
    app.run(debug=True)
