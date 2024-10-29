---
title: Tags
layout: default
nav_order: 100
---

<h1>Tags</h1>


{% for tag in unique_tags %}
  {% unless tag == "" %}
    <h2 id="{{ tag | slugify }}">{{ tag }}</h2>
    <ul>
      {% for page in site.pages %}
        {% if page.tags and page.tags contains tag %}
          <li><a href="{{ page.url | relative_url }}">{{ page.title }}</a></li>
        {% endif %}
      {% endfor %}
    </ul>
  {% endunless %}
{% endfor %}
