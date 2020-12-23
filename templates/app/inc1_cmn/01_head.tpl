{% load static %}

<meta charset="UTF-8">
<meta name="description" content="">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<!-- The above 4 meta tags *must* come first in the head; any other head content must come *after* these tags -->

<!-- Title  -->
<title>{{page_title}}</title>

<!-- Favicon  -->
<link rel="icon" href="{% static 'favicon.ico' %}">

<!-- SNS -->
<meta property="og:type" content="blog" />
<meta property="og:site_name" content="{{site_title}}" />
<meta property="og:url" content="{{request.build_absolute_uri}}" />
<meta property="og:title" content="{{page_title}}" />
<meta property="og:description" content="{{site_desc}}" />
<meta property="og:image" content="{{mainimage_fullpath}}" />

<!-- Twitter -->
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@miroriiro">
<meta name="twitter:image" content="{{mainimage_fullpath}}" />
<meta name="twitter:title" content="{{page_title}}">
<meta name="twitter:description" content="{{site_desc}}">

<!-- Style CSS -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700|Work+Sans:300,400,500,600,700">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/magnific-popup.js/1.1.0/magnific-popup.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css">
<link rel="stylesheet" href="{% static 'app/css/themify-icons.css' %}">
<link rel="stylesheet" href="{% static 'app/vendor/github-markdown.css' %}">
<link rel="stylesheet" href="{% static 'app/vendor/highlight/default.css' %}">
<link rel="stylesheet" href="{% static 'app/style.css' %}?2020-02-23">

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-80238362-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-80238362-2');
</script>
