import numpy as np
import pandas as pd
attendence_percentage = np.round(np.random.uniform(10.0,99.99,200),2)
study_hours = np.random.randint(0,10,200)
# print(attendence_percentage)
# print(study_hours)
percentage = []
for i in range(200):
    score = np.round((attendence_percentage[i]+(study_hours[i]/10*100))/2,2)
    percentage.append(score)
# print(percentage) 
dataset = pd.DataFrame({
    "Study Hrs/Day":study_hours,
    "Attendence Percentage":attendence_percentage,
    "Percentage Score":percentage
})  
print(dataset)
dataset.to_csv("StudentPercentageDataset.csv",index=False)