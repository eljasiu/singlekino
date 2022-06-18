from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
        self.fields['password1'].label = "Hasło"
        self.fields['password2'].label = "Powtórz hasło"