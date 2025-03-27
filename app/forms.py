from django import forms

class StrokePredictionForm(forms.Form):
    age = forms.FloatField(label='Age', min_value=0)
    hypertension = forms.ChoiceField(label='Hypertension', choices=[(0, 'No'), (1, 'Yes')])
    heart_disease = forms.ChoiceField(label='Heart Disease', choices=[(0, 'No'), (1, 'Yes')])
    ever_married = forms.ChoiceField(label='Ever Married', choices=[(0, 'No'), (1, 'Yes')])
    Residence_type = forms.ChoiceField(label='Residence Type', choices=[(0, 'Rural'), (1, 'Urban')])
    avg_glucose_level = forms.FloatField(label='Average Glucose Level', min_value=0)
    bmi = forms.FloatField(label='BMI', min_value=0)
    gender = forms.ChoiceField(label='Gender', choices=[
        ('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')
    ])
    work_type = forms.ChoiceField(label='Work Type', choices=[
        ('Govt_job', 'Government Job'), ('Never_worked', 'Never Worked'), 
        ('Private', 'Private'), ('Self-employed', 'Self-employed'), ('children', 'Children')
    ])
    smoking_status = forms.ChoiceField(label='Smoking Status', choices=[
        ('Unknown', 'Unknown'), 
        ('formerly smoked', 'Formerly Smoked'),
        ('never smoked', 'Never Smoked'), 
        ('smokes', 'Smokes')
    ])
