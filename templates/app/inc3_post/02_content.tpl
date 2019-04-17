{% load static %}

<!-- Post Meta -->
<div class="post-meta">
  <h1 class="single-title">Example Post テストポスト</h1>
  <!-- Post Tags -->
  <ul class="post-tags">
    <li><a href="#">Manual</a></li>
    <li><a href="#">Liberty</a></li>
  </ul>
  <p><a href="#" class="post-author">Katy Liu</a> on <a href="#" class="post-date">Sep 29, 2017 at 9:48 am</a></p>
</div>
<!-- Post Content -->
<div class="post-content markdown-body">
  <div class="toc">
    <ul>
      <li><a href="#_1">リスト系</a></li>
      <li><a href="#_2">画像</a></li>
      <li><a href="#_3">コード</a></li>
      <li><a href="#_4">色を変える</a></li>
      <li><a href="#_5">テーブル</a></li>
      <li><a href="#attr_list">attr_list を使う</a></li>
    </ul>
  </div>
  <p>よく書くマークダウン</p>
  <p>
    長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章
    長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章
    長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章長い文章
  </p>
  <p>&nbsp;</p>
  <h2 id="_1">リスト系</h2>
  <ul>
    <li>リスト<ul>
        <li>リスト<ul>
            <li>リスト</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
  <dl>
    <dt>見出し</dt>
    <dd>内容</dd>
    <dd>これはあんまり整わないから使わないかもしれん。</dd>
  </dl>
  <p>&nbsp;</p>
  <h2 id="_2">画像</h2>
  <p><img alt="" src="{% static 'app/img/sample/360x195.jpg' %}" /></p>
  <p>&nbsp;</p>
  <h2 id="_3">コード</h2>
  <pre><code class="python">def foo():
    print('FOOFOO')</code></pre>
  <p>&nbsp;</p>
  <h2 id="_4">色を変える</h2>
  <p><span style="color:red;">みー</span>、つぃー、にゃー</p>
  <p>&nbsp;</p>
  <h2 id="_5">テーブル</h2>
  <table>
    <thead>
      <tr>
        <th>ひと</th>
        <th>発言</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>わたし</td>
        <td>ちわっす</td>
      </tr>
      <tr>
        <td>きみ</td>
        <td>どもっす</td>
      </tr>
    </tbody>
  </table>
  <p>&nbsp;</p>
  <h2 id="attr_list">attr_list を使う</h2>
  <p><a href="https://python-markdown.github.io/extensions/attr_list/">公式
      https://python-markdown.github.io/extensions/attr_list/</a></p>
  <style>
    #red {
      color: red;
    }

    .green {
      color: green;
    }
  </style>
  <p id="red">RED.</p>
  <pre><code class="plaintext hljs">RED.
{: #red }</code></pre>
  <p><strong class="green">GREEN.</strong></p>
  <pre><code class="plaintext hljs">**GREEN.**{: .green}</code></pre>
</div>
