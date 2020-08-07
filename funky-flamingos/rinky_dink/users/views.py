import hashlib
import os
# import random

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

from users.forms import RegistrationForm, TeamRegistrationForm
from users.models import File, Member


def fhandler(request, name):
    path = "/".join(os.path.dirname(os.path.realpath(__file__)).split("/")[:-1])
    new_path = path + '/media/' + name
    with open(new_path, 'rb') as f:
        text = f.read()
        print(text)

    return render(request, 'users/file.html', {'text': text.decode('utf-8')})


def index(request):
    return render(request, "users/index.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.save())
            messages.success(request, "You have been successfully registered!")
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "users/register.html", {"form": form})


@login_required(login_url="/login/")
def teamregister(request):
    if request.method == "POST":
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form.instance.members.add(request.user)
            print(form.save())
            messages.success(request, "Your team has been successfully registered!")
            return redirect("dashboard")
    else:
        form = TeamRegistrationForm()

    return render(request, "users/team.html", {"form": form})


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect("login")
    return render(request, "users/login.html")


@login_required(login_url="/login/")
def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES["document"]
        if not check_title_presence(uploaded_file):
            messages.success(request, "New file save successfully.")
            path = save_on_server(uploaded_file)
            hash_val = hash_file(path)
            form = File(title=uploaded_file.name, hash_val=hash_val, user=request.user)
            form.save()
        else:
            # flash message that A similar file is already present  if hash value matches
            path = save_on_server(uploaded_file)
            hash_val = hash_file(path)
            if check_file_presence(hash_val):
                messages.warning(request, "A similar file is already present")
                os.remove(path)

            # hash value matches so no need to upload. if not, uploade it with different file name
            else:
                # save file on server with new name{version}
                title = path.split("/")[-1]
                form = File(title=title, hash_val=hash_val, user=request.user)
                form.save()
                messages.warning(
                    request,
                    "file with same name is already present adding it with new version ",
                )

    return render(request, "users/upload.html", context)


@login_required(login_url="/login/")
def dashboard(request):
    teams = Member.objects.filter(user__id__in=[request.user.id])
    context = {}
    file = File.objects.filter(user=request.user).order_by("-uploaded_at")[:5]
    context = {"file": file, "teams": teams}
    print(context["file"])
    print(context["teams"])
    return render(request, "users/dashboard.html", context)


def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return render(request, "users/logout.html")


def hash_file(filename):
    """"This function returns the SHA-1 hash
    of the file passed into it"""

    # make a hash object
    h = hashlib.sha1()
    with open(filename, "rb") as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b"":
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)

    # return the hex representation of digest
    return h.hexdigest()


def check_title_presence(uploaded_file):
    """
    query database for filename and if it is present then return True else return False
    """
    file = File.objects.filter(title=uploaded_file)
    if file:
        return True
    return False


def check_file_presence(hash_val):
    """
    checks if a file exists with the same hash value
    """
    file = File.objects.filter(hash_val=hash_val)
    if file:
        return True
    return False


def save_on_server(uploaded_file):
    """
    this method saves the file, using a new unique name if already present
    """
    fs = FileSystemStorage()
    name = fs.save(uploaded_file.name, uploaded_file)
    url = fs.url(name)
    path = "/".join(os.path.dirname(os.path.realpath(__file__)).split("/")[:-1])
    return path + url
