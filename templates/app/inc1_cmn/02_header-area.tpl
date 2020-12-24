{% load static %}

<!-- Preloader Start -->
<div id="preloader">
  <div class="preload-content">
    <div id="world-load"></div>
  </div>
</div>
<!-- Preloader End -->

<!-- ***** Header Area Start ***** -->
<header class="header-area">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <nav class="navbar navbar-expand-lg">
          <!-- Logo -->
          <a class="navbar-brand" href="/{{lang}}/"><img src="{% static 'app/img/core/mrrhp-logo-white.png' %}" alt="Logo"></a>
          <!-- Navbar Toggler -->
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#worldNav" aria-controls="worldNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
          <!-- Navbar -->
          <div class="collapse navbar-collapse" id="worldNav">
            <ul class="navbar-nav ml-auto">
              <li class="nav-item {% if is_top_page %}active{% endif %}">
                <a class="nav-link" href="/{{lang}}/">
                  <i class="fas fa-home"></i> TOP
                </a>
              </li>
              <li class="nav-item {% if is_latest_page %}active{% endif %}">
                <a class="nav-link" href="/{{lang}}/latest/">
                  <i class="fas fa-flag"></i> LATEST
                </a>
              </li>
              <li class="nav-item dropdown {% if is_tag_page %}active{% endif %}">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="fas fa-tags"></i> TAGS
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  {% for tag in tags %}
                    <a class="dropdown-item" href="/{{lang}}/tags/{{tag.code}}">
                      {{tag.name}} ({{tag.count}})
                    </a>
                  {% endfor %}
                </div>
              </li>
              <li class="nav-item dropdown {% if is_year_page %}active{% endif %}">
                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  <i class="fas fa-calendar-alt"></i> YEAR
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                  {% for year in years %}
                    <a class="dropdown-item" href="/{{lang}}/years/{{year.code}}">
                      {{year.code}} ({{year.count}})
                    </a>
                  {% endfor %}
                </div>
              </li>
            </ul>
            <!-- Search Form  -->
            <div id="search-wrapper">
              <form action="/{{lang}}/search/" method="get">
                <input type="text" id="search" placeholder="検索" name="s" value="{{search_words}}">
                <div id="close-icon"></div>
                <input class="d-none" type="submit">
              </form>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
</header>
<!-- ***** Header Area End ***** -->
