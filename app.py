from flask import Flask , request , render_template
import numpy as np
import pickle 

model = pickle.load(open("rf.pkl" , "rb"))
app = Flask(__name__)

@app.route('/')
def home():
   return render_template("index.html")

@app.route("/predict", methods = ["POST" , "GET"])
def predict():
   if request.method == "POST":
        department = int(request.form["department"])
        education = int(request.form["education"])
        gender =  int(request.form["gender"])
        age = int(request.form["age"])
        length_of_service = int(request.form["length_of_service"])
        total_score = int(request.form["total_score"])
        sum_metrics = float(request.form["sum_metrics"])

        pred = model.predict([[department , education , gender , 
                              age , length_of_service , total_score , sum_metrics]])
        
        output = pred[0]
        if output == 0:
            return render_template("predict.html" , predicted_text = "This Employee will not get promotion")
        
        else:
            return render_template("predict.html" , predicted_text = "This employee will get Promotion ")

   return render_template("predict.html")

if __name__ == '__main__':
   app.run(debug=True)