from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def return_response(request):
    
    data = request.GET
    
    if data:
        
        title = data.get('title')
        author = data.get('author')
        text = data.get('text')
        
        if title and author and text:
            return HttpResponse(f"{data['author'].title()} nomli muallif tomonidan yozilgan {data['title'].capitalize()} nomli post bazaga qo'shildi")
    
    return HttpResponse('Assalomu alaykum')
        
        