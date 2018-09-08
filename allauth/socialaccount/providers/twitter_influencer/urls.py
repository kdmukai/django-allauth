from allauth.socialaccount.providers.oauth.urls import default_urlpatterns

from .provider import TwitterInfluencerProvider


urlpatterns = default_urlpatterns(TwitterInfluencerProvider)
