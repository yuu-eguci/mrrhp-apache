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

<!-- Style CSS -->
<link rel="stylesheet" href="{% static 'app/style.css' %}?2019-05-25">

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-80238362-2"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-80238362-2');
</script>
