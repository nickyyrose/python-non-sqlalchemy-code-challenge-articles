class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, '_title'):
            self._title = title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author


    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine

class Author:

    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 1 and not hasattr(self, '_name'):
            self._name = name

    def articles(self):
        articles = []
        for article in Article.all:
            if article.author == self:
                articles.append(article)
        return articles

    def magazines(self):
        magazines = []
        for article in self.articles():
            if article.magazine not in magazines:
                magazines.append(article.magazine)
        return magazines

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        articles = self.articles()
        if articles:
            categories = []
            for article in articles:
                if article.magazine.category not in categories:
                    categories.append(article.magazine.category)
            return categories
        return None

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) >= 1:
            self._category = category

    def articles(self):
        articles = []
        for article in Article.all:
            if article.magazine == self:
                articles.append(article)
        return articles

    def contributors(self):
        contributors = []
        for article in self.articles():
            if article.author not in contributors:
                contributors.append(article.author)
        return contributors

    def article_titles(self):
        titles = []
        for article in self.articles():
            titles.append(article.title)
        if titles:
            return titles
        else:
            return None

    def contributing_authors(self):
        authors = {}
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1

        list_of_authors = []
        for author, count in authors.items():
            if count >= 2:
                list_of_authors.append(author)

        if list_of_authors:
            return list_of_authors
        else:
            return None
