from django.db import models
from django.utils.translation import gettext_lazy
from parler.models import TranslatableModel, TranslatedFields


class LevelChoices(models.TextChoices):
    BEGINNER = 'beginner', gettext_lazy('Beginner')
    INTERMEDIATE = 'intermediate', gettext_lazy('Intermediate')
    ADVANCED = 'advanced', gettext_lazy('Advanced')

class AbilityType(models.TextChoices):
    PROGRAMMING_LANGUAGE = 'programming_language', gettext_lazy('Programming Language')
    SKILL = 'skill', gettext_lazy('Skill') 
    FRAMEWORK = 'framework', gettext_lazy('Framework')
    LANGUAGE = 'language', gettext_lazy('Language')


class Ability(TranslatableModel):
    class Meta:
        verbose_name = gettext_lazy('Ability')
        verbose_name_plural = gettext_lazy('Abilities')

    key_name = models.CharField(
        max_length=50, 
        verbose_name=gettext_lazy('key name'), 
        help_text=gettext_lazy('the name that will appear on the admin page'))

    translations = TranslatedFields(
        name=models.CharField(max_length=50, verbose_name=gettext_lazy('name')),
    )
    level = models.CharField(choices=LevelChoices, max_length=20, verbose_name=gettext_lazy('level'))
    type = models.CharField(choices=AbilityType, max_length=20, verbose_name=gettext_lazy('type'))
    weight = models.IntegerField(verbose_name=gettext_lazy('weight'), help_text=gettext_lazy('order in wich it will appear on the index page'), default=0)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=gettext_lazy('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=gettext_lazy('updated at'))

    
    def __str__(self):
        return self.key_name


class PersonalInfo(TranslatableModel):
    class Meta:
        verbose_name = gettext_lazy('Personal Info')
        verbose_name_plural = gettext_lazy('Personal Infos')

    name = models.CharField(max_length=50, verbose_name=gettext_lazy('name'))

    translations = TranslatedFields(
        about_me=models.TextField(verbose_name=gettext_lazy('about me')),
        personal_life=models.TextField(verbose_name=gettext_lazy('personal life'))
    )

    abilities = models.ManyToManyField(Ability, verbose_name=gettext_lazy('abilities'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=gettext_lazy('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=gettext_lazy('updated at'))





