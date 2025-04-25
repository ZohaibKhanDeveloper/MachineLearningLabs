import numpy as np
import pandas as pd
ages = np.random.randint(20,81,500)
# print(ages)
bmis = np.round(np.random.uniform(18.5,45.0,500),1)
# print(bmis)
glucose_level = np.random.randint(70,201,500)
# print(glucose_level)
blood_pressure = np.random.randint(90,181,500)
# print(blood_pressure)
family_history = np.random.randint(0,2,500)
# print(family_history)
physical_activity = np.round(np.random.uniform(0.0,10.0,500),1)
# print(physical_activity)
def label_data(gl,bmi,age,fh,pa,size):
    labels = []
    for i in range(0,size):
        score = (
            0.3 * (gl[i]/200)+
            0.2 * (bmi[i]/45)+
            0.2 * (age[i]/80)+
            0.2 * fh[i]-
            0.2 * (pa[i]/10)
        )
        if score >= 0.5:
            labels.append(1)
        else: 
            labels.append(0)    
    return labels        
labels = label_data(glucose_level,bmis,ages,family_history,physical_activity,500)
dataset = pd.DataFrame({
    "Age":ages,
    "Body Mass Index(BMI)":bmis,
    "Glucose Level":glucose_level,
    "Blood Pressure":blood_pressure,
    "Family History":family_history,
    "Physical Activity(hrs/week)":physical_activity,
    "Diabetic(0/1)":labels
})
print(dataset)
dataset.to_csv("DiabetesClassificationData.csv",index=False)