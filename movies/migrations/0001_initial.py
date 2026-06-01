from datetime import date

from django.db import migrations, models


def seed_data(apps, schema_editor):
    Director = apps.get_model('movies', 'Director')
    Movie = apps.get_model('movies', 'Movie')

    Director.objects.create(
        first_name='George', last_name='Lucas', birthday=date(1944, 5, 14)
    )
    Director.objects.create(
        first_name='Steven', last_name='Spielberg', birthday=date(1946, 12, 18)
    )
    Director.objects.create(
        first_name='Rian', last_name='Johnson', birthday=date(1973, 12, 17)
    )
    Director.objects.create(
        first_name='Taika', last_name='Waititi', birthday=date(1975, 8, 16)
    )
    Director.objects.create(
        first_name='Christopher', last_name='Nolan', birthday=date(1970, 7, 30)
    )

    Movie.objects.create(
        title='Star Wars: Episode IV - A New Hope',
        release_year=1977,
        rating=8.6,
    )
    Movie.objects.create(
        title='Star Wars: Episode III - Revenge of the Sith',
        release_year=2005,
        rating=7.6,
    )
    Movie.objects.create(
        title='Star Wars: Episode VIII - The Last Jedi',
        release_year=2017,
        rating=6.9,
    )
    Movie.objects.create(
        title='American Graffiti',
        release_year=1973,
        rating=7.4,
    )
    Movie.objects.create(
        title='Jaws',
        release_year=1975,
        rating=8.1,
    )
    Movie.objects.create(
        title='Knives Out',
        release_year=2019,
        rating=7.9,
    )
    Movie.objects.create(
        title='Thor: Ragnarok',
        release_year=2017,
        rating=7.9,
    )
    Movie.objects.create(
        title='Inception',
        release_year=2010,
        rating=8.8,
    )


def unseed_data(apps, schema_editor):
    Movie = apps.get_model('movies', 'Movie')
    Director = apps.get_model('movies', 'Director')
    Movie.objects.all().delete()
    Director.objects.all().delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.RunPython(seed_data, unseed_data),
    ]
