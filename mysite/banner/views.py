from .models import Banner
from django.views.generic.detail import DetailView

# Create your views here.
class BannerView(DetailView):
    model = Banner
    template_name = 'banner/base.html'
    
    
    