from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject
from dj_affiliate.models import Affiliate

def get_affiliate(request, new_affiliate_id, prev_affiliate_id):
    if not hasattr(request, '_cached_affiliate'):
        affiliate = Affiliate.objects.filter(affiliate_id=new_affiliate_id).first()
        if affiliate is None:
            if prev_affiliate_id:
                affiliate = Affiliate.objects.filter(affiliate_id=prev_affiliate_id).first()
        request._cached_affiliate = affiliate
    return request._cached_affiliate


class AffiliateMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = getattr(request, 'session', None)
        prev_affiliate_id = session.get("_affiliate_id", None)
        AFFILIATE_PARAM = "affiliate_id"
        new_affiliate_id = request.GET.get(AFFILIATE_PARAM, None)
        if new_affiliate_id:
            session['_affiliate_id'] = new_affiliate_id
        request.affiliate = SimpleLazyObject(lambda: get_affiliate(request, new_affiliate_id, prev_affiliate_id))
        response = self.get_response(request)
        return response
