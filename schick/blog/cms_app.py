from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class Blog(CMSApp):
    name = _("Blog") # give your app a name, this is required
    urls = ["schick.blog.urls"] # link your app to url configuration(s)

apphook_pool.register(Blog) # register your app