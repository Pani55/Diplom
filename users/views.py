import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    """ This view is designed to be used for creating a new user """
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ This method performs the function of verifying by mail each new user """
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    """ This view is designed to be used for confirming the new user's email """
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class GeneratePasswordView(PasswordResetView):
    """ This view is designed to be used for generating a new password """
    form_class = PasswordResetForm
    template_name = "users/generate.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        """ This method performs the function of generating a new password for the user """
        email = form.cleaned_data['email']
        user = get_object_or_404(User, email=email)
        if user:
            password = User.objects.make_random_password(length=8)
            user.set_password(password)
            user.save(update_fields=['password'])
            send_mail(
                subject="Восстановление пароля",
                message=f"Мы сгенерировали для вас новый пароль: {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )
        return redirect(reverse("users:login"))
