from django.urls import path

from adminpanel.views import ClientListView, ClientDeleteView, ClientUpdateView, ClientDetailView, ClientCreateView, \
    FilterWordsListView, FilterWordsCreateView, FilterWordsDeleteView, FilterWordsUpdateView, FilterWordsDetailView, \
    NotificationsListView, NotificationsCreateView, NotificationsDeleteView, NotificationsUpdateView, \
    NotificationsDetailView, ArticlesDetailView, ArticlesListView, ArticlesCreateView, ArticlesDeleteView, \
    ArticlesUpdateView, SitesListView, SitesDetailView, SitesUpdateView, SitesDeleteView, SitesCreateView

urlpatterns = [
    # URLs for Client-related views
    path('client/', ClientListView.as_view(), name="client_list"),
    path('client/add/', ClientCreateView.as_view(), name="add_song"),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name="delete_client"),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name="update_client"),
    path('client/<int:pk>/', ClientDetailView.as_view(), name="client_detail"),

    # URLs for FilterWords-related views
    path('filter/', FilterWordsListView.as_view(), name="filter_list"),
    path('filter/add/', FilterWordsCreateView.as_view(), name="add_filter"),
    path('filter/delete/<int:pk>/', FilterWordsDeleteView.as_view(), name="delete_filter"),
    path('filter/update/<int:pk>/', FilterWordsUpdateView.as_view(), name="update_filter"),
    path('filter/<int:pk>/', FilterWordsDetailView.as_view(), name="filter_detail"),

    # URLs for Notifications-related views
    path('notifications/', NotificationsListView.as_view(), name="notification_list"),
    path('notifications/add/', NotificationsCreateView.as_view(), name="add_notification"),
    path('notifications/delete/<int:pk>/', NotificationsDeleteView.as_view(), name="delete_notification"),
    path('notifications/update/<int:pk>/', NotificationsUpdateView.as_view(), name="update_notification"),
    path('notifications/<int:pk>/', NotificationsDetailView.as_view(), name="notification_detail"),

    # URLs for Articles-related views
    path('articles/', ArticlesListView.as_view(), name="article_list"),
    path('articles/add/', ArticlesCreateView.as_view(), name="add_article"),
    path('articles/delete/<int:pk>/', ArticlesDeleteView.as_view(), name="delete_article"),
    path('articles/update/<int:pk>/', ArticlesUpdateView.as_view(), name="update_article"),
    path('articles/<int:pk>/', ArticlesDetailView.as_view(), name="article_detail"),

    # URLs for Sites-related views
    path('sites/', SitesListView.as_view(), name="site_list"),
    path('sites/add/', SitesCreateView.as_view(), name="add_site"),
    path('sites/delete/<int:pk>/', SitesDeleteView.as_view(), name="delete_site"),
    path('sites/update/<int:pk>/', SitesUpdateView.as_view(), name="site_article"),
    path('sites/<int:pk>/', SitesDetailView.as_view(), name="site_detail"),
]
