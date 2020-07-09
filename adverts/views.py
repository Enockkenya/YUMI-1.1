import json
from django.db.models import F
from django.utils import timezone
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.models import User
from adverts.forms import PostadForm, ReviewAdForm
from adverts.models import *
from account.views import profile
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.urls import reverse_lazy, reverse



@login_required(login_url ='login:login_redirect')
def post_ad(request):
    if request.method == 'POST':
       
        post_form = PostadForm(request.POST, files=request.FILES)
        
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

    print(post_form.is_valid())
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

    
    return render(request, 'listings/postad.html', {
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
    if request.method == 'POST':
        advert = get_object_or_404(Advert, id =id)
        user = request.user
        advert.likes.add(user)
    messages.success(request, _('Your ad was successfully posted!'))
    return redirect('adverts:advert_detail', id=advert.id, slug=advert.slug )
        
    

def adverts_list_by_category(request, category_slug):
    category = None
    categories = Category.objects.all()
    category = Category.objects.filter(slug=category_slug)
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



def adverts_list(request):
    categories = Category.objects.all()
    adverts = Advert.objects.filter(available=True)
    paginator = Paginator(adverts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    else:
        next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    else:
        prev_url = ''
        

    return render(request, 'listings/advertlist.html',   context = {
        'adverts' : adverts,
        'categories': categories,
        'category':'category',
        'page': page, 
        'next_page_url' : next_url,
        'prev_page_url': prev_url,
        'tab': 'listings',
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    }) 

@login_required(login_url ='login:login_redirect')
def advert_detail(request, id, slug):
    advert = get_object_or_404(Advert, id=id , slug=slug, available=True)
    ad_seller =  advert.user
    reviews = ad_seller.seller_reviews.all()
    total_likes= advert.total_likes
    print(total_likes)
    new_comment = None
    if request.method == 'POST':
        comment_form = ReviewAdForm(data=request.POST)
        if comment_form.is_valid():

            # Create  object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current review to the advert owner
            new_comment.reviewer = request.user
            new_comment.adseller = ad_seller
            if new_comment.reviewer == new_comment.adseller:
                new_comment = None
                messages.error(request,'You cannot review yourself')

            else:
                new_comment.save()
                messages.success(request,'Your review has been published')
    else:
        comment_form = ReviewAdForm(data=request.POST)
    return render( request, 'listings/advertdetail.html', context={
        'advert': advert,
        'reviews': reviews,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    }
      )



    





  

