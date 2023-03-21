from celery import shared_task

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from NewsApp.models import PostCategory
from .settings import SITE_URL, DEFAULT_FROM_EMAIL
import datetime


@shared_task
def send_notifications(preview, pk, title, subscribers):
    html_context = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/posts/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject = title,
        body = '',
        from_email = DEFAULT_FROM_EMAIL,
        to = subscribers,
    )

    msg.attach_alternative(html_content, 'text/html'),
    msg.send()


@shared_task
@receiver(post_save, sender=PostCategory)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        subscribers: list[str] = []
        for category in categories:
            subscribers += category.subcribers.all()

        subscribers = [s.email for s in subscribers]

        send_notifications(instance.preview(), instance.pk, instance.title, subscribers)

@shared_task
def notify_weekly():
    today = datetime.datetime.now()
    last_week=today-datetime.timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    print(posts)
    categories = set(posts.values_list('postCategory__name', flat=True))
    print(categories)
    subscribers = set(Category.objects.filter(name__in=categories).values_list("subscribers__email", flat=True))
    print(subscribers)
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    print(html_content)
    msg = EmailMultiAlternatives(
        subject="Статьи за прошедшую неделю",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

