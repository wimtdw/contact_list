from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import User
import json
   

    
@csrf_exempt
def manage_contacts(request):
    # Create a new record using the model's constructor.
    # record = User(username="user_user", email="email", mobile='89109102121')
    # # Save the object into the database.
    # record.save()
    # record = User(username="Taylor Swift", email="taylorswift@email.com", mobile='123123123')
    # record.save()
        
    if request.method == 'POST':
        username = request.POST.get('username')  # Replace 'field1' with your actual field names
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        # Create a new instance of your model
        new_contact = User(username=username, email=email, mobile=mobile)
        # Save the new entry to the database
        new_contact.save()
        message='New contact saved successfully!'
        context = {'message': message}
        template = 'result.html'
        return render(request, template, context)
    elif request.method == 'DELETE':
        all_users = User.objects.all()
        for user in all_users:
            user.delete()
        message='Contacts deleted successfully!'
        context = {'message': message}
        template = 'result.html'
        return render(request, template, context)
    all_users = User.objects.all()
    template = 'contacts.html'
    context = context = {'objects': all_users}
    return render(request, template, context)
    
@csrf_exempt
def contact_detail(request, user_id):
   
    if request.method == 'GET':
        try:
            entry = User.objects.get(id=user_id) 
        except User.DoesNotExist:
            message = 'Contact with this id doesn\'t exist'
            context = {'message': message}
            template = 'result.html'
            return render(request, template, context)
        # contact = get_object_or_404(User, id=user_id)
        context = {'contact': entry}
        template = 'contact_detail.html'
        return render(request, template, context)

    elif request.method == 'DELETE':
        message =''
        try:
            entry = User.objects.get(id=user_id) 
        except User.DoesNotExist:
            message = 'Contact with this id doesn\'t exist'
        else:
            entry.delete()
            message='Entry with ID '+ str(user_id) + ' deleted successfully'
        context = {'message': message}
        template = 'result.html'
        return render(request, template, context)
    
    if request.method == 'PUT':
        try:
            entry = User.objects.get(id=user_id) 
        except User.DoesNotExist:
            message = 'Contact with this id doesn\'t exist'
            context = {'message': message}
            template = 'result.html'
            return render(request, template, context)
            # contact = get_object_or_404(User, id=user_id)
        data = json.loads(request.body.decode('utf-8'))
        entry.username = data.get('username', entry.username)
        entry.email = data.get('email', entry.email)
        entry.mobile = data.get('mobile', entry.mobile)
        entry.save()
        context = {'contact': entry}
        template = 'contact_detail.html'
        return render(request, template, context)
    
    