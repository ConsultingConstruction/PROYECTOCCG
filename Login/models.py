from django.db import models

# Create your models here.
class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Correo', unique=True, max_length=50, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=15, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='fechaCreacion', blank=True, null=True)  # Field name made lowercase.
    fechaact = models.DateTimeField(db_column='fechaAct')  # Field name made lowercase.
