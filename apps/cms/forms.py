from apps.forms import FormMixin
from django import forms

from apps.news.models import *


class EditNewsCategoryForms(FormMixin,forms.Form):
    pk = forms.IntegerField(error_messages={'required':'必须传入参数'})
    name = forms.CharField(min_length=1,max_length=100)

class WriteNewsForms(forms.ModelForm,FormMixin):
    category = forms.IntegerField()
    class Meta:
        model = News
        fields = ('title','desc','thumbnail','content')
        error_messages = {
            'category':{
                'required':'必须传入分类的ID'
            },
        }