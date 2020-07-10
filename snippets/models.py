from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = (lexer for lexer in get_all_lexers() if lexer[1])
LANGUAGE_CHOICES = sorted((item[1][0], item[0]) for item in LEXERS)
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(
        to="auth.User", on_delete=models.CASCADE, related_name="snippets"
    )
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}

        self.highlighted = highlight(
            self.code,
            get_lexer_by_name(self.language),
            HtmlFormatter(style=self.style, linenos=linenos, full=True, **options),
        )

        super().save(*args, **kwargs)

    class Meta:
        ordering = ["created"]
