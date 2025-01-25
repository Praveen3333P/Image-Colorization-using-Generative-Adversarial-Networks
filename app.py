from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from colorization_test import test_colorization
import tempfile
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process_image", methods=["POST"])
def process_image_route():
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if file:
        try:
            # Save the uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_path = temp_file.name
                file.save(temp_path)

            # Process the image
            result = test_colorization(temp_path)
        finally:
            # Attempt to remove the temporary file
            try:
                os.remove(temp_path)
            except Exception as e:
                print(f"Failed to remove temporary file: {e}")

        return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)

        
#         return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)
