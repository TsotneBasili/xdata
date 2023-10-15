from django.db import models


# models to correspond existing tables in database.

class Sites(models.Model):
    id = models.IntegerField(primary_key=True)
    sitename = models.CharField(unique=True, max_length=128)
    internal_id = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'sites'

    def __str__(self):
        return str(self.id)


class Clients(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    tts_enabled = models.BooleanField()

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'clients'


class Articles(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey('Sites', on_delete=models.CASCADE)
    clientid = models.ForeignKey('Clients', db_column='clientid', on_delete=models.CASCADE)
    insert_date = models.DateTimeField()
    article_date = models.DateTimeField()
    autor = models.CharField(max_length=128, blank=True, null=True)
    url = models.CharField(max_length=1022)
    article_name = models.TextField()
    article_text = models.TextField()
    visitors_count = models.IntegerField()
    is_top_artikle = models.IntegerField()
    screenshot_url = models.CharField(max_length=90, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    found_word = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'articles'
        unique_together = (('id', 'site'), ('url', 'clientid'),)


class FilterWords(models.Model):
    id = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey('Clients', db_column='clientid', on_delete=models.CASCADE)
    word = models.CharField(max_length=255, blank=True, null=True)
    wordalias = models.CharField(db_column='wordAlias', max_length=1022, blank=True, null=True)  # Field name made lowercase.
    subwordalias = models.CharField(max_length=255, blank=True, null=True)
    stopword = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'filterwords'


class Notifications(models.Model):
    id = models.IntegerField(primary_key=True)
    clientid = models.ForeignKey('Clients', db_column='clientid', on_delete=models.CASCADE)
    sms = models.CharField(max_length=255, blank=True, null=True)
    telegram = models.CharField(max_length=255, blank=True, null=True)
    whatsapp = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notifications'



