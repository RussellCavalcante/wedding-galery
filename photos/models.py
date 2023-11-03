from django.db import models

class Photos(models.Model):
    imagem= models.ImageField(upload_to='casamento_imagens/%Y/%m/', blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True, null=True)
    usuario_dono = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    visivel = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nome

class CommentPhotos(models.Model):
    photos = models.ForeignKey(Photos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    comentario = models.TextField()
    visivel = models.IntegerField()
    
    def __str__(self):
        return self.nome or self.produto.nome