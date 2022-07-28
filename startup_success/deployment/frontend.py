import streamlit as st
import requests

st.set_page_config(
    page_title="A StartUp's Success Prediction",
    page_icon="💵",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/dinanirham',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': "This is web-based application for Author's very first classification model deployment on subject of StartUp's Success Prediction"
    }
)

st.title("A StartUp's Success Prediction")
st.subheader("Predicting the success of a startup allows investors to find companies that have the potential for rapid growth, thereby allowing them to be one step ahead of the competition.")

st.text_input("Your Nominated StartUp's Name To Be Predicted Its Success", value='Bukit Algoritma Bangsa')
code = st.selectbox("StartUp's Category Codes", ["advertising", "analytics", "automotive", 
                    "biotech", "cleantech", "consulting", "ecommerce", "education", 
                    "enterprise", "fashion", "finance", "games_video", "hardware", 
                    "health", "manufacturing", "medical", "messaging", "mobile", 
                    "music", "network_hosting", "news", "other", "photo_video", 
                    "public_relations", "real_estate", "search", "security", 
                    "semiconductor", "social", "software", "sports", "transportation", 
                    "travel", "web"])
agefm = st.number_input("StartUp's Age Since First Milestone (year)", value=2.5)
agelm = st.number_input("StartUp's Age Since Last Milestone (year)", value=5.0)
agenull = st.selectbox("If StartUp's Age Well-known (choose: 0, if yes)", [0, 1])
miles = st.selectbox("StartUp's Milestones Achievement", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
rels = st.number_input("StartUp's Degree of Relationships", value=5)
fround = st.selectbox("StartUp's Funding Rounds Achievement", [1, 2, 3, 4, 5, 6, 7])
ftotal = st.number_input("StartUp's Funding Total Achievement (USD)", value=1500000)
part = st.number_input("StartUp's Average No. of Fundings Participants", value=2.5)
top500 = st.selectbox("If StartUp Categorized as Top 500 Valuations (choose: 1, if yes)", [0, 1])

# inference
data = {'category_code':code,
        'age_first_milestone_year':agefm,
        'age_last_milestone_year':agelm,
        'age_milestone_year_null':agenull,
        'milestones':miles,
        'relationships':rels,
        'funding_rounds':fround,
        'funding_total_usd': ftotal,
        'avg_participants': part,
        'is_top500': top500 
        }

# URL = "http://localhost:5000/startup_prediction" # sebelum push backend
URL = "https://irham-dinan-ftds-p1m2-bend.herokuapp.com/startup_prediction"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if r.status_code == 200:
    st.title(res['result']['label_names'])
else:
    st.title("error")
    st.write(res['message'])