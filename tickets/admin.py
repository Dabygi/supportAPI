from django.contrib import admin
from tickets.models import Ticket, TicketCategory, Comment, Subcategory


admin.site.register(TicketCategory)
admin.site.register(Subcategory)
admin.site.register(Ticket)
admin.site.register(Comment)