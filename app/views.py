from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StrokePredictionForm
from .models import UserProfile, Activity
import pickle
import pandas as pd
import json
from django.core.paginator import Paginator

# Load model once at module level
with open('stroke_model.pkl', 'rb') as file:  # Ensure path matches your structure
    model = pickle.load(file)

def logout_view(request):
    if request.user.is_authenticated:
        Activity.objects.create(user=request.user, action="Logged out")
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            Activity.objects.create(user=user, action="Logged in")
            # Redirect to profile_setup if no profile exists
            if not hasattr(user, 'userprofile'):
                return redirect('profile_setup')
            return redirect('predict_stroke')
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Activity.objects.create(user=user, action="Registered")
            return redirect('profile_setup')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

@login_required
def profile_setup(request):
    if request.method == 'POST':
        form = StrokePredictionForm(request.POST)
        if form.is_valid():
            profile = UserProfile(
                user=request.user,
                age=form.cleaned_data['age'],
                hypertension=form.cleaned_data['hypertension'],
                heart_disease=form.cleaned_data['heart_disease'],
                ever_married=form.cleaned_data['ever_married'],
                residence_type=form.cleaned_data['Residence_type'],
                avg_glucose_level=form.cleaned_data['avg_glucose_level'],
                bmi=form.cleaned_data['bmi'],
                gender=form.cleaned_data['gender'],
                work_type=form.cleaned_data['work_type'],
                smoking_status=form.cleaned_data['smoking_status'],
                still_working=1 if form.cleaned_data['work_type'] in ['Govt_job', 'Private', 'Self-employed'] else 0
            )
            profile.save()
            Activity.objects.create(user=request.user, action="Profile created")
            return redirect('predict_stroke')
    else:
        form = StrokePredictionForm()
    return render(request, 'app/profile_setup.html', {'form': form})

@login_required(login_url='login')
def predict_stroke(request):
    # Check if user has a profile; redirect to setup if not
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('profile_setup')

    if request.method == 'POST':
        form = StrokePredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = {
                'age': [data['age']],
                'hypertension': [data['hypertension']],
                'heart_disease': [data['heart_disease']],
                'ever_married': [data['ever_married']],
                'Residence_type': [data['Residence_type']],
                'avg_glucose_level': [data['avg_glucose_level']],
                'bmi': [data['bmi']],
                'gender_Female': [1 if data['gender'] == 'Female' else 0],
                'gender_Male': [1 if data['gender'] == 'Male' else 0],
                'gender_Other': [1 if data['gender'] == 'Other' else 0],
                'work_Govt_job': [1 if data['work_type'] == 'Govt_job' else 0],
                'work_Never_worked': [1 if data['work_type'] == 'Never_worked' else 0],
                'work_Private': [1 if data['work_type'] == 'Private' else 0],
                'work_Self-employed': [1 if data['work_type'] == 'Self-employed' else 0],
                'work_children': [1 if data['work_type'] == 'children' else 0],
                'smoke_Unknown': [1 if data['smoking_status'] == 'Unknown' else 0],
                'smoke_formerly smoked': [1 if data['smoking_status'] == 'formerly smoked' else 0],
                'smoke_never smoked': [1 if data['smoking_status'] == 'never smoked' else 0],
                'smoke_smokes': [1 if data['smoking_status'] == 'smokes' else 0],
                'still_working': [1 if data['work_type'] in ['Govt_job', 'Private', 'Self-employed'] else 0]
            }
            input_df = pd.DataFrame(input_data)
            prediction = model.predict(input_df)[0]
            result = 'Yes' if prediction == 1 else 'No'
            Activity.objects.create(
                user=request.user,
                action="Made prediction",
                details=json.dumps({'input': input_data, 'prediction': result})
            )
            return render(request, 'app/result.html', {'result': result, 'form': form})
    else:
        # Populate form with existing profile data
        initial_data = {
            'age': profile.age,
            'hypertension': profile.hypertension,
            'heart_disease': profile.heart_disease,
            'ever_married': profile.ever_married,
            'Residence_type': profile.residence_type,
            'avg_glucose_level': profile.avg_glucose_level,
            'bmi': profile.bmi if profile.bmi else None,
            'gender': profile.gender,
            'work_type': profile.work_type,
            'smoking_status': profile.smoking_status,
        }
        form = StrokePredictionForm(initial=initial_data)
    return render(request, 'app/predict.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    activities = Activity.objects.filter(user=request.user).order_by('-timestamp')
    paginator = Paginator(activities, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/dashboard.html', {'page_obj': page_obj})
