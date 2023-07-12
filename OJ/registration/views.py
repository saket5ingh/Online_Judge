from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Problem, Submission
from django.contrib.auth.decorators import login_required
from .code_evaluator import evaluate_code

# Create your views here.
def home(request):
    return render(request,"registration/index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        verify_password=request.POST['verify_password']

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name 

        myuser.save()

        messages.success(request,"Your account has been successfully")
        return redirect('signin')

    return render(request,"registration/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            first_name=user.first_name
            problems = Problem.objects.all()
            return render(request, 'problem/list.html', {'problems': problems})
        
        else:
           messages.error(request,"Bad Credentials!")
           return redirect('home') 
    return render(request,"registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem/list.html', {'problems': problems})

def submission(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    context = {'problem': problem}
    return render(request, 'problem/submission.html', context)

@login_required
def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('language')

        # Create a new submission object
        submission = Submission(problem=problem, user=request.user, code=code, language=language)
        submission.save()

        # Perform evaluation of the submission
        evaluation_result = evaluate_code(code, language)

        # Store the evaluation result in the submission object
        submission.evaluation_result = evaluation_result
        submission.save()

        # Add the evaluation result to the context
        context = {'problem': problem, 'evaluation_result': evaluation_result}

        # Render the submission page with the evaluation result
        return render(request, 'problem/submission.html', context)

    context = {'problem': problem}
    return render(request, 'problem/submission.html', context)

