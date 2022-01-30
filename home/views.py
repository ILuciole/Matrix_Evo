from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.
from django.template import loader



def start_page(request):
    html_message = loader.render_to_string('message.html')
    form = UsersForm()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('user_email')
        if Users.objects.filter(user_email=email):
            messages.error(request, f'Вже бачилися, {name}')
        else:
            form = UsersForm(request.POST)
            if form.is_valid():
                email = form.save(commit=False)
                email.users_email = email.user_email.lower()
                email.save()
                messages.success(request, f'Привіт, {name}! Перевір свою пошту!')
                email = form.cleaned_data['user_email']
                try:
                    send_mail('Need your help!', "", 'MatrixEvo@gmail.com',
                              [email],  fail_silently=False, html_message=html_message)
                finally:
                    return redirect('home')
    return render(request, 'home/index.html', {'form': form})


def users_base(request):
    data = Users.objects.all()
    return render(request, 'home/done.html', {'data': data})


#######################################################################
# def login_page(request):
#     form = UsersForm()
#     if request.method == 'POST':
#         email = request.POST.get('user_email')
#         try:
#             email = Users.objects.get(user_email=email)
#             messages.error(request, f'какая то ошибка')
#         except:
#             messages.error(request, f'Вже бачилися, {email}')
#
#     context = {'form': form}
#     return render(request, 'home/send.html', context)


# def register_user(request):
#     form = UsersForm()
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             email = form.save(commit=False)
#             email.users_email = email.user_email.lower()
#             email.save()
#     return render(request, 'home/send.html', {'form': form})


# def home(request):
#     form = UsersForm()
#     if request.method == 'POST':
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('done')
#     context = {'form': form}
#     return render(request, 'home/index_old.html', context)


# def send_email(request):
#     # если метод GET, вернем форму
#     if request.method == 'GET':
#         form = ContactForm()
#     elif request.method == 'POST':
#         # если метод POST, проверим форму и отправим письмо
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             from_email = form.cleaned_data['from_email']
#             try:
#                 send_mail('Test', 'Test message.', 'MatrixEvo@gmail.com',
#                           [from_email], fail_silently=False)
#             except BadHeaderError:
#                 return HttpResponse('Ошибка в теме письма.')
#             return redirect('home')
#     else:
#         return HttpResponse('Неверный запрос.')
#     return render(request, "home/send.html", {'form': form})