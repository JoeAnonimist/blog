---
title: Tags
layout: default
nav_order: 100
---

<h1>Tags</h1>

<div>
<ul>
{% assign all_tags = "" %}
  {% for page in site.pages %}
    {% if page.tags %}
      {% for tag in page.tags %}
        {% assign all_tags = all_tags | append: tag | append: ',' %}
      {% endfor %}
    {% endif %}
  {% endfor %}
{% assign unique_tags = all_tags | split: ',' | uniq | sort %}
{% for tag in unique_tags %}
  <li><a href="#{{ tag | slugify }}">{{ tag }}</a></li>
{% endfor %}
</ul>

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
</div>
