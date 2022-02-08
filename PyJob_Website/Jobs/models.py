from django.db import models


# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    contract = models.CharField(max_length=10, null=True)
    location = models.CharField(max_length=50, null=True)
    remote = models.CharField(max_length=50, null=True)
    education_level = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=5000)
    salary = models.IntegerField(null=True)
    date_published = models.DateTimeField()
    url = models.CharField(max_length=100)

    def __str__(self):
        return f"""
            title: {self.title}
            company: {self.company}
            contract: {self.contract}
            location: {self.location}
            remote: {self.remote}
            education_level: {self.education_level}
            description: {self.description}
            salary: {self.salary}
            date_published: {self.date_published}
            url: {self.description}
        """
