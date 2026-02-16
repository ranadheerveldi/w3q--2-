from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User   # ⭐ ADD THIS
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm


# ---------------- HOME PAGE ----------------
def home(request):
    return render(request, "myfirst.html")


# ---------------- SIGNUP ----------------
def signup_view(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Check empty fields
        if not username or not password:
            error = "All fields are required"

        # Check if user already exists
        elif User.objects.filter(username=username).exists():
            error = "User already exists"

        else:
            # Create user (Password automatically hashed)
            User.objects.create_user(username=username, password=password)
            return redirect('login')

    return render(request, "signup.html", {"error": error})


# ---------------- ADD MEMBER ----------------
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MemberForm()

    return render(request, 'add_member.html', {'form': form})


# ---------------- SUCCESS PAGE ----------------
def success(request):
    return render(request, 'success.html')


# ---------------- VIEW ALL MEMBERS ----------------
def members(request):
    mymembers = Member.objects.all()
    return render(request, 'all_members.html', {'mymembers': mymembers})


# ---------------- MEMBER DETAILS ----------------
def details(request, id):
    try:
        mymember = Member.objects.get(id=id)
    except Member.DoesNotExist:
        return HttpResponse("Member not found")

    return render(request, 'details.html', {'mymember': mymember})


# ---------------- FORM TEST ----------------
def form_view(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('your_name')

    return render(request, "form.html")


# ---------------- LOGIN ----------------
def login_view(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('members')
        else:
            error = "Invalid username or password"

    return render(request, "login.html", {"error": error})


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect('login')
