from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask import Flask, send_from_directory
app = Flask(__name__)
CORS(app)

# Homepage route
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def about_us():
    return render_template("about.html")

@app.route("/product")
def services():
    return render_template("product.html")

@app.route("/team")
def patients():
    return render_template("team.html")

@app.route("/problem")
def problem():
    return render_template("problem.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/video')
def serve_video():
    return send_from_directory('static/videos', 'background.mp4')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route("/calculate-size", methods=["POST"])
def calculate_size():
    length = float(request.form.get("length"))
    if length > 15:
        model = "3.1"
    elif 10 < length <= 15:
        model = "2.2"
    else:
        model = "1.3"

    # Send the model name back to the services page
    return render_template("product.html", selected_model=model)

if __name__ == '__main__':
    app.run(debug=True)
handler = app
