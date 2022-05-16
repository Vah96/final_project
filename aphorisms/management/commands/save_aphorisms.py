import requests
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from tags.models import Tag
from aphorisms.models import Aphorism
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'

    authors = {}

    aphorism_list = []

    aphorism_objs = []

    tags = {}

    page = 1

    current_author_id = 0

    aphorisms_page_url = "https://quotes.toscrape.com/page/"

    def handle(self, *args, **kwargs):
        self.get_aphorisms()
        if self.aphorism_list:
            # b = Aphorism.objects.get(id=2)
            # e = Tag.objects.get(id=3326)
            # f = Tag.objects.get(id=3327)
            # f = Tag.objects.get(id=550)
            # g = Tag.objects.get(id=553)
            # h = Tag.objects.get(id=552)
            # lst = [e, f, g, h]
            # b.tags.set(lst)  # Associates Entry e with Blog b.
            # lst = [e, f]
            for item in self.aphorism_list:
                aphorism = Aphorism.objects.create(
                    text=item['text'],
                    author=item['author'],
                )

                # tag = Tag.objects.create(name=tag)
                # item_tags_as_string = ', '.join(item['tags'])
                # tags = Tag.objects.get(id=item_tags_as_string)
                aphorism.tags.set(item['tags'])
                # self.aphorism_objs.append(aphorism)

        # msg = Aphorism.objects.bulk_create(self.aphorism_objs)
        # print(msg)

    def get_aphorisms(self):
        while True:

            response = requests.get(self.aphorisms_page_url + str(self.page), headers={
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'})

            response_html = response.text

            soup = BeautifulSoup(response_html, 'html.parser')
            aphorisms = soup.select('div.quote')
            if aphorisms:
                for row in soup.select('div.quote'):
                    aphorism_tags_list = []

                    # get aphorism text as string
                    aphorism_text = row.select('span.text')[0].text.strip('”, “')

                    # get aphorism author firstname and lastname as list
                    aphorism_author = row.select('span small.author')[0].text.split(" ")

                    # check if user already exists then set author(user) id...
                    # if no create new user and only after then set author(user) id
                    author_username = self.create_username_from_name_and_surname(aphorism_author)
                    if author_username in self.authors:
                        self.current_author_id = self.authors[author_username]
                    else:
                        self.current_author_id = self.create_new_user(author_username, aphorism_author)
                        self.authors[author_username] = self.current_author_id

                    # get aphorism tags as list
                    aphorism_tags = row.select('div.tags meta.keywords')[0]['content'].split(",")

                    # save tags
                    # check if tag already exists then set tag id...
                    # if no create new tag and only after then set tag id
                    for tag in aphorism_tags:
                        if tag in self.tags:
                            aphorism_tags_list.append(self.tags[tag])
                        else:
                            new_tag = self.save_new_tag(tag)
                            aphorism_tags_list.append(new_tag)
                            self.tags[tag] = new_tag

                    self.aphorism_list.append({
                        'text': aphorism_text,
                        'author': self.current_author_id,
                        'tags': aphorism_tags_list
                    })
                else:
                    self.page += 1
            else:
                # when change the page and don't found any aphorism then break while loop
                break

        return self.aphorism_list

    @staticmethod
    def create_username_from_name_and_surname(data):
        username = ''.join(data).lower()
        return username

    @staticmethod
    def create_new_user(username, data):
        new_user = User.objects.create_user(username)
        new_user.set_password(username + 'xnu$&')
        new_user.first_name = data.pop(0)
        new_user.last_name = ' '.join(data)
        new_user.save()
        return new_user

    @staticmethod
    def save_new_tag(tag):
        tag = Tag.objects.create(name=tag)
        return tag
