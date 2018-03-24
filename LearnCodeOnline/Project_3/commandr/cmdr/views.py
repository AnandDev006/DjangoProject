from django.views.generic import ListView

from .models import Cmdr

# Create your views here.

class ButtonView(ListView):
	model = Cmdr
	template_name = 'buttons.html'