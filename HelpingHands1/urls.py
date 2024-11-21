"""
URL configuration for HelpingHands1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from helpinghands.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('all_logins', all_logins, name='all_logins'),
                  path('donor_login', donor_login, name='donor_login'),
                  path('volunteer_login', volunteer_login, name='volunteer_login'),
                  path('admin_login', admin_login, name='admin_login'),
                  path('organization_login', organization_login, name='organization_login'),
                  path('donor_reg', donor_reg, name='donor_reg'),
                  path('donor_home', donor_home, name='donor_home'),
                  path('volunteer_home', volunteer_home, name='volunteer_home'),
                  path('donate_now', donate_now, name='donate_now'),
                  path('donation_history', donation_history, name='donation_history'),
                  path('donor_base', donor_base, name='donor_base'),
                  path('admin_home', admin_home, name='admin_home'),
                  path('pending_donation', pending_donation, name='pending_donation'),
                  path('view_donationdetails/<int:pid>', view_donationdetails, name='view_donationdetails'),
                  path('accepted_donationdetail/<int:pid>', accepted_donationdetail, name='accepted_donationdetail'),
                  path('accepted_donation', accepted_donation, name='accepted_donation'),
                  path('add_area', add_area, name='add_area'),
                  path('manage_area', manage_area, name='manage_area'),
                  path('edit_area/<int:pid>', edit_area, name='edit_area'),
                  path('delete_area/<int:pid>', delete_area, name='delete_area'),
                  path('manage_donor', manage_donor, name='manage_donor'),
                  path('view_donordetail/<int:pid>', view_donordetail, name='view_donordetail'),
                  path('delete_donor/<int:pid>', delete_donor, name='delete_donor'),
                  path('volunteer_reg', volunteer_reg, name='volunteer_reg'),
                  path('new_volunteer', new_volunteer, name='new_volunteer'),
                  path('accepted_volunteer', accepted_volunteer, name='accepted_volunteer'),
                  path('rejected_volunteer', rejected_volunteer, name='rejected_volunteer'),
                  path('all_volunteer', all_volunteer, name='all_volunteer'),
                  path('delete_volunteer/<int:pid>', delete_volunteer, name='delete_volunteer'),
                  path('view_volunteerdetail/<int:pid>', view_volunteerdetail, name='view_volunteerdetail'),
                  path('collection_request', collection_request, name='collection_request'),
                  path('donation_collectiondetail/<int:pid>', donation_collectiondetail, name='donation_collectiondetail'),
                  path('donationreceived_volunteer', donationreceived_volunteer, name='donationreceived_volunteer'),
                  path('donationreceived_detail/<int:pid>', donationreceived_detail, name='donationreceived_detail'),
                  path('donationnotreceived_volunteer', donationnotreceived_volunteer, name='donationnotreceived_volunteer'),
                  path('donationDelivered_volunteer', donationDelivered_volunteer, name='donationDelivered_volunteer'),
                  path('profile_volunteer', profile_volunteer, name='profile_volunteer'),
                  path('successforpayment', successforpayment, name='successforpayment'),
                  path('indexforpayment', indexforpayment, name='indexforpayment'),
                  path('baseforpayment', baseforpayment, name='baseforpayment'),
                  path('logout', Logout, name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
