from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.http import Http404

# Create your views here.
def index(request):
    company = models.Company.objects.filter(id=1)
    nav = models.Nav.objects.filter(on_nav=True)
    footer = models.Nav.objects.filter(in_footer=True)
    tmp = []
    for i in nav:
        tmp.append({'id':i.id, 'name':i.name})
    nav = tmp
    tmp = []
    for i in footer:
        tmp.append({'id':i.id, 'name':i.name})
    footer = tmp
    adress = 'гр.' + company[0].sity + ' ' + 'ул.' + ' ' + company[0].ulica + ' ' + '№' + company[0].nomer
    company = {'name':company[0].name, 'tel':company[0].tel, 'addres':adress, 'mail':company[0].mail, 'sity':company[0].sity, 'ulica':company[0].ulica, 'nomer':company[0].nomer}

    promotion = []
    tmp = models.Promotion.objects.filter(in_index=True)
    for i in tmp:
        promotion.append(
            {'id': i.id, 'name': i.name, 'from_price': i.from_price, 'img': i.img_url, 'to_price': i.to_price})

    return render(request, "studio/index.html", {'company':company, 'adress':adress, 'nav':nav, 'footer':footer, 'promotion': promotion, 'nav_hide':True})

def about(request):
    company = models.Company.objects.filter(id=1)
    adress = 'гр.' + company[0].sity + ' ' + 'ул.' + ' ' + company[0].ulica + ' ' + '№' + company[0].nomer
    company = {'name': company[0].name, 'tel': company[0].tel, 'addres': adress, 'mail': company[0].mail,
               'sity': company[0].sity, 'ulica': company[0].ulica, 'nomer': company[0].nomer}
    nav = models.Nav.objects.filter(on_nav=True)
    footer = models.Nav.objects.filter(in_footer=True)
    tmp = []
    for i in nav:
        tmp.append({'id': i.id, 'name': i.name})
    nav = tmp
    tmp = []
    for i in footer:
        tmp.append({'id': i.id, 'name': i.name})
    footer = tmp
    return render(request, "studio/abaut.html", {'company':company, 'adress':adress, 'nav':nav, 'footer':footer})

def pages(request, id):
    company = models.Company.objects.filter(id=1)
    adress = 'гр.' + company[0].sity + ' ' + 'ул.' + ' ' + company[0].ulica + ' ' + '№' + company[0].nomer
    company = {'name': company[0].name, 'tel': company[0].tel, 'addres': adress, 'mail': company[0].mail,
               'sity': company[0].sity, 'ulica': company[0].ulica, 'nomer': company[0].nomer}
    nav = models.Nav.objects.filter(on_nav=True)
    footer = models.Nav.objects.filter(in_footer=True)
    tmp = []
    for i in nav:
        tmp.append({'id': i.id, 'name': i.name})
    nav = tmp
    tmp = []
    for i in footer:
        tmp.append({'id': i.id, 'name': i.name})
    footer = tmp
    pages = models.Nav.objects.filter(id=id)

    if pages[0].page_type == '4':
        pages = models.EmptyPage.objects.all()
        context = pages[0].text
        return render(request, "studio/pages.html",
                      {'company': company, 'adress': adress, 'nav': nav, 'footer': footer, 'context': context})
    elif pages[0].page_type == '1':
        galery = []
        tmp = models.Galery.objects.all()
        for i in tmp:
            galery.append({'id':i.id, 'name':i.name, 'description':i.description, 'img':i.img_url})
        return render(request, "studio/galery.html", {'company':company, 'adress':adress, 'nav':nav, 'footer':footer, 'galery':galery})
    elif pages[0].page_type == '2':
        promotion = []
        tmp = models.Promotion.objects.all()
        for i in tmp:
            promotion.append({'id': i.id, 'name': i.name, 'from_price': i.from_price, 'img': i.img_url, 'to_price':i.to_price})
        return render(request, "studio/promotion.html",
                      {'company': company, 'adress': adress, 'nav': nav, 'footer': footer, 'promotion': promotion})
    elif pages[0].page_type == '3':
        question = []
        tmp = models.Question.objects.all()
        for i in tmp:
            question.append({'id': i.id, 'question': i.question, 'answer': i.answer})
        return render(request, "studio/question.html",
                      {'company': company, 'adress': adress, 'nav': nav, 'footer': footer, 'question': question})
    else:
        raise Http404
