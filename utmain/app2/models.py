from django.db import models


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    readonly_fields=('id',)
    level = models.IntegerField()
    name = models.CharField(max_length=200)
    parent = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"id:{self.id}; level:{self.level}; name: {self.name}; parent:{self.parent}"


class Choice(models.Model):
    
    id = models.AutoField(primary_key=True)
    readonly_fields=('id',)
    question = models.ForeignKey(Option, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)