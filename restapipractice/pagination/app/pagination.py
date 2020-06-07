
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class MyPagination1(PageNumberPagination): # it is mandatory to declare this class then only it will work
	page_size = 5
	page_query_param = 'mypage' # for changing query parameter from page to mypage
	page_size_query_param = 'num'
	max_page_size = 15
	last_page_strings = ('endpage',)



# Limit offset pagination concept starts here

class MyPagination2(LimitOffsetPagination): # it is mandatory to declare this class then only it will work
	default_limit = 15
	limit_query_param = 'mylimit'
	offset_query_param = 'myoffset'
	max_limit = 20

class MyPagination3(CursorPagination): # it is mandatory to declare this class then only it will work
	ordering ='-esal' # If we want our result to come in sorting format then we go for cursor pagination
	page_size = 5
