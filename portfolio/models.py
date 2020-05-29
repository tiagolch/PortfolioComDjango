from django.db import models


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=50, null=False, blank=False, verbose_name='Tecnologias')

    class Meta:
        db_table = 'tecnolgias'

    def __str__(self):
        return self.tecnologia

###  Verificar a relação do campo tecnologias

class Projetos(models.Model):
    nome_projeto = models.CharField(max_length=100, blank=False, null=False, verbose_name='Projeto')
    descricao = models.TextField(max_length=1000, blank=False, null=False, verbose_name='Descrição')
    tecnologias = models.ManyToManyField(Tecnologias, field_name='tecnologia', to='tecnologia', on_delete=models.DO_NOTHING)
    endereco = models.CharField(max_length=200, blank=True, null=True, verbose_name='Enderço do Site')
    codigo = models.CharField(max_length=200, blank=True, null=True, verbose_name='Endereço do Codigo')
    data_cadastro = models.DateField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    imagem = models.ImageField(verbose_name='Carregar Imagem')

    class Meta:
        db_table = 'projetos'

    def __str__(self):
        return self.nome_projeto , str(self.tecnologias)

    def get_data_cadastro(self):
        return self.data_cadastro.strftime("%m/%d/%Y, %H:%M:%S")