from django import forms

from adminpanel.models import FilterWords, Articles, Sites, Clients


# forms to create and update objects in database


class ClientForm(forms.ModelForm):
    model = Clients


class FilterWordsForm(forms.ModelForm):
    model = FilterWords


class NotificationsForm(forms.ModelForm):
    model = FilterWords


class ArticlesForm(forms.ModelForm):
    model = Articles


class SiteFrom(forms.ModelForm):
    model = Sites
