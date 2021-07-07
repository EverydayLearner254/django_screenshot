from django.shortcuts import render
from desktopmagic.screengrab_win32 import getScreenAsImage
import getpass

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def screenshot(request):
    user = getpass.getuser()
    
    entireScreen = getScreenAsImage()
    entireScreen.save(user + r'_screen.png', format='png')
    context = {}
    
    return render(request, 'index.html', context)
    