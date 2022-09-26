from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()


def getAll():
    return User.objects.all()

def createUser(request):
    User.objects.create(
        first_name=request.POST["first"],
        last_name=request.POST["last"],
        email_address=request.POST["email"],
        age=request.POST["age"],
    )

# def isAuthenticated(request):
#     if request.session["loodegd"] == 1:
#         return True
#     else:
#         return False
