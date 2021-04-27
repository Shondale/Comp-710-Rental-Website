from django.db import models

class Location(models.Model):
	store_id = models.CharField(max_length=32, primary_key=True)
	address = models.CharField(max_length=300)


class Item(models.Model):
	item_id = models.CharField(max_length=128, primary_key=True)
	item_name = models.CharField(max_length=200)
	item_description = models.CharField(max_length=500)
	item_dimensions = models.CharField(max_length=65)
	item_weight = models.IntegerField()
	CATEGORIES = (
		('A', 'Appliances'),
		('E', 'Electronics'),
		('F','Furniture'),
		('T', 'Tools'),
	)
	item_category = models.CharField(max_length=11, choices=CATEGORIES)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
		#lifetime
	#times_rented
	#rent_to_own_time
	#

class User(models.Model):
	user_id = models.CharField(max_length=128, primary_key=True)
	user_name = models.CharField(max_length=200)
	user_password = models.CharField(max_length=32, default='password')
	current_item = models.ForeignKey(Item, on_delete=models.CASCADE)
	#past_item = models.ForeignKey(Item, on_delete=models.CASCADE)
	financial = models.CharField(max_length=250)

class Data_analytics(models.Model):
	rent_id = models.CharField(max_length=128)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
