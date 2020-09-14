from django.shortcuts import render

# Create your views here.

def get_list(request):
    articles = [
        {
            "title":"Card No 1",
            "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.",
            "img_url":"http://placehold.it/500x325"
        },
        {
            "title":"Card No 1",
            "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.",
            "img_url":"http://placehold.it/500x325"
        },
        {
            "title":"Card No 1",
            "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.",
            "img_url":"http://placehold.it/500x325"
        },
        {
            "title":"Card No 1",
            "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.",
            "img_url":"http://placehold.it/500x325"
        },
    ]
    context = {
        "list":articles
    }
    return render(request, 'website/home/index.html', context)
def get_details(request):
    article = {
        "title":"Card No 1",
        "description":"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sapiente esse necessitatibus neque.",
        "img_url":"http://placehold.it/500x325"
    }
    context = {
        "article":article
    }
    return render(request, 'website/details/index.html', context)
