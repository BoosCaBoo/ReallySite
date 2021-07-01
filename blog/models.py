from django.db import models


class Article(models.Model):
	title = models.CharField(
		default="",
		max_length=30,
	)
	text = models.CharField(
		default="",
		max_length=100
	)
	author = models.CharField(
		default="",
		max_length=30
	)
	created_at = models.DateTimeField(
		auto_now_add=True
	)
	updated_at = models.DateTimeField(
		auto_now=True
	)
