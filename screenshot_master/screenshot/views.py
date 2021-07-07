from django.shortcuts import render
# from desktopmagic.screengrab_win32 import getScreenAsImage
import getpass
import pyscreenshot


# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)


def screenshot(request):
    user = getpass.getuser()
    
    # entireScreen = getScreenAsImage()
    # entireScreen.save(user + r'_screen.png', format='png')
    
    image = pyscreenshot.grab()    
    image.save(user + r"_test.png")
    
    context = {}
    
    return render(request, 'index.html', context)
    