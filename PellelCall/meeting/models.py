from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Creation des modèles.

class Profile(models.Model):
    """ Ce modèle élargit le profil de l'utilisateur avec d'autres champs """
    # Fields
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Utilisateur")
    birthdate = models.DateField(verbose_name="date de naissance", null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name="adresse")
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    # Metadata
    class Meta:
        verbose_name = "profil"
        ordering = ['user']

    def __str__(self):
        """Retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
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
    """Ce modèle représente une offre à l'utilisateur"""
    title = models.CharField(max_length=255, verbose_name="titre")
    description = models.TextField()
    price = models.DecimalField(verbose_name="prix", max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User, through="Souscription", verbose_name="Utilisateurs souscrits", related_name="offers")
    
    #Metadonnées
    class Meta:
        verbose_name = "offre"
        
    def __str__(self):
        """Retourne une chaine de caractère qui répresente le titre de l'offre"""
        return self.title

class Souscription(models.Model):
    """Ce modèle représente la liaison entre une offre et un utilisateur"""
    user = models.ForeignKey(User, related_name='souscriptions', on_delete=models.SET_NULL, null=True, verbose_name="utilisateur")
    offer = models.ForeignKey(Offer, related_name='souscriptions',on_delete=models.SET_NULL, null=True, blank=True, verbose_name="offre")
    souscriptionDate = models.DateTimeField(default=timezone.now, verbose_name="Date de souscription")
    
    def __str__(self):
        """Identifie l'offre d'un utilisateur à une date"""
        return "{0} a souscrit à {1} le {2} ".format(self.user.username, self.offer, self.souscriptionDate)

class Conference(models.Model):
    """Ce modèle représente une conférence"""
    title = models.CharField(max_length=255, verbose_name="titre")
    description = models.TextField()
    secret = models.CharField(max_length=255, verbose_name="Code secret")
    beginDate = models.DateTimeField(default=timezone.now, verbose_name="Date de début")
    endDate = models.DateTimeField(default=timezone.now, verbose_name="Date de fin")
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Initiateur", related_name="+")
    participants = models.ManyToManyField(User, related_name='conferences')

    class Meta:
        verbose_name = "conférence"
        ordering = ['-beginDate']

    def __str__(self):
        """Retourne une chaine qui indique la conférence et l'horaire"""
        return "{0} de {1} à {2} ".format(self.title, self.beginDate, self.endDate)