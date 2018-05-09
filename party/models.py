from django.db import models

# Create your models here.


class Feedback(models.Model):
    name=models.CharField(max_length=20)
    feedback=models.TextField(max_length=200)


    def __str__(self):
        return str(self.name) + " 's feedback"


class Gotcha(models.Model):
    sl_no=models.AutoField(primary_key=True)
    secret=models.TextField(max_length=500)

    def __str__(self):
        return "secret number - "+str(self.sl_no)


class Oqp(models.Model):
    recipient=models.CharField(max_length=20)
    question=models.TextField(max_length=500)

    def __str__(self):
        return "Question to " + str(self.recipient)


class WishingWell(models.Model):
    name=models.CharField(max_length=20)
    crush_desc=models.TextField(max_length=1500)

    def __str__(self):
        return str(self.name)+" 's crush description"


class Sorry(models.Model):
    name=models.CharField(max_length=20)
    sorry=models.TextField(max_length=1000)
    to=models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)+ " 's sorry to " + str(self.to)


