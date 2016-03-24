from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	
	# the URL need to begging with the word "post/" ...
	# and with digit or number afterwards
	# the sybol "$" means "The End"
	
	
	# I used comments below from a reference URL of
	# http://tutorial.djangogirls.org/en/extend_your_application/index.html
	
	# That means if you enter  http://127.0.0.1:8000/post/5/  into your browser,
	# Django will understand that you are looking for a view called  post_detail
	# and transfer the information that  pk  equals  5  to that view.

    # pk  is shortcut for  primary key . This name is often used in Django projects.

	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
