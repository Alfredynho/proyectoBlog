from django.contrib import admin
from .models import Post

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
	list_display = ['autor', 'title', 'creted_date', 'publish_date']

	class Meta:
		models = Post