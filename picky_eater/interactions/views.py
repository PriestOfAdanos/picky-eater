from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



@login_required
@require_http_methods(['POST', 'GET'])
def my_profile(request):
    current_user = request.user
    if request.method == 'POST':
        pass
    else:
        return render(request, template_name='user_profile.html', context={'user': current_user})

@login_required()
def home(request):
    return render(request, template_name='home.html')



