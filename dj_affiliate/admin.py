from django.contrib import admin
from dj_affiliate.models import Affiliate


class AffiliateAdmin(admin.ModelAdmin):
    def get_exclude(self, request, obj=None):
        if request.method == 'POST':
            return ("reward_amount",)
        return None

admin.site.register(Affiliate, AffiliateAdmin)