from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfileForm


# Create your views here.
def index(request):
    return render(request, "core/home.html")


def register(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        password = request.POST.get("password")
        password_confirm = request.POST.get("passwordConfirm")
        email = request.POST.get("email")

        if password != password_confirm:
            messages.error(request, "As senhas não coincidem,")
            return render(request, "core/register.html", {"form": form})

        if form.is_valid():
            # Cria o usuario
            try:
                user = User.objects.create_user(
                    
                    username=form.cleaned_data["email"],
                    email=form.cleaned_data["email"],
                    password=password,
                    first_name =form.cleaned_data['first_name'],
                    last_name =form.cleaned_data['last_name']
                )
                # Salva o perfil associado ao usuario
                profile = form.save(commit=False)
                profile.owner = user
                profile.save()
                messages.success(request, "Conta criada com sucesso!")
                return redirect("ok")
            except ValueError as e:
                messages.error(request, f"Erro ao criar usuario {e}")
        else:
            messages.error(request, "Por favor corrija os erros no formulário.")
    else:
        form = ProfileForm()

    return render(request, "core/register.html", {"form": form})

def login(request):
    return render(request, 'core/login.html')

def ok(request):
    return render(request, 'core/ok.html')
