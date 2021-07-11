#!/usr/bin/python3
import numpy as np
import cgi
from keras.models import load_model

print("Content-Type: text/html")
print("Access-Control-Allow-Origin: *")
print()

form = cgi.FieldStorage()
age_year = form.getvalue("age")
fever = form.getvalue("fever")
cough = form.getvalue("cough")
runny_nose = form.getvalue("runny_nose")
muscle_soreness = form.getvalue("muscle_soreness")
diarrhea = form.getvalue("diarrhea")
lung_infection = form.getvalue("lung_infection")
travel_history = form.getvalue("travel_history")
isolation_treatment = form.getvalue("isolation_treatment")
pneumonia = form.getvalue("pneumonia")
male = form.getvalue("male")


model = load_model("Final_model.h5")
"""def test(age_year,fever,cough,runny_nose,muscle_soreness,pneumonia,diarrhea,lung_infection,travel_history,isolation_treatment, male):
    X = np.vstack([int(age_year),int(fever,cough),int(runny_nose),int(muscle_soreness),int(pneumonia),int(diarrhea),int(lung_infection),int(travel_history),int(isolation_treatment), int(male)])
    if model.predict(X.reshape(1,11))[0][0] < 0.50:
        return "Negative"
    else:
        return "Positive"
"""

age_year = int(age_year)
fever = int(fever)
cough = int(cough)
runny_nose = int(runny_nose)
muscle_soreness = int(muscle_soreness)
pneumonia = int(pneumonia)
diarrhea = int(diarrhea)
lung_infection = int(lung_infection)
travel_history = int(travel_history)
isolation_treatment = int(isolation_treatment)
male = int(male)



X = np.vstack([age_year,fever,cough,runny_nose,muscle_soreness,pneumonia,diarrhea,lung_infection,travel_history,isolation_treatment,male])

output = model.predict(X.reshape(1,11))[0][0]

print(output)
