from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django import forms


class UserForm(forms.ModelForm):
    # automatically select password as a inputtype so forms.PasswordInput
    password = forms.CharField(widget= forms.PasswordInput)
    # if we want to select multiple choices then ModelMultipleChoiceField and if only one choice needed then ModelChoiceField
    role = forms.ModelChoiceField(queryset= Group.objects.all())

     # Here form didn't recognize the password field so we have done as above, this also tends to charfield but inside (it denotes that this is password input)
    #  and when this form is called it will automatically recognize the password field

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        # excludes = ['']
        label = {
            'password' : 'Password'
        }

        # if you want other validation like @shreeraj.com you should do like this
        # Custom Validation
        # def clean_email(self):
        #     if self.cleaned_data['email'].endsWith('@shreeraj.com'):
        #         return self.cleaned_data['email']
        #     else:
        #         raise ValidationError("Email id is not valid")
        #

        # if you didn't define this save method then password will set as in row format which is not valid
        # so to get in required format we do like this

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
    # we get the 'initial' keyword argument or initialize it
    # as a dict if it didn't exist
            initial = kwargs.setdefault('initial', {})
    # The widget for a ModelMultipleChoiceField expects
    # a list of primary key for the selected data
            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None

        forms.ModelForm.__init__(self, *args, **kwargs)





    def save(self):
        password = self.cleaned_data.pop('password')
        role = self.cleaned_data.pop('role')
        u = super().save()
        u.groups.set([role])
        u.set_password(password)
        u.save()
        return u

