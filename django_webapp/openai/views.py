from django.contrib import messages
from django.shortcuts import render


# Create your views here.

def home(request):
    language_list = sorted(
        ["markup", "css", "clike", "javascript", "c", "csharp", "cpp", "dart", "django", "go", "haskell",
         "java", "kotlin", "markup-templating", "python", "regex", "rust", "scala", "sql", "typescript",
         "html"]
    )
    capitalize_lang = map(lambda x: x.capitalize(), language_list)

    if request.method == "POST":
        code = request.POST['code']
        lang = request.POST['lang']

        # Check to make sure they picked a lang
        if lang == "Select Programming Language":
            messages.success(request, "Hey! You Forgot To Pick A Programming Language...")
            return render(request, 'ai-home.html',
                          {'language_list': capitalize_lang, 'response': code, 'code': code, 'lang': lang})

        return render(request, 'ai-home.html', {'language_list': capitalize_lang, 'code': code, 'lang': lang})

    return render(request, 'ai-home.html', {'language_list': capitalize_lang})
