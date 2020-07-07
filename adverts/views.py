import json
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from adverts.forms import PostadForm
from adverts.models import *
from account.views import profile
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect




@login_required(login_url ='login:login_redirect')
def post_ad(request):
    if request.method == 'POST':
       
         # user_form = RegisterForm(request.POST,instance=request.user)
        post_form = PostadForm(request.POST,files=request.FILES)
        
        if post_form.is_valid():
            post_form=post_form.save(commit=False)
            post_form.slug = slugify(post_form.name)
            post_form.user=request.user
            post_form.save()
            messages.success(request, _('Your ad was successfully posted!'))
            return redirect('account:view_my_ads', user_id=request.user.id )

        else:
            messages.error(request, _('Please correct the error below.'))
    else:
         post_form = PostadForm(instance=request.user)
           

    return render(request, 'listings/postad.html', {
        # 'user_form': user_form,
        'post_form': post_form,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })

@login_required(login_url ='login:login_redirect')
def update_post(request, id, ):
    advert = get_object_or_404(Advert, id=id,  )
    post_form = PostadForm(instance=advert, )
    if request.method == 'POST':
       
         # user_form = RegisterForm(request.POST,instance=request.user)
        post_form = PostadForm(request.POST,instance=advert)
        
        if post_form.is_valid():
            # post_form.slug = slugify(post_form.name)
            post_form.user=request.user
            post_form.save()
            messages.success(request, _('Your ad was successfully posted!'))
            return redirect('account:view_my_ads', user_id=request.user.id )

        else:
            messages.error(request, _('Please correct the error below.'))

    
    return render(request, 'listings/edit_ad.html', {
        'post_form': post_form,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


@login_required(login_url ='login:login_redirect')
def delete_post(request, id, ):
    advert = get_object_or_404(Advert, id=id,  )
    if request.method == 'POST':
        advert.delete()
        return redirect('account:view_my_ads', user_id=request.user.id )
     
    
    return render(request, 'listings/deletead.html', {
        'advert': advert,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


def like_ad(request, id):
    advert = get_object_or_404(Advert, id=id, )
    advert.likes.add(request.user)
    return HttpResponseRedirect(reverse('adverts:advert_detail', id='advert.id'),{
        'advert': advert,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })




# @login_required(login_url='/accounts/login/')
def adverts_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    adverts = Advert.objects.filter(available=True)
    paginator = Paginator(adverts, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        adverts = Advert.objects.filter(category=category)
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
        

    return render(request, 'listings/advertlist.html',   context = {
        'category': category,
        'categories': categories,
        'adverts' : adverts,
        'page': page, 
        'next_page_url' : next_url,
        'prev_page_url': prev_url,
        'tab': 'listings',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    })


def advert_detail(request, id, slug):
    advert = get_object_or_404(Advert, id=id , slug=slug, available=True)
    return render( request, 'listings/advertdetail.html', context = {
        'advert': advert,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    }
      )










  

