from django.db import models
from django.db.models import *

from django.db import models as models

# Create your models here.
class imagen(models.Model):

	created = DateTimeField(auto_now_add=True, editable=False)
	last_updated = DateTimeField(auto_now=True, editable=False)
	foto = ImageField(upload_to='./images/', default = 'images/recursos/None/no-img.jpg')
	resultado = TextField()

	class Meta:
		ordering = ('created',)

	def __unicode__(self):
		return u'%s' % self.pk

	def __str__(self):
		return '{}'.format(self.pk)


