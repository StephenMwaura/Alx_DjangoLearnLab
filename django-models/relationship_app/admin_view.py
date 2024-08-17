from  django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

def is_Admin(user):
    return user.is_authenticated and user.groups.filter(name='Admin').exists()
@user_passes_test(is_Admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin")

