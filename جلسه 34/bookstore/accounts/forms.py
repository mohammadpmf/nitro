from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', )
        """
        به صورت پیش فرض، فیلد هایی که اضافه میکنه موقع ساخت فرم، یوزرنیم هست.
        ما اینجا سن رو هم اضافه کردم. پسورد 1 و پسورد 2 هم که باید باشه. اونا دست ما نیست.
        حالا میتونیم این شکلی هم بنویسیمش:
        برای فرم تغییر هم میشه گذاشت.
        """
        # fields = ("age", "username", "email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        # fields = ("age", "username", "email",)
