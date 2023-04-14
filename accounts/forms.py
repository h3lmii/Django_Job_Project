from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
	class Meta(UserCreationForm):
		model=CustomUser
		fields=("first_name","last_name","email","resume",)
class UserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields=("first_name","last_name","email","resume",)



class ApplyForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=("first_name","last_name","email","resume")


