from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    def __str__(self):
        return self.as_p()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'username',
                                                     'id': 'floatingInput',
                                                     'placeholder': 'username',
                                                     'for': 'floatingInput'})
        self.fields['email'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'email',
                                                  'id': 'floatingInput',
                                                  'placeholder': 'name@example.com',
                                                  'for': 'floatingInput'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'password1',
                                                      'id': 'floatingPassword',
                                                      'placeholder': '******',
                                                      'for': 'floatingPassword',
                                                      })
        self.fields['password2'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'password2',
                                                      'id': 'floatingPassword',
                                                      'placeholder': '******',
                                                      'for': 'floatingPassword'})


class AuthUserForm(AuthenticationForm):
    # email = forms.EmailField(label='email', required=True)


    def __str__(self):
        return self.as_p()

    class Meta:
        model = User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(AuthUserForm, self).__init__(*args, **kwargs)

        # self.fields['email'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'email',
        #                                           'id': 'floatingInput',
        #                                           'placeholder': 'name@example.com',
        #                                           'for': 'floatingInput'})

        self.fields['username'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'username',
                                                  'id': 'floatingInput',
                                                  'placeholder': 'Username',
                                                  'for': 'floatingInput'})

        self.fields['password'].widget.attrs.update({'class': 'form-control rounded-4', 'type': 'password',
                                                     'id': 'floatingPassword',
                                                     'placeholder': '******',
                                                     'for': 'floatingPassword',
                                                     })
