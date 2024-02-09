from .models import Article
from django.urls import reverse
from .forms import ArticleForm

class ArticleModelTest(TestCase):
    def test_string_representation(self):
        article = Article(title="Sample title")
        self.assertEqual(str(article), article.title)
    
    def test_article_creation(self):
        article = Article.objects.create(title="Test title", content="Test content")
        self.assertTrue(isinstance(article, Article))
        self.assertEqual(article.title, "Test title")

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class ArticleFormTest(TestCase):
    def test_form_validity(self):
        form_data = {'title': 'Test title', 'content': 'Test content'}
        form = ArticleForm(data=form_data)
        self.assertTrue(form.is_valid())

class APITests(TestCase):
    def test_get_articles(self):
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), Article.objects.count())
