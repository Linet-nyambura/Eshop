from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Customer
from django.views import View
from django.contrib.auth.hashers import check_password
#it handles user authentication, including login and logout.It allows users tolog in
#with their email and password, and upon successful login, it stores the customer's ID in  the session
#it also supoorts a return URL which can be used to redirect users to a specific page
#after successful login.There is alogout function to clear the user's session and log the out
#redirecting them to the login page

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def request(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'inavlid !!'

        print(email, password)
        return render(request, 'login.html' {'error': error_message})
    
    def logout(request):
        request.sessin.clear()
        return redirect('login')