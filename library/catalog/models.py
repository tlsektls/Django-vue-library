from django.db import models
from django.utils.timezone import now
from django.urls import reverse
import uuid

from django.utils.translation import ugettext_lazy as _

# Create your models here.

class MyModelName(models.Model):
  """A typical class defining a model, derived from the Model class."""

  # Fields
  my_field_name = models.CharField(
      max_length=20, help_text='Enter field documentation')

# Metadata


class Meta:
	ordering = ['title', '-my_field_name']
  
	# Methods
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of MyModelName."""
		return reverse('model-detail-view', args=[str(self.id)])

	def __str__(self):
		"""String for representing the MyModelName object (in Admin site etc.)."""
		return self.field_name


class Book(models.Model):
  """Model representing a book (but not a specific copy of a book)."""
  title = models.CharField(max_length=200)
  author = models.ManyToManyField('Author', related_name='b_author')
  publisher = models.ForeignKey(
      'Publisher', on_delete=models.SET_NULL, null=True)

  create_date = models.DateField(default=now)

  summary = models.TextField(
      max_length=1000, help_text='책소개 혹은 줄거리를 작성해 주세요')
  isbn = models.CharField(
      'ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

  genre = models.ManyToManyField(
      'Genre', related_name='b_genre')

  language = models.ForeignKey(
      'Language', on_delete=models.SET_NULL, null=True, related_name='books')
  #language = models.ForeignKey(
  #    'Language', on_delete=models.SET_NULL, null=True)

  image = models.ImageField(null=True, upload_to="", blank=True)
  def get_image(self, car):
    request = self.context.get('request')
    image = self.image.url
    return request.build_absolute_uri(image)


  def __str__(self):
    """String for representing the Model object."""
    return self.title

  def get_absolute_url(self):
    """Returns the url to access a detail record for this book."""
    return reverse('book-detail', args=[str(self.id)])

  def display_author(self):
    return ', '.join(author.name for author in self.author.all())
    
  def display_genre(self):
    """Create a string for the Genre. This is required to display genre in Admin."""
    return ', '.join(genre.name for genre in self.genre.all()[:3])

  def visited(request):
    "#Number of visits to this view, as counted in the session variable."
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return num_visits


class BookInstance(models.Model):
  """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
  id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                        help_text='Unique ID for this particular book across whole library')
  book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
  imprint = models.CharField(max_length=200)
  due_back = models.DateField(null=True, blank=True)

  LOAN_STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On loan'),
    ('a', 'Available'),
    ('r', 'Reserved'),
  )

  status = models.CharField(
    max_length=1,
    choices=LOAN_STATUS,
    blank=True,
    default='m',
    help_text='Book availability',
  )


class Meta:
	ordering = ['due_back']

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.book.title})'


class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
      """String for representing the Model object (in Admin site etc.)"""
      return self.name


class Author(models.Model):
  """Model representing an author."""
  name = models.CharField(max_length=100)
  date_of_birth = models.DateField(null=True, blank=True)
  date_of_death = models.DateField('Died', null=True, blank=True)
  #info = models.TextField(max_length=1000, help_text='저자 소개를 작성해 주세요', null=True, blank=True)
  intro = models.TextField(max_length=1000, help_text='저자 소개를 작성해 주세요', null=True, blank=True)

  class Meta:
    ordering = ['name']

  def get_absolute_url(self):
    """Returns the url to access a particular author instance."""
    return reverse('author-detail', args=[str(self.id)])

  def __str__(self):
    """String for representing the Model object."""
    return self.name


class Publisher(models.Model):
  """Model representing an Publisher."""
  name = models.CharField(max_length=60)

  def __str__(self):
    return self.name


class Genre(models.Model):
  """Model representing a book genre."""
  name = models.CharField(
      max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

  def __str__(self):
    """String for representing the Model object."""
    return self.name



#from django.db import models
#class BookImage(models.Model):
#  title = models.TextField(max_length=40, null=True)
#  imgfile = models.ImageField(null=True, upload_to="", blank=True)
#  content = models.TextField()

#  def __str__(self):
#    return self.title