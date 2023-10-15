from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

from adminpanel.models import FilterWords, Notifications, Articles, Sites, Clients


# Define views for the Clients model
class ClientListView(ListView):
    # Display a list of Clients
    model = Clients
    fields = ['id', "username", 'tts_enabled']
    template_name = 'client/list.html'
    context_object_name = 'clients'


class ClientDetailView(DetailView):
    # Display detailed information about a Client
    model = Clients
    fields = ["username", 'tts_enabled']
    template_name = 'client/detail.html'
    context_object_name = 'client'


class ClientCreateView(CreateView):
    # Create a new Client
    model = Clients
    fields = ["username", 'tts_enabled']
    template_name = 'client/add.html'
    context_object_name = 'clients'
    success_url = reverse_lazy('client_list')


class ClientDeleteView(DeleteView):
    # Delete a Client
    model = Clients
    fields = ["username", 'tts_enabled']
    template_name = 'client/delete.html'
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    # Update an existing Client
    model = Clients
    template_name = 'client/add.html'
    fields = ["username", 'tts_enabled']

    def get_success_url(self):
        return reverse('client_detail', kwargs={'pk': self.object.pk})


# Define views for the FilterWords model
class FilterWordsListView(ListView):
    # Display a list of FilterWords
    model = FilterWords
    fields = ['id', "clientid", "word", "wordalias", 'subwordalias', 'stopword']
    template_name = 'filter/list.html'
    context_object_name = 'filters'


class FilterWordsDetailView(DetailView):
    # Display detailed information about a FilterWord
    model = FilterWords
    fields = ["clientid", "word", "wordalias", 'subwordalias', 'stopword']
    template_name = 'filter/detail.html'
    context_object_name = 'filter'


class FilterWordsCreateView(CreateView):
    # Create a new FilterWord
    model = FilterWords
    fields = ["clientid", "word", "wordalias", 'subwordalias', 'stopword']
    template_name = 'filter/add.html'
    context_object_name = 'filter'
    success_url = reverse_lazy('filter_list')


class FilterWordsDeleteView(DeleteView):
    # Delete a FilterWord
    model = FilterWords
    fields = ["clientid", "word", "wordalias", 'subwordalias', 'stopword']
    template_name = 'filter/delete.html'
    success_url = reverse_lazy('filter_list')
    context_object_name = 'filter'


class FilterWordsUpdateView(UpdateView):
    # Update an existing FilterWord
    model = FilterWords
    template_name = 'filter/add.html'
    fields = ["clientid", "word", "wordalias", 'subwordalias', 'stopword']

    def get_success_url(self):
        return reverse('filter_detail', kwargs={'pk': self.object.pk})


# Define views for the Notifications model
class NotificationsListView(ListView):
    # Display a list of Notifications
    model = Notifications
    fields = ['id', "clientid", "sms", "telegram", 'whatsapp', 'email', 'comment']
    template_name = 'notifications/list.html'
    context_object_name = 'notifications'


class NotificationsDetailView(DetailView):
    # Display detailed information about a Notification
    model = Notifications
    fields = ['id', "clientid", "sms", "telegram", 'whatsapp', 'email', 'comment']
    template_name = 'notifications/detail.html'
    context_object_name = 'notification'


class NotificationsCreateView(CreateView):
    # Create a new Notification
    model = Notifications
    fields = ["clientid", "sms", "telegram", 'whatsapp', 'email', 'comment']
    template_name = 'notifications/add.html'
    context_object_name = 'notification'
    success_url = reverse_lazy('notification_list')


class NotificationsDeleteView(DeleteView):
    # Delete a Notification
    model = Notifications
    fields = ['id', "clientid", "sms", "telegram", 'whatsapp', 'email', 'comment']
    template_name = 'notifications/delete.html'
    success_url = reverse_lazy('notification_list')


class NotificationsUpdateView(UpdateView):
    # Update an existing Notification
    model = Notifications
    template_name = 'notifications/add.html'
    fields = ["clientid", "sms", "telegram", 'whatsapp', 'email', 'comment']

    def get_success_url(self):
        return reverse('notification_detail', kwargs={'pk': self.object.pk})


# Define views for the Articles model
class ArticlesListView(ListView):
    # Display a list of Articles
    model = Articles
    fields = ['id', "site", "clientid", "insert_date", 'article_date', 'autor', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_artikle', 'screenshot_url', 'status', 'found_word']
    template_name = 'articles/list.html'
    context_object_name = 'article'


class ArticlesDetailView(DetailView):
    # Display detailed information about an Article
    model = Articles
    fields = ['id', "site", "clientid", "insert_date", 'article_date', 'autor', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_artikle', 'screenshot_url', 'status', 'found_word']
    template_name = 'articles/detail.html'
    context_object_name = 'article'


class ArticlesCreateView(CreateView):
    # Create a new Article
    model = Articles
    fields = ["site", "clientid", "insert_date", 'article_date', 'autor', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_artikle', 'screenshot_url', 'status', 'found_word']
    template_name = 'articles/add.html'
    context_object_name = 'article'
    success_url = reverse_lazy('article_list')


class ArticlesDeleteView(DeleteView):
    # Delete an Article
    model = Articles
    fields = ['id', "site", "clientid", "insert_date", 'article_date', 'autor', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_artikle', 'screenshot_url', 'status', 'found_word']
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('article_list')


class ArticlesUpdateView(UpdateView):
    # Update an existing Article
    model = Articles
    template_name = 'articles/add.html'
    fields = ["site", "clientid", "insert_date", 'article_date', 'autor', 'url', 'article_name', 'article_text', 'visitors_count', 'is_top_artikle', 'screenshot_url', 'status', 'found_word']

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.pk})


# Define views for the Sites model
class SitesListView(ListView):
    # Display a list of Sites
    model = Sites
    fields = ['id', "sitename", "internal_id"]
    template_name = 'sites/list.html'
    context_object_name = 'sites'


class SitesDetailView(DetailView):
    # Display detailed information about a Site
    model = Sites
    fields = ['id', "sitename", "internal_id"]
    template_name = 'sites/detail.html'
    context_object_name = 'site'


class SitesCreateView(CreateView):
    # Create a new Site
    model = Sites
    fields = ["sitename", "internal_id"]
    template_name = 'sites/add.html'
    context_object_name = 'site'
    success_url = reverse_lazy('site_list')


class SitesDeleteView(DeleteView):
    # Delete a Site
    model = Sites
    fields = ['id', "sitename", "internal_id"]
    template_name = 'sites/delete.html'
    success_url = reverse_lazy('site_list')


class SitesUpdateView(UpdateView):
    # Update an existing Site
    model = Sites
    template_name = 'sites/add.html'
    fields = ["sitename", "internal_id"]

    def get_success_url(self):
        return reverse('site_detail', kwargs={'pk': self.object.pk})

