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
    {% comment %}
      [(DATE)TITLE](/url-path) の形式で clipboard copy を行うボタンです。
    {% endcomment %}
    <a onclick="copyTextInClipboard('[({{post.publish_at}}){{post.title}}](/{{lang}}/{{post.code}})');">
      <i class="fab fa-markdown"></i>
    </a>

    {% if post.no_en_version %}Sorry, this page is still on translating.{% endif %}
    {{post.has_only_html_body_message}}
  </p>
</div>

<script>
  // {% comment %}
  //   文字列をクリップボードにコピーします。
  // {% endcomment %}
  const copyTextInClipboard = function (text) {
    const tempTextarea = document.createElement('textarea');
    tempTextarea.textContent = text;
    const tempBodyElement = document.getElementsByTagName('body')[0];
    tempBodyElement.appendChild(tempTextarea);
    tempTextarea.select();
    document.execCommand('copy');
    tempBodyElement.removeChild(tempTextarea);
  };
</script>

<div class="post-content markdown-body mb-30">
  {{post.body|safe}}
</div>

<div class="d-flex justify-content-between">
  <div>
    <a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-show-count="false">
      Tweet
    </a>
    <a href="https://twitter.com/intent/tweet?screen_name=miroriiro&ref_src=twsrc%5Etfw" class="twitter-mention-button" data-show-count="false">
      Tweet to @miroriiro
    </a>
    <a href="https://b.hatena.ne.jp/entry/" class="hatena-bookmark-button" data-hatena-bookmark-layout="basic-label" data-hatena-bookmark-lang="ja" title="このエントリーをはてなブックマークに追加"><img src="https://b.st-hatena.com/images/v4/public/entry-button/button-only@2x.png" alt="このエントリーをはてなブックマークに追加" width="20" height="20" style="border: none;" /></a>
  </div>
  {% comment %}
    NOTE: 記事の閲覧中に編集ページへ即座に遷移するため用意したこっそりリンクです。
          これがないと、「あっタイポがある -> admin 開く -> 該当記事を検索 -> 編集ページを開く」面倒です。
  {% endcomment %}
  <div>
    <a href="/admin/app/post/{{post.id}}/" target="_blank">
      &copy; <span class="full-year"></span> Midoriiro
    </a>
  </div>
</div>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
<script type="text/javascript" src="https://b.st-hatena.com/js/bookmark_button.js" charset="utf-8" async="async"></script>
