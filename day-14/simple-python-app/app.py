from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Ome Shree Poojaya Raghavendra Satya Dharma Ratayacha bhajatam kalparukshaya Namatama Kamdhenuve!!'

if __name__ == '__main__':
    app.run()

