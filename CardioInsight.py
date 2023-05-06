import streamlit as st;
import pandas as pd;
import numpy as np;
import pickle;
print(pickle.format_version)
from streamlit_option_menu import option_menu

div_html = """
<div style='display:flex; justify-content:center; align-items:center'>
  <div style='background-color:#f2f2f2; padding:10px; text-align: center; width: 400vh'>
    <h1 style='text-align:center;'>CardioInsight</h1>
  </div>
</div>
"""

#.as sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = "Diagnose",
        options=["Heart", "Diabetes", "Lung Cancer"],
        )

if selected == "Heart":
    
    safe_html="""  
          <div style="background-color:green;padding:11px;margin-top:10px" >
           <h2 style="color:white;text-align:center;"> Your heart is safe</h2>
           </div>"""

    danger_html="""  
          <div style="background-color:red;padding:11px;margin-top:10px" >
           <h2 style="color:white;text-align:center;"> Your heart is in danger</h2>
           </div>"""

    html_temp = """
          <div style="background-color:tomato;padding:20px;margin-bottom:30px" >
        <h2 style = "color:white; text-align:center;">Disease Prediction Model -(Heart) </h2>
        </div>
        """
    
    st.write(div_html, unsafe_allow_html=True)
    st.write("##")
    st.markdown("<h2 style='text-align: center; color: black;'>Know your health with ML</h2>", unsafe_allow_html=True)

    # st.markdown(html_temp, unsafe_allow_html = True)
    f1 = st.number_input("Cholesterol");
    f2 = st.number_input("MaxHR");
    f3=st.number_input("Oldpeak");
    f4=st.number_input("ChestPainType");
    f5=st.number_input("ExerciseAngina");
    f6=st.number_input("Age");
    f7=st.number_input("ST_Slope");

    loaded_model=pickle.load(open('heartModel.sav','rb'));

    input_data=(f1,f2,f3,f4,f5,f6,f7);
    input_array=np.asarray(input_data);
    input=input_array.reshape(1,-1);
    prediction=loaded_model.predict(input);

    columns = st.columns((2, 1, 2))
    if columns[1].button("Submit"):
        if prediction == 0:
            st.markdown(safe_html,unsafe_allow_html=True)   
        else:
            st.markdown(danger_html,unsafe_allow_html=True)

if selected == "Diabetes":
    
    safe_html="""  
          <div style="background-color:green;padding:11px;margin-top:10px" >
           <h2 style="color:white;text-align:center;">You are safe from Diabetes!! </h2>
           </div>"""

    danger_html="""  
          <div style="background-color:red;padding:11px;margin-top:10px" >
           <h2 style="color:white;text-align:center;"> You seem to have Diabetes..</h2>
           </div>"""

    html_temp = """
          <div style="background-color:tomato;padding:20px;margin-bottom:30px" >
        <h2 style = "color:white; text-align:center;">Disease Prediction Model -(Heart) </h2>
        </div>
        """
    
    st.write(div_html, unsafe_allow_html=True)
    st.write("##")
    st.markdown("<h2 style='text-align: center; color: black;'>Know your health with ML</h2>", unsafe_allow_html=True)

    # st.markdown(html_temp, unsafe_allow_html = True)
    f1 = st.number_input("Insulin");
    f2 = st.number_input("Glucose");
    f3=st.number_input("Age");
    f4=st.number_input("Pregnancies");
    f5=st.number_input("BMI");
    f6=st.number_input("Skin Thickness");
    f7=st.number_input("DiabetesPedegreeFunction");

    loaded_model=pickle.load(open('diabetesModel.sav','rb'));

    input_data=(f1,f2,f3,f4,f5,f6,f7);
    input_array=np.asarray(input_data);
    input=input_array.reshape(1,-1);
    prediction=loaded_model.predict(input);

    columns = st.columns((2, 1, 2))
    if columns[1].button("Submit"):
        if prediction == 0:
            st.markdown(safe_html,unsafe_allow_html=True)   
        else:
            st.markdown(danger_html,unsafe_allow_html=True)

if selected == "Lung Cancer":
    
    lvl0_html="""
        <div style="background-color:green;padding:11px;margin-top:10px" >
        <h2 style="color:white;text-align:center;">You are having LOW chances of having cancer</h2>
        </div>"""

    lvl1_html="""  
          <div style="background-color:yellow;padding:11px;margin-top:10px" >
           <h2 style="color:black;text-align:center;">You are having MEDIUM chances of having cancer</h2>
           </div>"""
    
    lvl2_html="""  
          <div style="background-color:red;padding:11px;margin-top:10px" >
           <h2 style="color:white;text-align:center;">You are having HIGH chances of having cancer</h2>
           </div>"""

    html_temp = """
          <div style="background-color:tomato;padding:20px;margin-bottom:30px" >
        <h2 style = "color:white; text-align:center;">Disease Prediction Model -(Heart) </h2>
        </div>
        """
    
    st.write(div_html, unsafe_allow_html=True)
    st.write("##")
    st.markdown("<h2 style='text-align: center; color: black;'>Know your health with ML</h2>", unsafe_allow_html=True)

    # st.markdown(html_temp, unsafe_allow_html = True)
    f1 = st.number_input("Coughing of Blood");
    f2 = st.number_input("Alcohol Use");
    f3=st.number_input("Passive Smoker");
    f4=st.number_input("Obesity");
    f5=st.number_input("Smoking");
    f6=st.number_input("Balanced Diet");
    f7=st.number_input("Chest Pain");

    loaded_model=pickle.load(open('cancerModel.sav','rb'));

    input_data=(f1,f2,f3,f4,f5,f6,f7);
    input_array=np.asarray(input_data);
    input=input_array.reshape(1,-1);
    prediction=loaded_model.predict(input);

    columns = st.columns((2, 1, 2))
    if columns[1].button("Submit"):
        if prediction == 0:
            st.markdown(lvl2_html,unsafe_allow_html=True)   
        elif prediction == 1:
            st.markdown(lvl0_html,unsafe_allow_html=True)
        else:
            st.markdown(lvl1_html, unsafe_allow_html=True)



