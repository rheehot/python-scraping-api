from flask import Flask, request, jsonify
import json
import scraping

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route("/news/switch", methods=['GET'])
def switch():
    print("start scraping")
    minutes = request.args.get("minutes", default=30)
    news = scraping.get_switch_news(minutes)
    print("finished scraping")
    return jsonify(news)

@app.route("/ping", methods=['GET'])
def ping():
    return "pong"


host_addr = "0.0.0.0"
host_port = 8080
if __name__ == "__main__":
    app.run(host=host_addr, port=host_port, threaded=True)
