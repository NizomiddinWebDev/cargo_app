from django.db import models
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Client(models.Model):
    tg_id = models.CharField(max_length=200, primary_key=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    prop_address = models.CharField(max_length=300, null=True, blank=True)
    passport = models.CharField(max_length=10, null=True, blank=True)
    mark = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ['update_date']


class Product(models.Model):
    name = models.CharField(max_length=200)
    product_count = models.IntegerField(null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=CASCADE, related_name='products', null=True, blank=True)

    def __str__(self):
        return self.client.tg_id

    class Meta:
        ordering = ['created_date']


class Mark(models.Model):
    mark_id = models.AutoField(primary_key=True)
    mark = models.CharField(max_length=150, null=True, blank=True)
    client = models.OneToOneField(Client, on_delete=CASCADE, related_name='marks', null=True, blank=True)

    def __str__(self):
        return self.client.tg_id


@receiver(post_save, sender=Product)
def save_user_profile(sender, instance, **kwargs):
    Client.objects.filter(tg_id=instance).update(update_date=timezone.now())


@receiver(post_save, sender=Mark)
def save_user_profile(sender, instance, **kwargs):
    count = Mark.objects.all().count()
    mark = 124 + count
    Client.objects.filter(tg_id=instance).update(mark=f'A-25/{mark}')
    Mark.objects.filter(client__tg_id=instance).update(mark=f'A-25/{mark}')
