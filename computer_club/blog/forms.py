from contextlib import nullcontext
from django.forms import ModelForm
from blog.models import *
from django import forms
import datetime
class RegisterForm(ModelForm):
    class Meta:
        model = User
        isUsing = 0
        order = None
        payment = None
        fields = ["name", "passw"]
        print("here")
    def save(self, commit=True):
        print("here1")
        user = super(RegisterForm, self).save(commit=False)
        user.isusing = 0
        if commit:
            user.save()
        return user
# class LoginForm(ModelForm):
#     class Meta:
#         model = User
#         isUsing = 0
#         order = None
#         payment = None
#         fields = ["name", "passw"]
#         print("here3")

class LoginForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ),error_messages={
               'required': 'The username field is required.'
        })
    passw = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ),error_messages={
               'required': 'The password field is required.'
        })
    # isUsing = 0

class CCCModelForm(forms.Form):
    queryset=Computer.objects.select_related('computer_club')
    print(queryset)
    item_name = forms.ModelChoiceField(
        label="Item Choices", queryset=queryset, required=True
    )

class TimePickerInput(forms.TimeInput):
    input_type = 'time'


t = [
    ("2022-11-15 00:00:00.000000-00:00",'00:00:00'),
    ("2022-11-15 01:00:00.000000-00:00",'01:00:00'),
    ("2022-11-15 02:00:00.000000-00:00",'02:00:00'),
    ("2022-11-15 03:00:00.000000-00:00",'03:00:00'),
    ("2022-11-15 04:00:00.000000-00:00",'04:00:00'),
    ("2022-11-15 05:00:00.000000-00:00",'05:00:00'),
    ("2022-11-15 06:00:00.000000-00:00",'06:00:00'),
    ("2022-11-15 07:00:00.000000-00:00",'07:00:00'),
    ("2022-11-15 08:00:00.000000-00:00",'08:00:00'),
    ("2022-11-15 09:00:00.000000-00:00",'09:00:00'),
    ("2022-11-15 10:00:00.000000-00:00",'10:00:00'),
    ("2022-11-15 11:00:00.000000-00:00",'11:00:00'),
    ("2022-11-15 12:00:00.000000-00:00",'12:00:00'),
    ("2022-11-15 13:00:00.000000-00:00",'13:00:00'),
    ("2022-11-15 14:00:00.000000-00:00",'14:00:00'),
    ("2022-11-15 15:00:00.000000-00:00",'15:00:00'),
    ("2022-11-15 16:00:00.000000-00:00",'16:00:00'),
    ("2022-11-15 17:00:00.000000-00:00",'17:00:00'),
    ("2022-11-15 18:00:00.000000-00:00",'18:00:00'),
    ("2022-11-15 19:00:00.000000-00:00",'19:00:00'),
    ("2022-11-15 20:00:00.000000-00:00",'20:00:00'),
    ("2022-11-15 21:00:00.000000-00:00",'21:00:00'),
    ("2022-11-15 22:00:00.000000-00:00",'22:00:00'),
    ("2022-11-15 23:00:00.000000-00:00",'23:00:00'),
]

class OrderCreationForm(forms.ModelForm):
    # date_start = forms.ChoiceField(choices=times)
    # date_start = forms.TimeField(widget=TimePickerInput)
    time = []
    for i in range(len(t)):
        h,m,s = t[i][1].split(":")
        date = datetime.datetime.combine(datetime.date.today(),datetime.time(hour=int(h),minute=int(m),second=int(s)))
        true_date =  str(date.date()) + t[i][0][10::]
        time.append((true_date,date))


    date_start = forms.ChoiceField(
                        required=True,
                        choices=time,
                        widget=forms.Select(
                            attrs={'OrderTable': 'date_start',}
                       ))
    # date_start = forms.SelectDateWidget()
    class Meta:
        model = OrderTable
        # fields = "__all__"
        fields = ["computer_club","computer","date_start"]
        
        
    def __init__(self, *args, **kwargs):
        time = []
        for i in range(len(t)):
            h,m,s = t[i][1].split(":")
            date = datetime.datetime.combine(datetime.date.today(),datetime.time(hour=int(h),minute=int(m),second=int(s)))
            true_date =  str(date.date()) + t[i][0][10::]
            time.append((true_date,date))
        super().__init__(*args, **kwargs)
        self.fields['computer_club'].queryset = ComputerClub.objects.all()
        
        self.fields['computer'].queryset = Computer.objects.none()
        self.fields['date_start'].queryset = forms.ChoiceField(choices=time)
        if 'computer_club_id':
            try:
                # print("rphr")
                comp_club_id = int(self.data.get('computer_club'))
                self.fields['computer_club'].queryset = ComputerClub.objects.filter(id=comp_club_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        if "computer":
            try:
                comp_id = int(self.data.get('computer'))
                self.fields['computer'].queryset = Computer.objects.filter(id=comp_id).order_by('isworking')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        if "date_start":
            try:
                print("mi tut")
                # print(self.data)
                date_start = self.data.get('date_start')
                print(date_start)
                print(" i tut")
                if date_start is not None:
                    print("slomavsya")
                    # date_start = date_start.split(" ")
                    # if date_start[1][0] == 'a':
                    #     date_start = datetime.time(hour = int(date_start[0]), minute=0,second=0)
                    # else:
                    #     date_start = datetime.time(hour = 12+ int(date_start[0]), minute=0,second=0)
                    # date_start = datetime.datetime.combine(datetime.date.today(),date_start)
                    # a = str(datetime.datetime.combine(datetime.date.today(),times[int(date_start)][1]))
                    # print(str(a) + ".000000-00:00")
                    # self.fields['date_start'].queryset= a
                    # self.fields['date_start'].queryset= datetime.datetime.strptime(times[date_start][1], "YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
                    print("here is us")

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['Computer'].queryset = self.instance.country.city_set.order_by('isworking')

    def save(self, commit=True):
        print("here10")
        order = super(OrderCreationForm, self).save(commit=False)
        order.date_end = order.date_start + datetime.timedelta(hours=1)
        if commit:
            order.save()
        return order