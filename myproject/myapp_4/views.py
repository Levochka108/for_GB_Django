import logging

from django.shortcuts import render

from .forms import UserForm

logger = logging.getLogger(__name__)

def user_form(requeast):
    if requeast.method == 'POST':
        form = UserForm(requeast.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.changed_data['email']
            age = form.cleaned_data['age']

            logger.info(f'Получили {name=}, {email=}, {age=}')
        
    else:
        form = UserForm()
    return render(requeast, 'myapp_4/user_form.html', {'form': form})

