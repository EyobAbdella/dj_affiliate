from django.contrib import admin
from dj_affiliate.models import Affiliate
from django import forms

class AffiliateForm(forms.ModelForm):
    class Meta:
        model = Affiliate
        exclude = ['reward_amount']

class AffiliateAdmin(admin.ModelAdmin):
    form = AffiliateForm 
    
    def get_readonly_fields(self, request, obj=None):
        if obj: 
            return ['reward_amount']
        return [] 

    list_display = ['affiliate_id', 'user', 'reward_amount', 'created_at']
    search_fields = ['affiliate_id', 'user__username']

admin.site.register(Affiliate, AffiliateAdmin)