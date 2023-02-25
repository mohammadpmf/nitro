from django.contrib import admin

from .models import Post, Comment


##########################################################################
# # raveshe avval
# admin.site.register(Post)
##########################################################################


##########################################################################
# # ravesh e dovvom ke khafan tareh
# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post, PostAdmin)
##########################################################################


##########################################################################
# # edameye ravesh e dovvom ke khafan tareh
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'datetime_created', 'datetime_modified', 'status']

# admin.site.register(Post, PostAdmin)
##########################################################################


##########################################################################
# ravesh sevvom ke az hame khafan tareh
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'datetime_created', 'datetime_modified', 'status']
    list_display_links = ['title', 'author', 'datetime_created', 'datetime_modified', 'status']
    ordering = ['status', 'author']
##########################################################################
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author','author_email','text','likes',]
    list_display_links = ['post', 'author','author_email','text','likes',]
