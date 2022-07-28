from flask import Flask, request, jsonify
import pickle
import pandas as pd

# inisiasi app
app = Flask(__name__)

# inisiasi open model

def open_model(model_path):
    """
    helper function for loading model
    """
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

model_startup = open_model("model.pkl") # pandas dataframe

def inference_startup(data, model):
    """
    input : list with length : 6 --> [1, 2, 3, 4, 5, male/female]
    ouput : predicted class (idx, label)
    """
    label = ["Closed", "Acquired"]
    columns = ['category_code', 'age_first_milestone_year', 'age_last_milestone_year', 'age_milestone_year_null', 
               'milestones', 'relationships', 'funding_rounds', 'funding_total_usd', 'avg_participants', 'is_top500']
    data = pd.DataFrame([data],columns=columns)
    res = model_startup.predict(data)
    return res[0], label[res[0]]

# Halaman home
@app.route("/")
def homepage():
    return "<h1> Deployment Model Backend! </h1>"


@app.route('/startup_prediction', methods=['POST'])
def startup_predict():
    """
     content = 
    {
        'category_code': XX,
        'age_first_milestone_year': XX,
        'age_last_milestone_year': XX,
        'age_milestone_year_null': XX,
        'milestones': XX,
        'relationships': XX,
        'funding_rounds': XX,
        'funding_total_usd': XX,
        'avg_participants': XX,
        'is_top500': X 
    }
    """
    columns = ['category_code', 'age_first_milestone_year', 'age_last_milestone_year', 'age_milestone_year_null', 
               'milestones', 'relationships', 'funding_rounds', 'funding_total_usd', 'avg_participants', 'is_top500']
    content = request.json
    newdata = [content['category_code'], 
               content['age_first_milestone_year'],
               content['age_last_milestone_year'],
               content['age_milestone_year_null'],
               content['milestones'],
               content['relationships'],
               content['funding_rounds'],
               content['funding_total_usd'],
               content['avg_participants'],
               content['is_top500']
               ]
    res_idx, res_label = inference_startup(newdata, model_startup)
    result = {"label_idx":str(res_idx),
              "label_names": res_label
              }

    response = jsonify(success=True,
                       result=result)
    return response, 200

# run app di local
# jika deploy di heroku, comment baris di bawah ini
# app.run(debug=True)

