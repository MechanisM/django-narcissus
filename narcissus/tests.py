from django.core.urlresolvers import reverse
from django.test import TestCase

from narcissus.models import UpdatePetal, ArticlePetal


class PetalModelTestCase(TestCase):
    """
    Test the petal models, which are the various built-in content types.
    """

    def test_update_petal(self):
        update = UpdatePetal(
            message="What I do, I do for the good of the universe. Something "
                    "you lost sight of thousands of years ago."
        )
        self.assertEqual(str(update), "What I do, I do for the good of the ...")

    def test_article_petal(self):
        content = "# War of the Green Lanterns\n\n"
        content += "As _Sinestro_ fights _Krona_, a green power ring comes to "
        content += "him, making _Sinestro_ a *Green Lantern* once more."

        article = ArticlePetal(
            title="Sinestro wields green power ring once again",
            content=content,
            markup="markdown"
        )

        rendered = "<h1>War of the Green Lanterns</h1>\n<p>As <em>Sinestro</em>"
        rendered += " fights <em>Krona</em>, a green power ring comes to him, "
        rendered += "making <em>Sinestro</em> a <em>Green Lantern</em> once "
        rendered += "more.</p>"

        self.assertEqual(article.rendered_content, rendered)
        self.assertEqual(article.word_count, 23)
        self.assertEqual(article.get_teaser(), rendered)


class GardenViewTestCase(TestCase):

    def test_home_view(self):
        """
        Requests for the home view should be successful and include the current
        flowers in the context.
        """
        from narcissus.garden import flowers

        response = self.client.get(reverse('narcissus-home'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['flowers'], flowers)
