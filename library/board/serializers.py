from rest_framework import serializers
from .models import Map, OffDay, NewsBoard, SuggestBoard


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = "__all__"


class OffDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = OffDay
        fields = "__all__"


class NewsBoardSerializer(serializers.ModelSerializer):
    news_poster = serializers.ImageField(use_url=True)

    class Meta:
        model = NewsBoard
        ordering = ['timestamp', 'id']
        fields = ('news_title', 'news_content', 'news_poster', 'news_date', 'id')


class SuggestBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestBoard
        ordering = ['timestamp', 'id']
        fields = "__all__"

