from django . urls import path
from onlineshopping import views
app_name="onlineshopping"
urlpatterns=[
    path('',views.index,name='index'),
    path('user_home/<int:id>',views.user_home,name='user_home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('update/<int:id>',views.update,name='update'),
    path('logout',views.logout,name='logout'),
]