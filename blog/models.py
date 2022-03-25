from django.db import models
from django.conf import settings

class Tag(models.Model):
  value = models.TextField(max_length=100)

  def __str__(self):
    return f'Tag value is {self.value}'

class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  published_at = models.DateTimeField(blank=True, null=True)
  title = models.TextField(max_length=100)
  slug = models.SlugField()
  summary = models.TextField(max_length=500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name="posts")

  def __str__(self):
    return f'Post author is {self.author}, it was create at {self.created_at} \
            and modified at {self.modified_at}. It was published at {self.published_at} \
            with the title {self.title}. The slug is {self.slug}, and the summary read: {self.summary}.\
            The content is {self.content} and the tags are {self.tags}.'