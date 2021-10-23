from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, name, surename, password=None):
        """
        Creates and saves a User with the given data
        """

        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            name=name,
            surename=surename
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name=None, surename=None, password=None):
        """
        Creates and saves a superUser with the given data
        """
        user = self.model(
            username=username,
            name=name,
            surename=surename
        )
        user.is_admin = True
        is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class AuthUser(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=255)
    surename = models.CharField(max_length=255)

    objects = UserManager()
    
    class Meta:
        db_table = 'auth_user'

    def is_staff(self):
        return self.is_admin

    def is_super_admin(self):
        return self.is_admin

    USERNAME_FIELD = 'username'
