from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import PersonalInfo, AbilityType, Ability, LevelChoices


def home(request, *args, **kwargs):

    infos = PersonalInfo.objects.order_by('-updated_at').first()

    programming_languages = infos.abilities.filter(
        type=AbilityType.PROGRAMMING_LANGUAGE
    ).order_by('-weight')
    skills = infos.abilities.filter(
        type=AbilityType.SKILL
    ).order_by('-weight')
    frameworks = infos.abilities.filter(
        type=AbilityType.FRAMEWORK
    ).order_by('-weight')
    languages = infos.abilities.filter(
        type=AbilityType.LANGUAGE
    ).order_by('-weight')

    context = {
        'name': infos.name,
        'about_me': infos.about_me,
        'personal_life': infos.personal_life,
        'programming_languages': programming_languages,
        'skills': skills,
        'frameworks': frameworks,
        'languages': languages
    }

    return render(request, 'core/index.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('core:home')