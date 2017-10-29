"""models defind for 'homepage' app"""

from django.db import models
from django.contrib.auth.models import User



class TopResultType(models.Model):
	"""docstring for topResultType"""
	resultId = models.IntegerField(primary_key=True, max_length=5)
	resultTopic = models.CharField(blank=False, max_length=250)
	def __unicode__(self):
		return self.resultId
	# def __init__(self, arg):
	#   super(topResultType, self).__init__()
	#   self.arg = arg

class TopResultMapping(models.Model):
	"""result Table"""
	id = models.IntegerField(primary_key=True, max_length=10)
	resultType = models.IntegerField(blank=False,  max_length=5)
	# resultType = models.ForeignKey(TopResultType, to_field=resultId, max_length=5)
	resultName = models.CharField(blank=True, max_length=250)
	def __unicode__(self):
		return self.resultType        
