from flask import Flask,render_template,request,redirect
from pipeline import preprocessing,vectorizer,get_prediction


app = Flask(__name__)
data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html',data = data)

@app.route("/",methods = ['post'])
def gettxt():
    txt = request.form['Textarea']
    preprocessed_txt = preprocessing(txt)
    vectorized_txt = vectorizer(preprocessed_txt)
    prediction = get_prediction(vectorized_txt)

    if prediction == 'positive':
        global positive
        positive += 1
    else:
        global negative
        negative += 1
    reviews.insert(0,txt)
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)