import pocket

from pocket_auth.models import AccessToken, PocketItem

from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse



def index(request):
    access_tokens = AccessToken.objects.all()

    if len(access_tokens) > 0:
        pocket_access_token = access_tokens[0].access_token
    else:
        pocket_access_token = None

    context = {
                'pocket_access_token': pocket_access_token,
                'total_items_downloaded': PocketItem.objects.all().count(),
                'total_videos_converted': PocketItem.objects.exclude(downloaded_file='').count(),
                'total_videos_not_converted': PocketItem.objects.filter(downloaded_file='').count()
            }
    return render(request, 'wicker_park/index.html', context)
