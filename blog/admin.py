from django.contrib import admin
from blog.models import Post, Category, Comment
from projects.models import Project
from about_me.models import About
from contact.models import Message



class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
   pass

    
class AboutAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
    
class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Message, MessageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(About, AboutAdmin)
