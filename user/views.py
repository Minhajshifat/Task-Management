from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, get_user_model, logout
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            token = default_token_generator.make_token(user)
            print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            print("uid ", uid)
            confirm_link = (
                f"https://task-management-xchz.onrender.com//user/active/{uid}/{token}"
            )
            email_subject = "Confirm Your Email"
            email_body = render_to_string(
                "acc_active_email.html", {"confirm_link": confirm_link}
            )

            email = EmailMultiAlternatives(email_subject, "", to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            messages.success(request, "confirm your email for verifiacation")
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "registation.html", {"form": form})


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except User.DoesNotExist:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("login")
    else:
        return redirect("register")


class UserLoginView(LoginView):
    template_name = "login.html"

    def get_success_url(self):
        messages.success(self.request, "Logged in successfully")
        return reverse_lazy("showtask")


def userLogout(request):
    logout(request)
    return redirect("home")
