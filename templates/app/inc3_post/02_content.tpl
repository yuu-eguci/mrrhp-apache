{% load static %}

<div class="post-meta">
  <h1 class="single-title">{{post.title}}</h1>
  {% if post.tag %}
  <ul class="post-tags">
    <li><a href="/{{lang}}/tags/{{post.tag.code}}">{{post.tag.name}}</a></li>
  </ul>
  {% endif %}
  <p>
    {{post.publish_at}}
    {% if post.no_en_version %}Sorry, this page is still on translating.{% endif %}
  </p>
</div>
<div class="post-content markdown-body">
  {{post.body|safe}}
</div>
