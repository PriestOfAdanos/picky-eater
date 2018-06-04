from django.http import HttpResponse
from django.shortcuts import render
from .forms import SignupForm, UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from picky_eater.settings import AUTH_USER_MODEL
from .models import Restaurant


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('email_confirmation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = AUTH_USER_MODEL.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, AUTH_USER_MODEL.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        user.login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def restaurant_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.is_active = False
            restaurant.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('email_confirmation.html', {
                'restaurant': restaurant,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(restaurant.pk)),
                'token': account_activation_token.make_token(restaurant),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreationForm
    return render(request, 'signup.html', {'form': form})


def restaurant_activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        restaurant = Restaurant.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, AUTH_USER_MODEL.DoesNotExist):
        restaurant = None

    def check_nip(nip):

        return True

    if restaurant_activate() is not None\
            and account_activation_token.check_token(restaurant, token)\
            and check_nip(restaurant.NIP) is True:
        restaurant_activate().is_active = True
        restaurant_activate().save()
        restaurant_activate().login(request, restaurant_activate())
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')