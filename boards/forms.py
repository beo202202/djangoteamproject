from django import forms
from .models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['board_id', 'content', 'img']

    def clean_img(self):
        img = self.cleaned_data.get('img')
        if img and img.size > 2 * 1024 * 1024:  # 2mb
            raise forms.ValidationError('이미지 크기는 최대 2mb까지 가능해요.')
        return img
