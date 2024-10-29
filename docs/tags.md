---
title: Tags
layout: default
nav_order: 100
---

## Tags

{% assign page_tags = "" | split: ',' %}
{% assign post_tags = "" | split: ',' %}
{% assign all_tags = "" | split: ',' %}

{% comment %}
# get all post tags
{% endcomment %}


{% capture post_tags %}
  {% for tag in site.tags %}
    {{ tag[0] }}
  {% endfor %}
{% endcapture %}
{% assign tags = post_tags | strip_newlines | split:' ' %}

{% comment %}
# get all unique page tags
{% endcomment %}

{%- for page in site.pages -%}
  {% assign page_tags = page_tags | concat:page.tags %}
{%- endfor -%}

{%- assign post_tags = post_tags | remove: "\n" | split: " " -%}


{% comment %}
# debug prints

post_tags
{{post_tags | jsonify}}

page_tags
{{page_tags | jsonify}}

{% endcomment %}

{% comment %}
# concat was injecting line breaks here, so had to hammer
# it the old fashioned way to avoid concat
{% endcomment %}

{% for tag in post_tags %}
  {% assign all_tags = all_tags | push: tag %}
{% endfor %}

{% for tag in page_tags %}
  {% assign all_tags = all_tags | push: tag %}
{% endfor %}

{% assign sortedtags = all_tags | uniq | sort%}

{% for tag in sortedtags %}
  {% assign all_tagged = "" | split: ',' %}

  <h3 id="{{ tag }}">{{ tag }}</h3>
  <ul>

  {% comment %}
  # combine posts and pages with this tag
  {% endcomment %}

  {% for post in site.tags[tag]%}
    {% assign all_tagged = all_tagged | push: post %}
  {% endfor %}

  {% for page in site.pages %}
    {% if page.tags contains tag %}
      {% assign all_tagged = all_tagged | push: page %}
    {% endif %}
  {% endfor %}

  {% comment %}
  # sort by title
  {% endcomment %}
  {% assign all_tagged = all_tagged | sort: "title" %}


  {% comment %}
  # finally, print the list item!
  {% endcomment %}
  {% for tagged in all_tagged %}
    <li><a href="{{ tagged.url }}">{{ tagged.title }}</a></li>
  {% endfor %}

  </ul>
{% endfor %}