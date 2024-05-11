from django.conf import settings
from django.db import models
from django.utils import timezone   #Todas as linhas começando com from ou import são linhas que adicionam pedaços de outros arquivos.


class Post(models.Model):   # esta linha define o nosso modelo (é um objeto).
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):  #def significa que se trata de uma função/método e que publish é seu nome.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# models.CharField - é assim que definimos um texto com um número limitado de caracteres.
# models.TextField - este campo é para textos sem um limite fixo. Parece ideal para o conteúdo de um blog, né?
# models.DateTimeField - este é uma data e hora.
# models.ForeignKey - este é um link para outro modelo.
