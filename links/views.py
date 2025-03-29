from django.shortcuts import render, redirect, get_object_or_404
from .models import Link  # Ensure you have a Link model

def index(request):
    if request.method == 'POST':
        # Handle link creation
        name = request.POST.get('name', '')
        url = request.POST.get('url')
        
        # Create a new link
        Link.objects.create(name=name, url=url)
        return redirect('index')
    
    # Fetch all links for display
    links = Link.objects.all()
    return render(request, "links/index.html", {"links": links})

def edit_link(request, slug):
    link = get_object_or_404(Link, slug=slug)
    if request.method == 'POST':
        # Update the link
        link.name = request.POST.get('name', link.name)
        link.url = request.POST.get('url', link.url)
        link.save()
        return redirect('index')
    
    return render(request, "links/edit.html", {"link": link})

def delete_link(request, slug):
    link = get_object_or_404(Link, slug=slug)
    if request.method == 'POST':
        # Delete the link
        link.delete()
        return redirect('index')
    
    return render(request, "links/delete.html", {"link": link})