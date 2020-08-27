from django.contrib.auth import get_user_model
import django.contrib.auth.forms as form

class UserCreateForm(form.UserCreationForm):
    class Meta:
        fields= ('username', 'email', 'password1','password2' )
        model= get_user_model()

        def __init__(self,*args,**kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'
            self.fields['email'].label = 'Email Address'
            
