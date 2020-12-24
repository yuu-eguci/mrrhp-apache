{% load static %}

{% if next_post %}
<a id="linkNext" href="/{{lang}}/{{next_post.code}}" title="{{next_post.title}}">
  <i class="fas fa-step-forward"></i>
</a>
{% endif %}
{% if previous_post %}
<a id="linkPrev" href="/{{lang}}/{{previous_post.code}}" title="{{previous_post.title}}">
  <i class="fas fa-step-backward"></i>
</a>
{% endif %}
