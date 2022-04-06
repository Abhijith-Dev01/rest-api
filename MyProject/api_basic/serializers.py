from rest_framework import serializers
from .models import Article,Users

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Article
		# fields 	= ['id','title','author','email']
		fields	= '__all__'

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model 	= Users
		fields 	= '__all__'