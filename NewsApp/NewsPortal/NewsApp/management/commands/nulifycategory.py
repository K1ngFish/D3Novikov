from django.core.management.base import BaseCommand, CommandError
from NewsApp.models import Post, Category

class Command(BaseCommand):
    help = 'Команда для удаления всех постов из категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы хотите удалить все статьи в категории {options["category"]}? y/n: ')

        if answer != 'y':
            self.stdout.write(self.style.ERROR('Запрос удаления отменен!'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(postCategory = category).delete()
            self.stdout.write(self.style.SUCCESS(f'Все посты из категории {category.name} успешно удалены'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Не удалось найти категорию'))

