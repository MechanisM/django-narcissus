from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import simplejson as json

from narcissus.models import UpdatePost, ArticlePost


class PostTestCase(TestCase):
    """Test the built-in post models."""

    def test_update(self):
        update = UpdatePost(
            message="What I do, I do for the good of the universe. Something "
                    "you lost sight of thousands of years ago."
        )
        self.assertEqual(str(update),
                         "What I do, I do for the good of the ...")

    def test_article(self):
        content = (
            "# War of the Green Lanterns\n\n"
            "As _Sinestro_ fights _Krona_, a green power ring comes to him, "
            "making _Sinestro_ a **Green Lantern** once more."
        )

        article = ArticlePost(
            title="Sinestro wields green power ring once again",
            content=content,
            markup="markdown"
        )

        rendered = (
            "<h1>War of the Green Lanterns</h1>\n<p>As <em>Sinestro</em> "
            "fights <em>Krona</em>, a green power ring comes to him, making "
            "<em>Sinestro</em> a <strong>Green Lantern</strong> once more.</p>"
        )

        self.assertEqual(article.rendered_content, rendered)
        self.assertEqual(article.word_count, 23)
        self.assertEqual(article.get_teaser(), rendered)


class DashboardViewTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Hal',
                                        email='hjordan@oa.com')

        self.common_fields = {
            'status': 1,
            'slug': 'slug',
            'language': 'en',
            'author': self.user.pk,
            'tags': None,
        }

    def test_home_view(self):
        """
        Requests for the home view should be successful and include the current
        post types in the context.
        """
        from narcissus.dashboard import posttypes

        response = self.client.get(reverse('narcissus-home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['posttypes'], posttypes)

    def test_new_update(self):
        """Test the creation of new updates using the Ajax interface."""
        url = reverse('narcissus-new-post', args=['update'])
        response = self.client.post(url, dict(self.common_fields,
            message="I'm a little teapot.",
        ), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['success'], True)

        post = UpdatePost.objects.latest('created_date')
        self.assertEqual(post.message, "I'm a little teapot.")

    def test_new_article(self):
        url = reverse('narcissus-new-post', args=['article'])
        response = self.client.post(url, dict(self.common_fields,
            title='Joe needs some soda',
            content="Joe's epic journey takes him through two worlds.",
            markup='markdown',
        ), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['success'], True)

        post = ArticlePost.objects.latest('created_date')
        self.assertEqual(post.title, 'Joe needs some soda')
