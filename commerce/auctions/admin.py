from django.contrib import admin
from .models import User, Listing, Bids,Comments
# Register your models here.



class ListAdmin(admin.ModelAdmin):
    list_display=('creator','title','description','starting_bid','image_URL','category','closed')
    
    
class BidsAdmin(admin.ModelAdmin):   
    list_display=('listing','user','value_offer')

class CommentsAdmin(admin.ModelAdmin):   
    list_display=('author','content','listing')


#class PassengerAdmin(admin.ModelAdmin):
 #   filter_horizontal=("flights",)

admin.site.register(User)
admin.site.register(Listing,ListAdmin)
admin.site.register(Bids,BidsAdmin)
admin.site.register(Comments,CommentsAdmin)
#admin.site.register(Flight,FlightAdmin)
#admin.site.register(Passenger,PassengerAdmin)