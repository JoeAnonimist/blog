---
title: Tags
layout: default
nav_order: 100
---

## Tags

{% if site.tags != "" %}
  {% include include docs/collecttags.html %}
{% endif %}


<div class="post">
<h1>Tag: {{ page.tag }}</h1>
<ul>
{% for post in site.tags[page.tag] %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> ({{ post.date | date_to_string }})<br>
    {{ post.description }}
  </li>
{% endfor %}
</ul>
</div>
<hr>