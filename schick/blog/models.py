from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Blog(models.Model):
    """
    Represents blog objects, which in turn contain a number of blog posts. Examples
    include IRE News, Extra Extra and Uplink.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(help_text='Don\'t change unless you have absolute confidence in what you\'re doing.')
    about = models.TextField(blank=True)
    
    class Meta:
        ordering = ('title',)
        # Custom permission for use with django-guardian. Allows qualified users
        # to view the blog on the public-facing site.
        permissions = (
            ('view_blog', 'View blog'),
        )
    
    def __unicode__(self):
        return self.title

	'''
	A model to represent each dispatch call. Notice how it relates 
	to the Type model via the Foreignkey "type" field.
	'''

class Post(models.Model):

    blog = models.ForeignKey(Blog,
                             help_text="Select the blog on which you would like this to appear. All posts will appear in the homepage news feed automatically.")
    authors = models.CharField(max_length=50)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=50, unique_for_date="publication_date",
                            help_text='Don\'t change unless you have absolute confidence in what you\'re doing.')
    body = HTMLField()
    #status = models.CharField(max_length=1, choices=PUBLICATION_STATUS_CHOICES, default=0,
    #                           help_text='Only published posts will appear on the site')
    publication_date = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return self.headline



'''
__unicode__
Each  row has all of these thigns, when we wnat to define it to ourselves when looking at the data,
 the row will be named "the shooting and 123 main st" ... if that's not there, we're going to get gobbledygook
 It'll give us a the value we want instead of something like object 1
Alright, row, self.type, self.location is how you're going to tell me your name.
'''

    
