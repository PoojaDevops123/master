from django.urls import path, include
from summary import pages, logged_pages

urlpatterns = [

    path('login', pages.login, name='login'),
    path('logout', pages.log_out, name='log_out'),
    path('summary_dash', logged_pages.dashboard, name='dashboard'),
    path('upload_URL', logged_pages.fromURL, name='frm_URL'),
    path('upload_PDF', logged_pages.fromPDF, name='frm_PDF'),
    path('upload_DOCX', logged_pages.fromDOCX, name='frm_DOCX'),
    path('upload_TXT', logged_pages.fromTXT, name='frm_TXT'),
    path('post_twitter', logged_pages.sendRequest, name='SendTweet')

]
