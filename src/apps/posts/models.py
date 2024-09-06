from django.db import models
from django.utils.translation import gettext_lazy
from parler.models import TranslatableModel, TranslatedFields


class PostType(models.TextChoices):
    PORTFOLIO = 'portfolio', gettext_lazy('Portfolio')
    PROJECTS = 'projects', gettext_lazy('Projects')
    ACADEMIC = 'academic', gettext_lazy('Academic')


class Post(TranslatableModel):

    cover_image = models.ImageField(verbose_name=gettext_lazy('cover image'))
    
    translations = TranslatedFields(
        description = models.TextField(verbose_name=gettext_lazy('description')),
        text=models.TextField(verbose_name=gettext_lazy('text')),
        title=models.CharField(max_length=150, verbose_name=gettext_lazy('title')),
        category=models.CharField(max_length=50, verbose_name=gettext_lazy('category'))
    )

    post_type = models.CharField(max_length=10, verbose_name=gettext_lazy('type'), choices=PostType)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=gettext_lazy('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=gettext_lazy('updated at'))


    def __str__(self):
        return self.title
    
    
    @property
    def translated_post_type(self):
        match self.post_type:
            case PostType.PORTFOLIO:
                return gettext_lazy('Portfolio')
            case PostType.PROJECTS:
                return gettext_lazy('Projects')
            case PostType.ACADEMIC:
                return gettext_lazy('Academic')
    
