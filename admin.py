from django.contrib import admin
from .models import (
Customer ,
Carts,
 Product,
) 

@admin.register ( Customer )
class CustomerModelAdmin( admin.ModelAdmin  ):
    list_display = [ 'id' , 'user' , 'name' ,  'locality', 'city','zipcode']
                    


@admin.register ( Carts) 
class cartsModelAdmin ( admin.ModelAdmin ): 
    list_display= ['id' ,'user' , 'product','quantity'] 
# Register your models here.
@admin.register ( Product ) 
class ProductModelAdmin ( admin.ModelAdmin ): 
    list_display= [ 'id' , 'title'  ,'selling_price', 'discounted_price','description' , 'brand','category' ]