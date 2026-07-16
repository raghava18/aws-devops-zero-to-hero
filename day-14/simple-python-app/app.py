from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 'Ome Shree Poojaya Raghavendra Satya Dharma Ratayacha bhajatam kalparukshaya Namatama Kamdhenuve!!!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
