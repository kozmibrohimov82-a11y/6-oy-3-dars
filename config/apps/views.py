

from django.http import HttpResponse,HttpRequest

def index(requests:HttpRequest):
    return HttpResponse("""<h1 style="color:#3527F5; text-align: center;"> Salom clubga hush kelibsiz </h1>""")

def about(requests:HttpRequest):
    return HttpResponse("""<h1 style="color:#3527F5; text-align: center;"> Salom bu club sizga erkinlik va kuch beradi </h1>""")

def info(requests:HttpRequest):
    return HttpResponse( (   """<div style="text-align: center; margin-top: 50px;">
            <h1 style="color: #3527F5;">Salom clubga xush kelibsiz</h1>
            <input type="text" placeholder="Ismingizni yozing..." style="padding: 10px; border-radius: 5px; border: 1px solid #3527F5;">
            <button style="padding: 10px 20px; background-color: #3527F5; color: white; border: none; border-radius: 5px; cursor: pointer;">
                Yuborish
            </button>
        </div>
    """))
