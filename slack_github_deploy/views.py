from django.shortcuts import redirect


def install_slack(request):
    return redirect('social:begin', backend='slack-app')
