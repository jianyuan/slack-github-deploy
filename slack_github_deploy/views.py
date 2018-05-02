from django.shortcuts import redirect, render


def temp_root(request):
    return render(request, 'temp_root.html')


def install_slack(request):
    return redirect('social:begin', backend='slack')
