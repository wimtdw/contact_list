from django.shortcuts import redirect, render
from contact.forms import UserForm
from .models import User


def manage_contacts(request):
    all_users = User.objects.all()
    if request.method == 'POST':
        message = ''
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'delete':
                for user in all_users:
                    user.delete()
                message = 'Contacts deleted successfully!'
            context = {'message': message}
            template = 'result.html'
            return render(request, template, context)
    template = 'contacts.html'
    context = context = {'objects': all_users}
    return render(request, template, context)


def contact_detail(request, user_id):
    if request.method == 'GET':
        try:
            entry = User.objects.get(id=user_id)
        except User.DoesNotExist:
            message = 'Contact with this id doesn\'t exist'
            context = {'message': message}
            template = 'result.html'
            return render(request, template, context)
        context = {'contact': entry}
        template = 'contact_detail.html'
        return render(request, template, context)
    if request.method == 'POST':
        message = ''
        if 'action' in request.POST:
            action = request.POST['action']
            if action == 'delete':
                try:
                    entry = User.objects.get(id=user_id)
                    username = entry.username
                except User.DoesNotExist:
                    message = 'Contact with this id doesn\'t exist'
                else:
                    entry.delete()
                    message = 'Contact "' + username + '" deleted successfully'
        context = {'message': message}
        template = 'result.html'
        return render(request, template, context)


def user_update(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        if request.method == 'POST':
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('contact:contact_detail', user.id)
        else:
            form = UserForm(instance=user)
    except User.DoesNotExist:
        message = 'Contact with this id doesn\'t exist'
        context = {'message': message}
        template = 'result.html'
        return render(request, template, context)
    context = {'contact': user, 'form': form}
    template = 'contact_form.html'
    return render(request, template, context)


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('contact:contact_detail', user.id)
    else:
        form = UserForm()
    context = {'form': form}
    template = 'contact_form.html'
    return render(request, template, context)


def delete_all(request):
    all_users = User.objects.all()
    for user in all_users:
        user.delete()
    message = 'Contacts deleted successfully!'
    context = {'message': message}
    template = 'result.html'
    return render(request, template, context)
