from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        
        model = get_user_model() # 유지보수가 더 편한 방법 
        # model = User
        fields = ('username', 'profile_image', )