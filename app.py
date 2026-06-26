from flask import Flask, render_template, request
from scanner import scan_ports

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    ip = None

    if request.method == "POST":
        ip = request.form["ip"]
        result = scan_ports(ip)

        
        print("DEBUG IP:", ip)
        print("DEBUG RESULT:", result)

    return render_template("index.html", result=result, ip=ip)

if __name__ == "__main__":
    app.run(debug=True)