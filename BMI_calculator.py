
import pandas as pd

df = pd.read_csv("Data_for_BMI_Calculator_Height_Weight.csv", usecols = ['Gender','Height (cm)','Weight (Kg)'])


df = df[df['Gender'].isin(['Male','Female','Other'])]

def type_check(i):
    try:
        if int(i['Height (cm)']) and int(i['Weight (Kg)']):
            return True
    except:
        return False

df['flag'] = df.apply(lambda row: type_check(row),axis=1)

df =df[df['flag']]


df['Weight (Kg)'] = df['Weight (Kg)'].astype(int)
df['Height (cm)'] = df['Height (cm)'].astype(int)

df['BMI'] = df['Weight (Kg)']/ ((df['Height (cm)']/100)**2)


df.loc[df['BMI']<=18.4,'BMI Category'] = 'Underweight'
df.loc[df['BMI']<=18.4,'Health Risk'] = 'Malnutrition risk'

df.loc[df['BMI'].between(18.5,24.9),'BMI Category'] = 'Normal weight'
df.loc[df['BMI'].between(18.5,24.9),'Health Risk'] = 'Low risk'

df.loc[df['BMI'].between(25,29.9),'BMI Category'] = 'Overweight'
df.loc[df['BMI'].between(25,29.9),'Health Risk'] = 'Enhanced risk'

df.loc[df['BMI'].between(30,34.5),'BMI Category'] = 'Moderately obese'
df.loc[df['BMI'].between(30,34.5),'Health Risk'] = 'Medium risk'

df.loc[df['BMI'].between(35,39.9),'BMI Category'] = 'Severely obese'
df.loc[df['BMI'].between(35,39.9),'Health Risk'] = 'High risk'

df.loc[df['BMI']>=40,'BMI Category'] = 'Very severely obese'
df.loc[df['BMI']>=40,'Health Risk'] = 'Very high risk'

del df['flag']





