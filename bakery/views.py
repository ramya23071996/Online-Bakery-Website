from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegisterForm, CustomLoginForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def login(request):
    reg_form = RegisterForm()
    login_form = CustomLoginForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            reg_form = RegisterForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                messages.success(request, "Account created successfully! Please login.")
                return redirect('login')

        elif 'login' in request.POST:
            login_form = CustomLoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = authenticate(
                    request,
                    username=login_form.cleaned_data['username'],
                    password=login_form.cleaned_data['password']
                )
                if user:
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, "Invalid credentials")

    return render(request, 'bakery/login.html', {
        'reg_form': reg_form,
        'login_form': login_form
    })


def logout_user(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'bakery/home.html')


def about(request):
    return render(request, 'bakery/about.html')

def cakes(request):
    return render(request, 'bakery/cakes.html')

def products(request):
    q = request.GET.get('q', '')
    ctx = {'q': q}
    return render(request, 'bakery/products.html', ctx)


def blog(request):
    return render(request, 'bakery/blog.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_message = form.save()
            
            # Send email to admin (optional)
            try:
                subject = f"New Contact Form Submission: {form.cleaned_data['subject']}"
                message = f"""
                New message from contact form:
                
                Name: {form.cleaned_data['name']}
                Email: {form.cleaned_data['email']}
                Phone: {form.cleaned_data['phone_number']}
                Subject: {form.cleaned_data['subject']}
                
                Message:
                {form.cleaned_data['message']}
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],  # Define this in settings.py
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Your message has been sent successfully! We will get back to you within 24 hours.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'bakery/contact.html', {'form': form})