---
title: Tags
layout: default
nav_order: 100
---

## Tags

<h1>Tags</h1>
<ul>
{% for tag in site.tags %}
  <li><a href="#{{ tag[0] }}">{{ tag[0] }}</a> ({{ tag[1].size }})</li>
{% endfor %}
</ul>

{% for tag in site.tags %}
  <h2 id="{{ tag[0] }}">{{ tag[0] }}</h2>
  <ul>
  {% for post in tag[1] %}
    <li><a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
  </ul>
{% endfor %}