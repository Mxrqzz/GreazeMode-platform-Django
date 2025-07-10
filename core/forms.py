from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "photo",
            "category",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "input_box", "placeholder": "Nome:"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "input_box", "placeholder": "Sobrenome:"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "input_box", "placeholder": "Telefone:"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "input_box", "placeholder": "E-mail:"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "input_box",
                    "rows": 4,
                    "placeholder": "Descreva um pouco sobre você e suas experiências...",
                }
            ),
            "category": forms.Select(attrs={"class": "input_box", "placeholder": "Categoria"}),
            "photo": forms.ClearableFileInput(attrs={"class": "input_box", "accept": "image/*"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Selecione uma categoria"