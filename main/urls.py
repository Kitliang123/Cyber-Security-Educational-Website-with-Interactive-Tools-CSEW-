from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("category/", views.category, name="category"),
    path("about/", views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.registerPage, name="register"),
    # path('loginn/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('phishing/', views.phishing, name="phishing"),
    path('ddos/', views.ddos, name="ddos"),
    path('mitm/', views.mitm, name="mitm"),
    path('bruteforce/', views.bruteforce, name="brute-force"),
    path('packetsniffing/', views.packetsniffing, name="packetsniffing"),
    path('zphisher/', views.zphisher, name="zphisher"),
    path('socialphish/', views.socialphish, name="socialphish"),
    path('LOIC/', views.LOIC, name="LOIC"),
    path('slowloris/', views.slowloris, name="slowloris"),
    path('ettercap/', views.ettercap, name="ettercap"),
    path('xerosploit/', views.xerosploit, name="xerosploit"),
    path('john/', views.john, name="john"),
    path('aircrack/', views.aircrack, name="aircrack"),
    path('wireshark/', views.wireshark, name="wireshark"),
    path('tcpdump/', views.tcpdump, name="tcpdump"),
]