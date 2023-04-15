"""
URL configuration for apidemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from ninja import NinjaAPI, Schema
from testCRUD.api import api

# api = NinjaAPI()

# class HelloSchema(Schema):
#     name: str = "World"

# Can't use
# class UserSchema(Schema):
#     username: str
#     is_authenticated: bool
#     email: str = None
#     first_name: str = None
#     last_name: str = None

# @api.get("/me", response=UserSchema)
# def me(request):
#     return request.user

# class UserSchema(Schema):
#     username: str
#     is_authenticated: bool = True#False
#     email: str
#     first_name: str
#     last_name: str

# class Error(Schema):
#     message: str

# @api.get("/me", response={200: UserSchema, 403: Error})
# def me(request):
#     user = UserSchema(username="pmikada", email="test@example.com", first_name="Panupong", last_name="Mikada")
#     if not user.is_authenticated:
#         return 403, {"message": "Please sign in first"}
#     return user

#/api/hello?name=you => "Hello you"
# @api.get("/hello")
# @api.post("/hello")
# def hello(request, data: HelloSchema):# name: str):# ="World"):
#     return f"Hello {data.name}" #{name}!!"

"""
/api/math?a=1&b=2 => add: 3, multiply: 2
@api.get("/math")
"""
#/api/math/1and2 => add: 3, multiply: 2
# @api.get("math/{a}and{b}")
# def math(request, a: int, b: int):
#     return {"add": a + b, "multiply": a * b}

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("api/", api.urls),
    path('api/', api.urls)
]
