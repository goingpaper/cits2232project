from django.db import models

# Create your models here.
class Bar(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	phone = models.CharField(max_length=100,blank = True,null = True)
	email = models.CharField(max_length=100,blank = True,null = True)
	website = models.CharField(max_length=100,blank = True,null = True)
	yearEstablished = models.IntegerField(blank=True,null=True)
	description = models.CharField(max_length=300,blank = True,null = True)
	
	def __unicode__(self):
		return self.name
	
class User(models.Model):
	username = models.CharField(max_length=100) # username compulsory
	password = models.CharField(max_length=100) # password compulsory
	fname = models.CharField(max_length=100) # fname compulsory
	lname = models.CharField(max_length=100) # lname compulsory
	email = models.CharField(max_length=100) # email compulsory
	dateRegistered = models.DateField()
	userType = models.CharField(max_length=100) #compulsory
	
	def __unicode__(self):
		return self.username
	
class Drink(models.Model):
	brewery = models.CharField(max_length=100)
	dType = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

class Brewery(models.Model):
	name = models.CharField(max_length=100) #not sure
	
	def __unicode__(self):
		return self.name
	
class ReviewBar(models.Model):
	user = models.ForeignKey(User) # ? constraints
	bar = models.ForeignKey(Bar) # ? constraints
	rating = models.IntegerField() #?
	date = models.DateField()
	comment = models.CharField(max_length=300)
#unable to make a multifield primary key in django
	def __unicode__(self):
		return self.username

	class Meta:
		unique_together = ('username', 'barName', 'date')

class LikesBeer(models.Model):
	username = models.CharField(max_length=100)
	drink = models.ForeignKey(Drink)

	class Meta:
		unique_together = ('username', 'drinkName')
    
	def __unicode__(self):
		return self.username

class Serves(models.Model):
	bar = models.ForeignKey(Bar)
	drink = models.ForeignKey(Drink)
	onTap = models.BooleanField()
	price = models.DecimalField(max_digits=5,decimal_places=2)

	def __unicode__(self):
		return '%s serves %s' % (self.barName , self.drinkName)

	class Meta:
		unique_together = ('barName', 'drinkName')

	
class Comment(models.Model):
	user1 = models.ForeignKey(User,related_name = 'source')
	user2 = models.ForeignKey(User,related_name = 'target')
	date = models.DateField()
	comment = models.CharField(max_length=300)
    
	def __unicode__(self):
		return '%s comments on %s' % (self.user1, self.user2)

	class Meta:
		unique_together = ('user1', 'user2','date')
#max 5 digit number and 2 decimal places

	

	
	
