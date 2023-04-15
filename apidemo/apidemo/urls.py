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
from ninja import NinjaAPI, Schema

api = NinjaAPI()

class HelloSchema(Schema):
    name: str = "World"

#/api/hello?name=you => "Hello you"
# @api.get("/hello")
@api.post("/hello")
def hello(request, data: HelloSchema):# name: str):# ="World"):
    return f"Hello {data.name}" #{name}!!"

"""
/api/math?a=1&b=2 => add: 3, multiply: 2
@api.get("/math")
"""
#/api/math/1and2 => add: 3, multiply: 2
@api.get("math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
