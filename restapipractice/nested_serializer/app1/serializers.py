from rest_framework.serializers import ModelSerializer
from app1.models import Book,Author


class BookSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = '__all__'

class AuthorSerializer(ModelSerializer):
	books_by_author = BookSerializer(read_only = True, many = True)
	class Meta:
		model = Author
		fields = '__all__'

