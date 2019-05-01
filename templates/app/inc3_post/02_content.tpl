{% load static %}

<!-- Post Meta -->
<div class="post-meta">
  <h1 class="single-title">{{post.title}}</h1>
  <!-- Post Tags -->
  <ul class="post-tags">
    <li><a href="/{{lang}}/tags/{{post.tag.code}}">{{post.tag.name}}</a></li>
  </ul>
  <p>
    {{post.publish_at}}
    {% if post.no_en_version %}Sorry, this page is still on translating.{% endif %}
  </p>
</div>
<!-- Post Content -->
<div class="post-content markdown-body">
  {{post.body|safe}}
</div>
