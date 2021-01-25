from django.contrib import admin

# Register your models here.
from ui import models
from ui.models import Sliders, About, Contact, Agent, FeaturesHome, BrandsItem, House, Service, Blog, HomeName, \
    Pictures, CtrlComment


class ModifiedSlider(admin.ModelAdmin):
    list_display = ('title1','title2','title3','picture',)# extra fields in the admin
    list_filter = ('title1',) #filters
    search_fields = ('title1',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically


class ModifiedAgent(admin.ModelAdmin):
    list_display = ('first_name','last_name','job','email','inDate',)# extra fields in the admin
    list_filter = ('first_name',) #filters
    search_fields = ('first_name',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically

class ModifiedBrandsItem(admin.ModelAdmin):
    list_display = ('brandsName',)# extra fields in the admin
    list_filter = ('brandsName',) #filters
    search_fields = ('brandsName',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically

class PicturesInline(admin.TabularInline):
    model = models.Pictures
    extra = 1

# class BooksInstanceInline(admin.StackedInline):
#     model = models.BookInstance
#     extra = 1
# farklı bir format

class ModifiedHouse(admin.ModelAdmin):
    list_display = ('name','price','square','agent')# extra fields in the admin
    list_filter = ('name','price','square',) #filters
    search_fields = ('square','name',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically
    inlines = [PicturesInline]


class ModifiedService(admin.ModelAdmin):
    list_display = ('title',)# extra fields in the admin
    list_filter = ('title',) #filters
    search_fields = ('title',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically

class ModifiedBlog(admin.ModelAdmin):
    list_display = ('name',)# extra fields in the admin
    list_filter = ('name',) #filters
    search_fields = ('name',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically

class ModifiedHomeName(admin.ModelAdmin):
    list_display = ('name',)# extra fields in the admin
    list_filter = ('name',) #filters
    search_fields = ('name',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically

class ModifiedPictures(admin.ModelAdmin):
    list_display = ('homeName','cover',)# extra fields in the admin
    list_filter = ('homeName','cover',) #filters
    search_fields = ('homeName',) #bu alanlar üzerinde search yapılacaktır
    #date_hierarchy = 'title1' #navigate quickly through a date hierarchy.
    ordering = ['id'] #order the list by 'appStatus' and then 'appDate'
    #prepopulated_fields = {'slugName': ('title2',)} # write slug of the given name automatically


admin.site.register(Sliders, ModifiedSlider)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Agent, ModifiedAgent)
admin.site.register(FeaturesHome)
admin.site.register(BrandsItem, ModifiedBrandsItem)
admin.site.register(House, ModifiedHouse)
admin.site.register(Service, ModifiedService)
admin.site.register(Blog, ModifiedBlog)
admin.site.register(HomeName, ModifiedHomeName)
admin.site.register(Pictures,ModifiedPictures)
admin.site.register(CtrlComment)


