from django.forms import ModelForm
from .models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'body']

    def clean(self):
        # data from the form is fetched using super function
        super(ArticleForm, self).clean()
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        body = self.cleaned_data.get('body')
        # conditions to be met for the username length
        if len(name) < 5:
            self._errors['name'] = self.error_class([
                'Minimum 5 characters required'])
        if len(body) > 10:
            self._errors['body'] = self.error_class([
                'Post Should not Contain a more than 10 characters'])
        return self.cleaned_data
