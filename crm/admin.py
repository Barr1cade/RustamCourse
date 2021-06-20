from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0


class OrderAdm(admin.ModelAdmin):
    '''отображение полей'''
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    '''поля-ссылки'''
    list_display_links = ('id', 'order_name')
    '''поля-поиск'''
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    '''поля-фильтры'''
    list_filter = ('order_status',)
    '''редактируемые поля'''
    list_editable = ('order_status', 'order_phone')
    '''list-pagination'''
    list_per_page = 10
    list_max_show_all = 100
    '''card editing'''
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    '''not editable fields'''
    readonly_fields = ('id', 'order_dt')
    # class comment field
    inlines = [Comment, ]


# Register your models here.
admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
