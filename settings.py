{% extends 'flatpages/default.html' %}

{% block title %}
{{ flatpage.title }}
{% endblock title %}

{% block content %}
    <h2>{{ flatpage.title }}</h2>
    <hr>
    <h3>Наши контакты:</h3>
{{ flatpage.content }}
{% endblock content %}
