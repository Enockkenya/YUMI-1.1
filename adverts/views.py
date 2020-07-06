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




def adverts_list_by_category(request, category_slug):
    category = None
    categories = Category.objects.all()
    category = Category.objects.filter(slug=category_slug)
    adverts = Advert.objects.filter(available=True)
    adverts2 = Advert.objects.filter(available=True)
    paginator = Paginator(adverts, 1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        adverts = Advert.objects.filter(category=category)
        adverts2 = Advert.objects.filter(category=category)
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
        'adverts2' : adverts2,
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


def advert_detail(request, id, slug):
    advert = get_object_or_404(Advert, id=id , slug=slug, available=True)
    return render( request, 'listings/advertdetail.html', context = {
        'advert': advert,
        'local_css_urls': settings.SB_ADMIN_2_CSS_LIBRARY_URLS,
        'local_js_urls': settings.SB_ADMIN_2_JS_LIBRARY_URLS,
    }
      )


def review_ad_seller(request):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})






  

