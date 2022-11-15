import os
from django.conf import settings
from summary.models import User_Model
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .alogs import throughURL
from .twitter import create_tweet
# from alogs import sum_url


# GLOBAL VARIABLES

fileDIR = "files/"


def dashboard(request):
    if request.session.get('UserName') is None:
        return HttpResponseRedirect('login')
    else:
        context = {
            'userName': request.session.get('UserName')
        }

        return render(request, 'logged_pages/dashboard.html', context=context)


def fromURL(request):
    userName = request.session.get('UserName')
    if request.method == 'GET':
        context = {
            'userName': userName
        }
        return render(request, 'logged_pages/fromURL.html', context=context)
    else:
        frm_URL_ARTICLE = request.POST.get('frm_URL')
        # return HttpResponse(frm_URL_ARTICLE)
        summary = throughURL(frm_URL_ARTICLE)
        char_count = summary.count('')
        word_count = summary.count(' ')
        author = "TestAuthor"
        return HttpResponse(summaryPage(summary, author, char_count, word_count, userName, request))


def fromPDF(request):
    userName = request.session.get('UserName')

    if request.method == 'GET':
        context = {
            'userName': userName
        }
        return render(request, 'logged_pages/fromPDF.html', context=context)
    else:
        frm_URL_ARTICLE = request.POST.get('url')
        frm_uploadedFile = request.FILES.get('filepdf')

        handle_uploaded_file(fileDIR+frm_uploadedFile.name, frm_uploadedFile)

        summary = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum laboriosam eius, eaque rerum at, similique eos qui consequatur ipsum veritatis sed, temporibus labore perferendis nisi quidem dicta accusantium optio repellat ab corporis unde. Est, accusantium, alias autem non quam ipsam voluptas necessitatibus cumque nobis labore aspernatur ea? At quis soluta iste consequuntur eum laboriosam voluptas?"
        char_count = summary.count('')
        word_count = summary.count(' ')
        author = "TestAuthor"
        return HttpResponse(summaryPage(summary, author, char_count, word_count, userName, request))


def fromDOCX(request):
    userName = request.session.get('UserName')

    if request.method == 'GET':
        context = {
            'userName': userName
        }
        return render(request, 'logged_pages/fromDOCX.html', context=context)
    else:
        frm_URL_ARTICLE = request.POST.get('url')
        frm_uploadedFile = request.FILES.get('filedocx')

        handle_uploaded_file(fileDIR+frm_uploadedFile.name, frm_uploadedFile)

        summary = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum laboriosam eius, eaque rerum at, similique eos qui consequatur ipsum veritatis sed, temporibus labore perferendis nisi quidem dicta accusantium optio repellat ab corporis unde. Est, accusantium, alias autem non quam ipsam voluptas necessitatibus cumque nobis labore aspernatur ea? At quis soluta iste consequuntur eum laboriosam voluptas?"
        char_count = summary.count('')
        word_count = summary.count(' ')
        author = "TestAuthor"
        return HttpResponse(summaryPage(summary, author, char_count, word_count, userName, request))


def fromTXT(request):
    userName = request.session.get('UserName')

    if request.method == 'GET':
        context = {
            'userName': userName
        }
        return render(request, 'logged_pages/fromTXT.html', context=context)
    else:
        frm_URL_ARTICLE = request.POST.get('url')
        frm_uploadedFile = request.FILES.get('filetxt')

        handle_uploaded_file(fileDIR+frm_uploadedFile.name, frm_uploadedFile)

        summary = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum laboriosam eius, eaque rerum at, similique eos qui consequatur ipsum veritatis sed, temporibus labore perferendis nisi quidem dicta accusantium optio repellat ab corporis unde. Est, accusantium, alias autem non quam ipsam voluptas necessitatibus cumque nobis labore aspernatur ea? At quis soluta iste consequuntur eum laboriosam voluptas?"
        char_count = summary.count('')
        word_count = summary.count(' ')
        author = "TestAuthor"
        return HttpResponse(summaryPage(summary, author, char_count, word_count, userName, request))


# GLOBAL FUNCTIONS
def handle_uploaded_file(filePassingDir, file):

    with open(filePassingDir, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    print("file Uploaded")


def summaryPage(summaryText, author, char_count, word_count, userName, request):
    context = {
        'summary': summaryText,
        'AutorName': author,

        'char_count': char_count,
        'word_count': word_count,
        'userName': userName
    }
    return render(request, 'logged_pages/sum_fromURL.html', context=context)


def sendRequest(request):
    if request.method == 'POST':
        text = request.POST.get('summary')
        author = request.POST.get('author')
        return HttpResponse(makeTweet(text, author))


def makeTweet(tweet_txt, author):
    create_tweet(tweet_txt)
    return "Tweet Successfully created"

# ==================
# ALGOS
# ==================


def sum_url(url):

    return True
