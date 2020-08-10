from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Creation des modèles.

class Profile(models.Model):
    """ Modèle qui élargit le profil de l'utilisateur """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(verbose_name="date de naissance", null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name="adresse")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        return 'Profile de: {}'.format(self.user.username)

# Envoi d'un signal pour la création du profil élargit de User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Envoi d'un signal pour l'enregistrement du profil élargit de User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Offer(models.Model):
    title = models.CharField(max_length=255, verbose_name="titre")
    description = models.TextField()
    price = models.DecimalField(verbose_name="prix", max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User, through="Souscription", verbose_name="Utilisateurs souscrits")
    
    def __str__(self):
        return self.title

class Souscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    souscriptionDate = models.DateTimeField(default=timezone.now, verbose_name="Date de souscription")
    
    def __str__(self):
        return "{0} a souscrit à {1} le {2} ".format(self.user, self.offer, self.souscriptionDate)

class Conference(models.Model):
    title = models.CharField(max_length=255, verbose_name="titre")
    description = models.TextField()
    secret = models.CharField(max_length=255, verbose_name="Code secret")
    beginDate = models.DateTimeField(default=timezone.now, verbose_name="Date de début")
    endDate = models.DateTimeField(default=timezone.now, verbose_name="Date de fin")
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Initiateur")
    participants = models.ManyToManyField(User, related_name="+")

