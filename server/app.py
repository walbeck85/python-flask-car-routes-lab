"""This Flask application is part of the Flatiron 'Introduction to Flask – Car Routes' lab. It serves as a simple demonstration of routing in Flask, allowing users to query available car models in the Flatiron fleet."""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# List of existing car models available in the Flatiron fleet
existing_models = [
    "civic", "accord", "camry", "corolla",
    "mustang", "model-3", "model-s", "model-x",
    "Crossroads"  
]

# Define the root route that welcomes users to the application
@app.route("/")
def index():
    # Return a welcome message for the root URL
    return "Welcome to Flatiron Cars"

# Define a dynamic route that looks up car models by name
@app.route("/<string:model>")
def model_lookup(model):
    # Create a set of existing models in lowercase for case-insensitive matching
    models_lower = {m.lower() for m in existing_models}
    # Check if the requested model exists in the fleet (case-insensitive)
    if model.lower() in models_lower:
        return f"Flatiron {model} is in our fleet!"
    # Return a message if the model is not found in the catalog
    return f"No models called {model} exists in our catalog"

# Entry point of the application
if __name__ == "__main__":
    # Run the Flask app on port 5555 with debug mode enabled for easier development and troubleshooting
    app.run(port=5555, debug=True)