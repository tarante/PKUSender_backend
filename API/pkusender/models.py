# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	objects 	= models.Manager()
	user_id 	= models.CharField(max_length=100, default='', primary_key=True)
	user_name 	= models.CharField(max_length=100, default='')
	address 	= models.CharField(max_length=1000, default='')
	credit 		= models.IntegerField(default=100)
	coin_num 	= models.IntegerField(default=20)
	gender 		= models.CharField(max_length=100, default='') # gender: 0-unkonw  1-male  2-female
	call_order_list = models.CharField(max_length=1000, default='')
	take_order_list = models.CharField(max_length=1000, default='')





class Order(models.Model):
	objects 		= models.Manager()
	order_id 		= models.CharField(max_length=100, default='', primary_key=True)
	caller_id		= models.CharField(max_length=100, default='')
	helper_id 		= models.CharField(max_length=100, default='')
	src_address 	= models.CharField(max_length=100, default='')
	dest_address 	= models.CharField(max_length=100, default='')
	coin_cost 		= models.IntegerField(default=0)
	descrption 		= models.CharField(max_length=1000, default='')
	secret_info 	= models.CharField(max_length=1000, default='')
	order_status 	= models.IntegerField(default=0) # 0-waiting 1-running 2-complete
	comment 		= models.CharField(max_length=1000, default='')
	star_level 		= models.CharField(max_length=10, default='') # 1 2 3 4 5
	# complete_time 	= models.TimeField()