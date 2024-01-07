from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        create and saves a User with the given email, date of birth and password
        """
        if not email:
            raise ValueError("Users must have a email address")
        
        user = self.model(
            email=self.normalize_email(email),
            name = name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, password=None):
        user = self.create_user(email, password=password,name=name)
        user.is_admin = True
        user.save(using=self.db)
        return user
    

# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email",max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        "Does user have a specific permission?"

        return True
    
    def has_module_perms(self, app_label):
        "Does user have permissions to view the app 'app_label'?"
        return True
    

