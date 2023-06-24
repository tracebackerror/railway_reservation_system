from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from .utils import getRailwayRates, getTrainData
from .models import *
from .forms import *

    
class Login(LoginView):
    template_name = "login.html"
    formclasss = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("shipping")
        return super().get(request, *args, **kwargs)


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/login/")


class Register(CreateView):
    template_name = 'register.html'
    model = User
    formclasss = RegisterForm
    success_url = "/login/"



class BookTicket(LoginRequiredMixin, TemplateView):
    template_name = 'book_ticket.html'
    login_url = "/login/"
    extra_context = {}

    def get(self, request, *args, **kwargs):
        self.extra_context["name"] = request.user.first_name
        self.extra_context["mobile_no"] = ""
        self.extra_context["source"] = ""
        self.extra_context["destination"] = ""
        self.extra_context["date"] = ""
        self.extra_context["classs"] = ""
        self.extra_context["fare"] = None
        self.extra_context["train_list"] = getTrainData()
        self.extra_context["classes"] = CLASSES_CHOICES
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        post_data = self.request.POST.dict()
        action = post_data.pop("action")
        del post_data["csrfmiddlewaretoken"]
        if action == "book":
            shipment_obj = Booking.objects.create(booked_by=request.user,**post_data)
            return redirect(f"/pnr-status/?pnr={shipment_obj.pnr}")
        else:
            fare = getRailwayRates(post_data["source"],post_data["destination"],post_data["classs"])
            self.extra_context["fare"] = fare    
        self.extra_context["classes"] = CLASSES_CHOICES
        self.extra_context["train_list"] = getTrainData()
        self.extra_context.update(self.request.POST.dict())
        return super().get(request, *args, **kwargs)
        


class PNRStatus(TemplateView):
    template_name = 'pnr_status.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        pnr = request.GET.get("pnr")
        booking = Booking.objects.filter(pnr=pnr)
        if booking:
            booking = booking.first()
        self.extra_context["booking"] = booking
        return super().get(request, *args, **kwargs)
    

class FareCalculator(TemplateView):
    template_name = 'fare_calculator.html'
    extra_context = {}

    def get(self, request, *args, **kwargs):
        self.extra_context["classes"] = CLASSES_CHOICES
        self.extra_context["train_list"] = getTrainData()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        post_data = self.request.POST.dict()
        fare = getRailwayRates(post_data["source"],post_data["destination"],post_data["classs"])
        self.extra_context["fare"] = fare
        self.extra_context["classes"] = CLASSES_CHOICES
        self.extra_context["train_list"] = getTrainData()
        self.extra_context.update(post_data)
        return super().get(request, *args, **kwargs)