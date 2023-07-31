import json
import requests

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_str
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.views import View
from django.db.models import Count
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages, auth
from django.views.decorators.cache import cache_control, never_cache

from .token import generate_token
from .models.locations import Locations
from .models.feedback import Feedback
from .models.traveldesk import Traveldesk
import msg
import queries
from .regex imcontact_ust check_email, check_name


@method_decorator(never_cache, name="dispatch")
class AboutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'about_us.html', {'list': queries.cat_list})
        else:
            return HttpResponseRedirect('/login')


@method_decorator(never_cache, name="dispatch")
class Index(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html', {'list': queries.cat_list})
        else:
            return HttpResponseRedirect('/login')


@method_decorator(never_cache, name="dispatch")
class SinglePage(View):

    def get(self, request, cat):
        if request.user.is_authenticated:
            cat = queries.get_location(cat)
            return render(request, 'singlepage.html', {'data': cat, 'list': queries.cat_list, 'category': cat})
        else:
            return HttpResponseRedirect('/login')


@method_decorator(never_cache, name="dispatch")
class FeedbackView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'feedback.html', {'list': queries.cat_list})
        else:
            return HttpResponseRedirect('/login')

    def post(self, request):
        if request.user.is_authenticated:
            review = Feedback()
            review.name = request.POST.get('name')
            review.email = request.POST.get('email')
            review.review = request.POST.get('review')
            review.image = request.FILES.get('image')
            if check_name(review.name) and check_email(review.email):
                if len(review.review) > 1000:
                    messages.error(
                        request, msg.long_message)
                    return HttpResponseRedirect("/feedback")

                review.save()
                html_content = render_to_string(
                    'email_template.html', {'title': 'test email', 'content': obj.name})
                text_content = strip_tags(html_content)
                subject = "Thank you for given your feedback for Udaipur Travel Guide"
                message = text_content
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email']]
                res = EmailMultiAlternatives(
                    subject, message, email_from, recipient_list)
                res.attach_alternative(html_content, "text/html")
                result = res.send()
                if result == 1:
                    messages.error(request, message.submitted)
                    return redirect('/feedback')
                else:
                    messages.error(request, message.mail_failed)
                    return redirect('/feedback')
            else:
                messages.error(request, msg.format_error)
                return redirect('/feedback')
        else:
            return HttpResponseRedirect('/login')


@method_decorator(never_cache, name="dispatch")
class TraveldeskView(View):

    def get(self, request):
        if request.user.is_authenticated:

            return render(request, 'traveldesk.html', {'list': queries.cat_list})
        else:
            return HttpResponseRedirect('/login')

    def post(self, request):
        if request.user.is_authenticated:
            try:
                print("try")
                contact_us = Traveldesk()
                contact_us.name = request.POST.get('name')
                contact_us.email = request.POST.get('email')
                contact_us.expected_date = request.POST.get('expected_date')
                print(obj.expected_date)
                contact_us.phone = request.POST.get('phone')
                contact_us.message = request.POST.get('message')
                contact_us.number_of_person = request.POST.get('number_of_person')

                if check_name(contact_us.name) and check_name(contact_us.email):
                    if len(obj.phone) != 10:
                        messages.error(
                            request, msg.phone)
                        return redirect("/traveldesk")
                    if int(obj.number_of_person) < 1:
                        messages.error(request, msg.number_of_person)
                        return redirect("/traveldesk")
                    if len(obj.message) > 1000:
                        messages.error(
                            request, msg.long_message)
                        return HttpResponseRedirect("/traveldesk")
                    # --------------html edited mail to user----------------
                    contact_us.save()
                    html_content = render_to_string(
                        'email_template.html', {'title': 'test email', 'content': obj.name})
                    text_content = strip_tags(html_content)
                    subject = "Thank you for given your feedback for Udaipur Travel Guide"
                    message = text_content
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [request.POST['email']]
                    res = EmailMultiAlternatives(
                        subject, message, email_from, recipient_list)
                    res.attach_alternative(html_content, "text/html")
                    result = res.send()
                    if result == 1:
                        messages.error(request, message.submitted)
                        return redirect('/traveldesk')
                    else:
                        messages.error(request, message.mail_failed)
                        return redirect('/traveldesk')
                else:
                    messages.error(
                        request, msg.format_error)
                    return redirect('/traveldesk')
            except:
                return HttpResponse(status=204)
        else:
            return HttpResponseRedirect('/login')


# ------------ owner view ------------------------
@method_decorator(never_cache, name="dispatch")
class Owner(View):

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                user_approve_list = User.objects.filter(is_active=0)
                return render(request, 'owner.html', {'data': user_approve_list})
            else:
                messages.error(
                    request, msg.owner)
                return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')
# -------------------owner view ends here --------------------


# ------------------ user approve view ------------------------

@method_decorator(never_cache, name="dispatch")
class Approve(View):

    def get(self, request, id):
        if request.user.is_authenticated:
            user = User()
            user = User.objects.filter(id=id).first()
            user.is_active = True
            user.save()
            user_approve_list = User.objects.filter(is_active=0)

            return render(request, 'owner.html', {'data': user_approve_list})
        else:
            return HttpResponseRedirect('/login')


@method_decorator(never_cache, name="dispatch")
class SignUp(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        obj = User()
        username = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')


        if check_name(name) and check_email(email):

            if User.objects.filter(username=username):
                messages.error(request, msg.already_user)
                return HttpResponseRedirect("/signup")
            if User.objects.filter(email=email):
                messages.error(request, msg.already_email)
                return redirect("/signup")
            if password1 != password2:
                messages.error(request, msg.no_match)
                return redirect("/signup")
            if len(password1) < 8:
                messages.error(request, msg.short_pswrd)
                return redirect("/signup")

            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeAePQhAAAAAAk3SwpToCu_WHgVj5zZJIIcKQ_P'
            captchaData = {
                'secret': secretKey,
                'response': clientKey
            }
            res = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(res.text)
            verify = response['success']
            if verify:
                obj = User.objects.create_user(
                    username=username, email=email, password=password1, is_active=False)
                obj.save()
                messages.success(
                    request, msg.activation)
            # welcome email
                subject = " confirmation link for Udaipur Travel Guide"
                message = "hey!!" + obj.username + \
                    "welcome to Udaipur Travel Guide. please approve the email confirmation"

                to_list = obj.email
                send_mail(subject, message,
                          settings.EMAIL_HOST_USER, [to_list])

                # confirmation email using tokens
                current_site = get_current_site(request)
                email_subject = "confirm your email"
                message2 = render_to_string('activation.html', {
                    'name': obj.username,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
                    'token': generate_token.make_token(obj),
                })
                send_mail(email_subject, message2,
                          settings.EMAIL_HOST_USER, [to_list])
                return HttpResponseRedirect("/login")
            else:
                messages.error(
                    request, msg.captcha)
                return render(request, 'signup.html')
        else:
            messages.error(
                request, msg.error_entry)
            return render(request, 'signup.html')


def activate(request, uid64, token):
    User = get_user_model()

    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        new_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        new_user = None
    if new_user is not None and generate_token.check_token(new_user, token):
        new_user.is_active = True
        new_user.save()
        messages.error(request, msg.verified)
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')


@method_decorator([cache_control(private=True)], name="dispatch")
class SignIn(View):

    @method_decorator([cache_control(private=True)], name="dispatch")
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')

    @method_decorator([cache_control(private=True)], name="dispatch")
    def post(self, request):
        if request.user.is_authenticated:
            return render(request, 'index.html')
        else:
            username = request.POST['name']
            password1 = request.POST['password1']
            active = User.objects.filter(username=username).first()
            if active is None:
                messages.error(request, msg.no_such_user)
                return HttpResponseRedirect('/login')
            if active.is_active == False:
                messages.error(request, msg.under_review)
                return HttpResponseRedirect("/login")
            clientKey = request.POST['g-recaptcha-response']
            secretKey = '6LeAePQhAAAAAAk3SwpToCu_WHgVj5zZJIIcKQ_P'
            captchaData = {
                'secret': secretKey,
                'response': clientKey
            }
            res = requests.post(
                'https://www.google.com/recaptcha/api/siteverify', data=captchaData)
            response = json.loads(res.text)
            verify = response['success']
            if verify:
                user = authenticate(
                    request, username=username, password=password1)
                if user is not None:
                    request.session['username'] = username
                    auth.login(request, user)
                    return redirect('/index')
                else:
                    messages.error(request, msg.error_entry)
                    return redirect('/login')
            else:
                messages.error(request, msg.captcha)
                return redirect('/login')


class SignOut(View):

    @method_decorator([cache_control(private=True)], name="dispatch")
    def get(self, request):
        try:
            auth.logout(request)
            del request.session['username']
        except Exception as e:
            print(e)
        messages.error(request, msg.logged_out)
        return HttpResponseRedirect("/login")


class MessageView(View):

    def get(self, request):
        messages.success(request, msg.logged_out)
        return render(request, 'message.html')
