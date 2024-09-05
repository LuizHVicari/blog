from django.db import models
from django.utils.translation import gettext_lazy
from parler.models import TranslatableModel, TranslatedFields


class PersonalInfo(TranslatableModel):
    class Meta:
        verbose_name = gettext_lazy('Personal Info')
        verbose_name_plural = gettext_lazy('Personal Infos')

    name = models.CharField(max_length=50, verbose_name=gettext_lazy('name'))
    birth_date = models.DateField(verbose_name=gettext_lazy('birth date'))
    phone_number = models.CharField(max_length=15, verbose_name=gettext_lazy('phone number'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=gettext_lazy('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=gettext_lazy('updated at'))

