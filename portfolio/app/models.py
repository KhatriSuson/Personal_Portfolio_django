from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    image = models.ImageField(upload_to="static/banners")

    def __str__(self):
        return self.title


class Service(models.Model):
    stitle = models.CharField(max_length=400)
    sdescription = models.TextField()
    simage = models.ImageField(upload_to="static/services")

    def __str__(self):
        return self.stitle


class Feature(models.Model):
    ftitle = models.CharField(max_length=400)
    fdescription = models.TextField()
    fimage = models.ImageField(upload_to="static/features")

    def __str__(self):
        return self.ftitle


class About(models.Model):
    title = models.CharField(max_length=400)
    dis = models.TextField()
    # sub_dis = models.CharField(max_length=1000)
    img = models.ImageField(upload_to="static/abouts")

    def __str__(self):
        return self.title


# class Contact(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     subject = models.TextField()
#     message = models.TextField()


#     def __str__(self):
#         return self.name


class MyContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=150)
    logo = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name
