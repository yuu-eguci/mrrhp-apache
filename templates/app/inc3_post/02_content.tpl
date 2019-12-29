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
    {{post.has_only_html_body_message}}
  </p>
</div>

<div class="post-content markdown-body mb-30">
  {{post.body|safe}}
</div>

<div class="social-buttons">
  <div>
    <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">
      Tweet
    </a>
  </div>
  <div>
    <a href="https://twitter.com/intent/tweet?screen_name=miroriiro&ref_src=twsrc%5Etfw" class="twitter-mention-button" data-show-count="false">
      Tweet to @miroriiro
    </a>
  </div>
  <div>
    <a href="https://b.hatena.ne.jp/entry/" class="hatena-bookmark-button" data-hatena-bookmark-layout="basic-label" data-hatena-bookmark-lang="ja" title="このエントリーをはてなブックマークに追加"><img src="https://b.st-hatena.com/images/v4/public/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a>
  </div>
</div>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<script type="text/javascript" src="https://b.st-hatena.com/js/bookmark_button.js" charset="utf-8" async="async"></script>
