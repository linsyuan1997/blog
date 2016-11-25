from populate import base
from book.models import book
import random

def populate():
    print('Populating book and Comment...', end='')
    titles = ['如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django'
              '如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django'
              '如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django'
              '如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django'
              '如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django'
              '如何像電腦科學家一樣思考', '10 分鐘內學好 Python', '簡單學習 Django']
    
    authors = ['張三','李四','王五','照六','前七']
    
    book.objects.all().delete()
    for titles in titles:
    
    
    print('done')
if __name__ == '__main__':
    populate()