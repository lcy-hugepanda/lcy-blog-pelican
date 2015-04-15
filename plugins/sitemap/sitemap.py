


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>pelican-plugins/sitemap.py at master · getpelican/pelican-plugins</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="getpelican/pelican-plugins" name="twitter:title" /><meta content="pelican-plugins - Collection of plugins for the Pelican static site generator" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/2043492?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/2043492?v=3&amp;s=400" property="og:image" /><meta content="getpelican/pelican-plugins" property="og:title" /><meta content="https://github.com/getpelican/pelican-plugins" property="og:url" /><meta content="pelican-plugins - Collection of plugins for the Pelican static site generator" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/NTg0MjY2Njo1NmJlYmI4OGNlYjNjOThjMTkyYTgzNTk1ZDUwZTgyZTo4NDhjZTMwYzU1OWRmMzRmNDcwYWYyZDY5NWE2NzkxNjM0ZTcwOTY4MDBlZWQ0MzBlMGE3MjQ1YTM3ZmJkNDJl--7842b990f698dd62c0fc9e729c4cfa4ddc4cd850">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="3D962B79:2DEC:6EB256:5525F690" name="octolytics-dimension-request_id" /><meta content="5842666" name="octolytics-actor-id" /><meta content="lcy-hugepanda" name="octolytics-actor-login" /><meta content="dc01ef1805f2383f29dcb0fe2cc31fe80e147db0137a98bbb757830cbecc5553" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged In">
    <meta class="js-ga-set" name="dimension2" content="Header v3">
    <meta name="is-dotcom" content="true">
    <meta name="hostname" content="github.com">
    <meta name="user-login" content="lcy-hugepanda">

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="LHzgx9ZuvtPjmgy8FAAtYMebKoa5mtsahVJpXMEhjdVJ0Gwhd/rnEAC0zyukW/ac8ATL8+lqKddQ/+S1MDV7VQ==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-c27ba1dfa67445324bab49f8e0c263d3fd50fd4cb5797bbb03011d74bf7e8608.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-5b5e999e041f2586f9dc06b940229076225e6ec5ab5406be292a87331325fdc0.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="789bdb6a3ae10922d200debfa735ab1c">

      
  <meta name="description" content="pelican-plugins - Collection of plugins for the Pelican static site generator">
  <meta name="go-import" content="github.com/getpelican/pelican-plugins git https://github.com/getpelican/pelican-plugins.git">

  <meta content="2043492" name="octolytics-dimension-user_id" /><meta content="getpelican" name="octolytics-dimension-user_login" /><meta content="6547965" name="octolytics-dimension-repository_id" /><meta content="getpelican/pelican-plugins" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="6547965" name="octolytics-dimension-repository_network_root_id" /><meta content="getpelican/pelican-plugins" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/getpelican/pelican-plugins/commits/master.atom" rel="alternate" title="Recent Commits to pelican-plugins:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      


        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/getpelican/pelican-plugins/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/getpelican/pelican-plugins/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
          <li class="header-nav-item explore">
            <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
          </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
            </li>
            <li class="header-nav-item">
              <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
            </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
          </li>
      </ul>

      
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/lcy-hugepanda" data-ga-click="Header, go to profile, text:username">
      <img alt="@lcy-hugepanda" class="avatar" data-user="5842666" height="20" src="https://avatars2.githubusercontent.com/u/5842666?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">lcy-hugepanda</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu">
        
<li>
  <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
</li>
<li>
  <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
</li>


  <li class="dropdown-divider"></li>
  <li class="dropdown-header">
    <span title="getpelican/pelican-plugins">This repository</span>
  </li>
    <li>
      <a href="/getpelican/pelican-plugins/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
    </li>

      </ul>
    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
        <span class="mail-status unread"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="OtYXT8SAKRFGjD6n+hpuF9WUFaJ4E08e+7SLdaRY4vIYQgJ215mAf/7TogmKBp35u8n2eA5SnXuLGpolixPWQQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>



    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="myuNeEpT4fETYu8Lxe7p7P8c91RJbnjI9qXQr+v8xRV4CVAq8vmtZjFDDepQpdj8zXklKgW/kDqjOUzzoCRY1Q==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="6547965" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/getpelican/pelican-plugins/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Watch
          </span>
        </a>
        <a class="social-count js-social-count" href="/getpelican/pelican-plugins/watchers">
          44
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/getpelican/pelican-plugins/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fBiY8+GH4XthJOdpRuWdzHKXzY/0OA7PNqzvP1b6H1c3/lKj2X3mpShkVHrM1NQ3tHmcHZjrN3kkzXdBeLVsdg==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar getpelican/pelican-plugins"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/getpelican/pelican-plugins/stargazers">
          431
        </a>
</form>
    <form accept-charset="UTF-8" action="/getpelican/pelican-plugins/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="S7g/uxH9TTil5yZI6aCFbMSkFGv8Kp8zlmq9O0xmLNs2qDs3ir8vmQW3j8NN1hYtyqvM0ppdOGhkI4qrMiJzwQ==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star getpelican/pelican-plugins"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/getpelican/pelican-plugins/stargazers">
          431
        </a>
</form>  </div>

  </li>

        <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of getpelican/pelican-plugins to your account"
              aria-label="Fork your own copy of getpelican/pelican-plugins to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/getpelican/pelican-plugins/network" class="social-count">391</a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/getpelican/pelican-plugins/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-128-338974454bb5c32803e82f601beb051d373744b024fe8742a76009700fd7e033.gif" width="64" />
            </include-fragment>
          </div>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/getpelican" class="url fn" itemprop="url" rel="author"><span itemprop="title">getpelican</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/getpelican/pelican-plugins" class="js-current-repository" data-pjax="#js-repo-pjax-container">pelican-plugins</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/getpelican/pelican-plugins/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/getpelican/pelican-plugins" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /getpelican/pelican-plugins">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/getpelican/pelican-plugins/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /getpelican/pelican-plugins/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/getpelican/pelican-plugins/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /getpelican/pelican-plugins/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/getpelican/pelican-plugins/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /getpelican/pelican-plugins/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/getpelican/pelican-plugins/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /getpelican/pelican-plugins/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/getpelican/pelican-plugins.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" data-copy-hint="Copy to clipboard" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:getpelican/pelican-plugins.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" data-copy-hint="Copy to clipboard" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/getpelican/pelican-plugins" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" data-copy-hint="Copy to clipboard" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/getpelican/pelican-plugins" class="btn btn-sm sidebar-button" title="Save getpelican/pelican-plugins to your computer and use it in GitHub Desktop." aria-label="Save getpelican/pelican-plugins to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/getpelican/pelican-plugins/archive/master.zip"
                   class="btn btn-sm sidebar-button"
                   aria-label="Download the contents of getpelican/pelican-plugins as a zip file"
                   title="Download the contents of getpelican/pelican-plugins as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/getpelican/pelican-plugins/blob/4421bfd40625734f45b451411f43769b6aa9ce60/sitemap/sitemap.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:6d65201804faeb6a1e3e716e3c08fcae -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/getpelican/pelican-plugins/blob/master/sitemap/sitemap.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/getpelican/pelican-plugins/blob/touch/sitemap/sitemap.py"
               data-name="touch"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="touch">
                touch
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="btn-group right">
    <a href="/getpelican/pelican-plugins/find/master"
          class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" data-copy-hint="Copy file path to clipboard" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/getpelican/pelican-plugins" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">pelican-plugins</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/getpelican/pelican-plugins/tree/master/sitemap" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">sitemap</span></a></span><span class="separator">/</span><strong class="final-path">sitemap.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@kernc" class="avatar" data-user="684364" height="24" src="https://avatars1.githubusercontent.com/u/684364?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/kernc" rel="contributor">kernc</a></span>
        <time datetime="2014-12-24T16:37:17Z" is="relative-time">Dec 24, 2014</time>
        <div class="commit-title">
            <a href="/getpelican/pelican-plugins/commit/c0a882b5ac140914eab3a023684e67d42c41cfc2" class="message" data-pjax="true" title="Fix /index.html as / in generated sitemap">Fix /index.html as / in generated sitemap</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>10</strong>
           contributors
        </a>
      </p>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="talha131" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=talha131"><img alt="@talha131" class="avatar" data-user="1094724" height="20" src="https://avatars0.githubusercontent.com/u/1094724?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="barraudf" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=barraudf"><img alt="@barraudf" class="avatar" data-user="7677569" height="20" src="https://avatars1.githubusercontent.com/u/7677569?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="avaris" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=avaris"><img alt="@avaris" class="avatar" data-user="1186345" height="20" src="https://avatars3.githubusercontent.com/u/1186345?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="kernc" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=kernc"><img alt="@kernc" class="avatar" data-user="684364" height="20" src="https://avatars3.githubusercontent.com/u/684364?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="zhangliyong" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=zhangliyong"><img alt="@zhangliyong" class="avatar" data-user="448010" height="20" src="https://avatars1.githubusercontent.com/u/448010?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sukharevd" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=sukharevd"><img alt="@sukharevd" class="avatar" data-user="845064" height="20" src="https://avatars2.githubusercontent.com/u/845064?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="Keats" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=Keats"><img alt="@Keats" class="avatar" data-user="680355" height="20" src="https://avatars2.githubusercontent.com/u/680355?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="arthur-alves" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=arthur-alves"><img alt="@arthur-alves" class="avatar" data-user="4562996" height="20" src="https://avatars1.githubusercontent.com/u/4562996?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="andyli" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=andyli"><img alt="@andyli" class="avatar" data-user="103977" height="20" src="https://avatars1.githubusercontent.com/u/103977?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="adworacz" href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py?author=adworacz"><img alt="@adworacz" class="avatar" data-user="561689" height="20" src="https://avatars3.githubusercontent.com/u/561689?v=3&amp;s=40" width="20" /> </a>


    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@talha131" data-user="1094724" height="24" src="https://avatars2.githubusercontent.com/u/1094724?v=3&amp;s=48" width="24" />
            <a href="/talha131">talha131</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@barraudf" data-user="7677569" height="24" src="https://avatars3.githubusercontent.com/u/7677569?v=3&amp;s=48" width="24" />
            <a href="/barraudf">barraudf</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@avaris" data-user="1186345" height="24" src="https://avatars1.githubusercontent.com/u/1186345?v=3&amp;s=48" width="24" />
            <a href="/avaris">avaris</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@kernc" data-user="684364" height="24" src="https://avatars1.githubusercontent.com/u/684364?v=3&amp;s=48" width="24" />
            <a href="/kernc">kernc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@zhangliyong" data-user="448010" height="24" src="https://avatars3.githubusercontent.com/u/448010?v=3&amp;s=48" width="24" />
            <a href="/zhangliyong">zhangliyong</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@sukharevd" data-user="845064" height="24" src="https://avatars0.githubusercontent.com/u/845064?v=3&amp;s=48" width="24" />
            <a href="/sukharevd">sukharevd</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@Keats" data-user="680355" height="24" src="https://avatars0.githubusercontent.com/u/680355?v=3&amp;s=48" width="24" />
            <a href="/Keats">Keats</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@arthur-alves" data-user="4562996" height="24" src="https://avatars3.githubusercontent.com/u/4562996?v=3&amp;s=48" width="24" />
            <a href="/arthur-alves">arthur-alves</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@andyli" data-user="103977" height="24" src="https://avatars3.githubusercontent.com/u/103977?v=3&amp;s=48" width="24" />
            <a href="/andyli">andyli</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@adworacz" data-user="561689" height="24" src="https://avatars1.githubusercontent.com/u/561689?v=3&amp;s=48" width="24" />
            <a href="/adworacz">adworacz</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/getpelican/pelican-plugins/raw/master/sitemap/sitemap.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/getpelican/pelican-plugins/blame/master/sitemap/sitemap.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/getpelican/pelican-plugins/commits/master/sitemap/sitemap.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/getpelican/pelican-plugins?branch=master&amp;filepath=sitemap%2Fsitemap.py"
           aria-label="Open this file in GitHub for Windows">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <form accept-charset="UTF-8" action="/getpelican/pelican-plugins/edit/master/sitemap/sitemap.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="ThT6bYCbMgLcmX68F8b564ia/MBURF5Xw7MkjAC3qeoPHTU3J6SkNfbtNwvYGH101yTBqAMHrYdsJusQpQjaPA==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Clicking this button will fork this project so you can edit the file" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <form accept-charset="UTF-8" action="/getpelican/pelican-plugins/delete/master/sitemap/sitemap.py" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="X1dNC7TzHrn+BzTDM6D9HHv87T5oJi5szIm7Ck9zUJtFED2bXTgkZImS4w0x+uDQLe3zTJtbEwSkatZHXsbUkg==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Fork this project and delete file" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        244 lines (193 sloc)
        <span class="file-info-divider"></span>
      8.417 kb
    </div>
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c"># -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-s">Sitemap</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-s">-------</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line"><span class="pl-s">The sitemap plugin generates plain-text or XML sitemaps.</span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-k">from</span> __future__ <span class="pl-k">import</span> unicode_literals</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line"><span class="pl-k">import</span> collections</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line"><span class="pl-k">import</span> os.path</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line"><span class="pl-k">from</span> datetime <span class="pl-k">import</span> datetime</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line"><span class="pl-k">from</span> logging <span class="pl-k">import</span> warning, info</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line"><span class="pl-k">from</span> codecs <span class="pl-k">import</span> <span class="pl-c1">open</span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line"><span class="pl-k">from</span> pytz <span class="pl-k">import</span> timezone</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line"><span class="pl-k">from</span> pelican <span class="pl-k">import</span> signals, contents</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line"><span class="pl-k">from</span> pelican.utils <span class="pl-k">import</span> get_date</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">TXT_HEADER <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span><span class="pl-c1">{0}</span>/index.html</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line"><span class="pl-s"><span class="pl-c1">{0}</span>/archives.html</span></td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line"><span class="pl-s"><span class="pl-c1">{0}</span>/tags.html</span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line"><span class="pl-s"><span class="pl-c1">{0}</span>/categories.html</span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line">XML_HEADER <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line"><span class="pl-s">&lt;urlset xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line"><span class="pl-s">xsi:schemaLocation=&quot;http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd&quot;</span></td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line"><span class="pl-s">xmlns=&quot;http://www.sitemaps.org/schemas/sitemap/0.9&quot;&gt;</span></td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">XML_URL <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line"><span class="pl-s">&lt;url&gt;</span></td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line"><span class="pl-s">&lt;loc&gt;<span class="pl-c1">{0}</span>/<span class="pl-c1">{1}</span>&lt;/loc&gt;</span></td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line"><span class="pl-s">&lt;lastmod&gt;<span class="pl-c1">{2}</span>&lt;/lastmod&gt;</span></td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line"><span class="pl-s">&lt;changefreq&gt;<span class="pl-c1">{3}</span>&lt;/changefreq&gt;</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line"><span class="pl-s">&lt;priority&gt;<span class="pl-c1">{4}</span>&lt;/priority&gt;</span></td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line"><span class="pl-s">&lt;/url&gt;</span></td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line">XML_FOOTER <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line"><span class="pl-s">&lt;/urlset&gt;</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">format_date</span>(<span class="pl-smi">date</span>):</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">    <span class="pl-k">if</span> date.tzinfo:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">        tz <span class="pl-k">=</span> date.strftime(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%z</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">        tz <span class="pl-k">=</span> tz[:<span class="pl-k">-</span><span class="pl-c1">2</span>] <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>:<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> tz[<span class="pl-k">-</span><span class="pl-c1">2</span>:]</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line">        tz <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>-00:00<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line">    <span class="pl-k">return</span> date.strftime(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%Y</span>-<span class="pl-c1">%m</span>-<span class="pl-c1">%d</span>T<span class="pl-c1">%H</span>:<span class="pl-c1">%M</span>:<span class="pl-c1">%S</span><span class="pl-pds">&quot;</span></span>) <span class="pl-k">+</span> tz</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line"><span class="pl-k">class</span> <span class="pl-en">SitemapGenerator</span>(<span class="pl-e"><span class="pl-c1">object</span></span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">    <span class="pl-k">def</span> <span class="pl-en"><span class="pl-c1">__init__</span></span>(<span class="pl-smi">self</span>, <span class="pl-smi">context</span>, <span class="pl-smi">settings</span>, <span class="pl-smi">path</span>, <span class="pl-smi">theme</span>, <span class="pl-smi">output_path</span>, *<span class="pl-smi">null</span>):</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">        <span class="pl-v">self</span>.output_path <span class="pl-k">=</span> output_path</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">        <span class="pl-v">self</span>.context <span class="pl-k">=</span> context</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">        <span class="pl-v">self</span>.now <span class="pl-k">=</span> datetime.now()</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">        <span class="pl-v">self</span>.siteurl <span class="pl-k">=</span> settings.get(<span class="pl-s"><span class="pl-pds">&#39;</span>SITEURL<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line">        <span class="pl-v">self</span>.default_timezone <span class="pl-k">=</span> settings.get(<span class="pl-s"><span class="pl-pds">&#39;</span>TIMEZONE<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>UTC<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">        <span class="pl-v">self</span>.timezone <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(<span class="pl-v">self</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>timezone<span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.default_timezone)</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">        <span class="pl-v">self</span>.timezone <span class="pl-k">=</span> timezone(<span class="pl-v">self</span>.timezone)</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line">        <span class="pl-v">self</span>.format <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>xml<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">        <span class="pl-v">self</span>.changefreqs <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>monthly<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>indexes<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>daily<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>pages<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>monthly<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line">        <span class="pl-v">self</span>.priorities <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0.5</span>,</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>indexes<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0.5</span>,</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>pages<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">0.5</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">        config <span class="pl-k">=</span> settings.get(<span class="pl-s"><span class="pl-pds">&#39;</span>SITEMAP<span class="pl-pds">&#39;</span></span>, {})</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(config, <span class="pl-c1">dict</span>):</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line">            warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: the SITEMAP setting must be a dict<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line">            fmt <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>format<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line">            pris <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>priorities<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line">            chfreqs <span class="pl-k">=</span> config.get(<span class="pl-s"><span class="pl-pds">&#39;</span>changefreqs<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line">            <span class="pl-k">if</span> fmt <span class="pl-k">not</span> <span class="pl-k">in</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>xml<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>txt<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line">                warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: SITEMAP[&#39;format&#39;] must be `txt&#39; or `xml&#39;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line">                warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: Setting SITEMAP[&#39;format&#39;] on `xml&#39;<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line">            <span class="pl-k">elif</span> fmt <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>txt<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line">                <span class="pl-v">self</span>.format <span class="pl-k">=</span> fmt</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line">            valid_keys <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>indexes<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>pages<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line">            valid_chfreqs <span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>always<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>hourly<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>daily<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>weekly<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>monthly<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>yearly<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>never<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(pris, <span class="pl-c1">dict</span>):</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line">                <span class="pl-c"># We use items for Py3k compat. .iteritems() otherwise</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line">                <span class="pl-k">for</span> k, v <span class="pl-k">in</span> pris.items():</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line">                    <span class="pl-k">if</span> k <span class="pl-k">in</span> valid_keys <span class="pl-k">and</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(v, (<span class="pl-c1">int</span>, <span class="pl-c1">float</span>)):</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line">                        default <span class="pl-k">=</span> <span class="pl-v">self</span>.priorities[k]</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line">                        warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: priorities must be numbers<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line">                        warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: setting SITEMAP[&#39;priorities&#39;]<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">                                <span class="pl-s"><span class="pl-pds">&quot;</span>[&#39;<span class="pl-c1">{0}</span>&#39;] on <span class="pl-c1">{1}</span><span class="pl-pds">&quot;</span></span>.format(k, default))</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line">                        pris[k] <span class="pl-k">=</span> default</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line">                <span class="pl-v">self</span>.priorities.update(pris)</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">            <span class="pl-k">elif</span> pris <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">                warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: SITEMAP[&#39;priorities&#39;] must be a dict<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">                warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: using the default values<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(chfreqs, <span class="pl-c1">dict</span>):</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line">                <span class="pl-c"># .items() for py3k compat.</span></td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line">                <span class="pl-k">for</span> k, v <span class="pl-k">in</span> chfreqs.items():</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line">                    <span class="pl-k">if</span> k <span class="pl-k">in</span> valid_keys <span class="pl-k">and</span> v <span class="pl-k">not</span> <span class="pl-k">in</span> valid_chfreqs:</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line">                        default <span class="pl-k">=</span> <span class="pl-v">self</span>.changefreqs[k]</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line">                        warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: invalid changefreq `<span class="pl-c1">{0}</span>&#39;<span class="pl-pds">&quot;</span></span>.format(v))</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">                        warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: setting SITEMAP[&#39;changefreqs&#39;]<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line">                                <span class="pl-s"><span class="pl-pds">&quot;</span>[&#39;<span class="pl-c1">{0}</span>&#39;] on &#39;<span class="pl-c1">{1}</span>&#39;<span class="pl-pds">&quot;</span></span>.format(k, default))</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">                        chfreqs[k] <span class="pl-k">=</span> default</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">                <span class="pl-v">self</span>.changefreqs.update(chfreqs)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line">            <span class="pl-k">elif</span> chfreqs <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line">                warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: SITEMAP[&#39;changefreqs&#39;] must be a dict<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line">                warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: using the default values<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">    <span class="pl-k">def</span> <span class="pl-en">write_url</span>(<span class="pl-smi">self</span>, <span class="pl-smi">page</span>, <span class="pl-smi">fd</span>):</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">getattr</span>(page, <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>published<span class="pl-pds">&#39;</span></span>) <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>published<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">        <span class="pl-c"># We can disable categories/authors/etc by using False instead of &#39;&#39;</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> page.save_as:</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">        page_path <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.output_path, page.save_as)</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(page_path):</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line">        lastdate <span class="pl-k">=</span> <span class="pl-c1">getattr</span>(page, <span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>, <span class="pl-v">self</span>.now)</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line">            lastdate <span class="pl-k">=</span> <span class="pl-v">self</span>.get_date_modified(page, lastdate)</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line">            warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> page.save_as <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> has invalid modification date,<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code js-file-line">            warning(<span class="pl-s"><span class="pl-pds">&quot;</span>sitemap plugin: using date value as lastmod.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code js-file-line">        lastmod <span class="pl-k">=</span> format_date(lastdate)</td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(page, contents.Article):</td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code js-file-line">            pri <span class="pl-k">=</span> <span class="pl-v">self</span>.priorities[<span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code js-file-line">            chfreq <span class="pl-k">=</span> <span class="pl-v">self</span>.changefreqs[<span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code js-file-line">        <span class="pl-k">elif</span> <span class="pl-c1">isinstance</span>(page, contents.Page):</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code js-file-line">            pri <span class="pl-k">=</span> <span class="pl-v">self</span>.priorities[<span class="pl-s"><span class="pl-pds">&#39;</span>pages<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code js-file-line">            chfreq <span class="pl-k">=</span> <span class="pl-v">self</span>.changefreqs[<span class="pl-s"><span class="pl-pds">&#39;</span>pages<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code js-file-line">            pri <span class="pl-k">=</span> <span class="pl-v">self</span>.priorities[<span class="pl-s"><span class="pl-pds">&#39;</span>indexes<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code js-file-line">            chfreq <span class="pl-k">=</span> <span class="pl-v">self</span>.changefreqs[<span class="pl-s"><span class="pl-pds">&#39;</span>indexes<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code js-file-line">        pageurl <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> page.url <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>index.html<span class="pl-pds">&#39;</span></span> <span class="pl-k">else</span> page.url</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-v">self</span>.format <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>xml<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code js-file-line">            fd.write(XML_URL.format(<span class="pl-v">self</span>.siteurl, pageurl, lastmod, chfreq, pri))</td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code js-file-line">            fd.write(<span class="pl-v">self</span>.siteurl <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> pageurl <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_date_modified</span>(<span class="pl-smi">self</span>, <span class="pl-smi">page</span>, <span class="pl-smi">default</span>):</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">hasattr</span>(page, <span class="pl-s"><span class="pl-pds">&#39;</span>modified<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(page.modified, datetime):</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code js-file-line">                <span class="pl-k">return</span> page.modified</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code js-file-line">            <span class="pl-k">return</span> get_date(page.modified)</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code js-file-line">            <span class="pl-k">return</span> default</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code js-file-line">    <span class="pl-k">def</span> <span class="pl-en">set_url_wrappers_modification_date</span>(<span class="pl-smi">self</span>, <span class="pl-smi">wrappers</span>):</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code js-file-line">        <span class="pl-k">for</span> (wrapper, articles) <span class="pl-k">in</span> wrappers:</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code js-file-line">            lastmod <span class="pl-k">=</span> datetime.min.replace(<span class="pl-smi">tzinfo</span><span class="pl-k">=</span><span class="pl-v">self</span>.timezone)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code js-file-line">            <span class="pl-k">for</span> article <span class="pl-k">in</span> articles:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code js-file-line">                lastmod <span class="pl-k">=</span> <span class="pl-c1">max</span>(lastmod, article.date.replace(<span class="pl-smi">tzinfo</span><span class="pl-k">=</span><span class="pl-v">self</span>.timezone))</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code js-file-line">                    modified <span class="pl-k">=</span> <span class="pl-v">self</span>.get_date_modified(article, datetime.min).replace(<span class="pl-smi">tzinfo</span><span class="pl-k">=</span><span class="pl-v">self</span>.timezone)</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code js-file-line">                    lastmod <span class="pl-k">=</span> <span class="pl-c1">max</span>(lastmod, modified)</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code js-file-line">                    <span class="pl-c"># Supressed: user will be notified.</span></td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code js-file-line">                    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code js-file-line">            <span class="pl-c1">setattr</span>(wrapper, <span class="pl-s"><span class="pl-pds">&#39;</span>modified<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">str</span>(lastmod))</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code js-file-line">    <span class="pl-k">def</span> <span class="pl-en">generate_output</span>(<span class="pl-smi">self</span>, <span class="pl-smi">writer</span>):</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code js-file-line">        path <span class="pl-k">=</span> os.path.join(<span class="pl-v">self</span>.output_path, <span class="pl-s"><span class="pl-pds">&#39;</span>sitemap.<span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(<span class="pl-v">self</span>.format))</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code js-file-line">        pages <span class="pl-k">=</span> <span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>pages<span class="pl-pds">&#39;</span></span>] <span class="pl-k">+</span> <span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>] \</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code js-file-line">                <span class="pl-k">+</span> [ c <span class="pl-k">for</span> (c, a) <span class="pl-k">in</span> <span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>categories<span class="pl-pds">&#39;</span></span>]] \</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code js-file-line">                <span class="pl-k">+</span> [ t <span class="pl-k">for</span> (t, a) <span class="pl-k">in</span> <span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>tags<span class="pl-pds">&#39;</span></span>]] \</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code js-file-line">                <span class="pl-k">+</span> [ a <span class="pl-k">for</span> (a, b) <span class="pl-k">in</span> <span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>authors<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code js-file-line">        <span class="pl-v">self</span>.set_url_wrappers_modification_date(<span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>categories<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code js-file-line">        <span class="pl-v">self</span>.set_url_wrappers_modification_date(<span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>tags<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code js-file-line">        <span class="pl-v">self</span>.set_url_wrappers_modification_date(<span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>authors<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code js-file-line">        <span class="pl-k">for</span> article <span class="pl-k">in</span> <span class="pl-v">self</span>.context[<span class="pl-s"><span class="pl-pds">&#39;</span>articles<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code js-file-line">            pages <span class="pl-k">+=</span> article.translations</td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code js-file-line">        info(<span class="pl-s"><span class="pl-pds">&#39;</span>writing <span class="pl-c1">{0}</span><span class="pl-pds">&#39;</span></span>.format(path))</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code js-file-line">        <span class="pl-k">with</span> <span class="pl-c1">open</span>(path, <span class="pl-s"><span class="pl-pds">&#39;</span>w<span class="pl-pds">&#39;</span></span>, <span class="pl-smi">encoding</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>utf-8<span class="pl-pds">&#39;</span></span>) <span class="pl-k">as</span> fd:</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.format <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>xml<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code js-file-line">                fd.write(XML_HEADER)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code js-file-line">                fd.write(TXT_HEADER.format(<span class="pl-v">self</span>.siteurl))</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code js-file-line">            FakePage <span class="pl-k">=</span> collections.namedtuple(<span class="pl-s"><span class="pl-pds">&#39;</span>FakePage<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code js-file-line">                                              [<span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code js-file-line">                                               <span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code js-file-line">                                               <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code js-file-line">                                               <span class="pl-s"><span class="pl-pds">&#39;</span>save_as<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code js-file-line">            <span class="pl-k">for</span> standard_page_url <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>index.html<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code js-file-line">                                      <span class="pl-s"><span class="pl-pds">&#39;</span>archives.html<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code js-file-line">                                      <span class="pl-s"><span class="pl-pds">&#39;</span>tags.html<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code js-file-line">                                      <span class="pl-s"><span class="pl-pds">&#39;</span>categories.html<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code js-file-line">                fake <span class="pl-k">=</span> FakePage(<span class="pl-smi">status</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>published<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code js-file-line">                                <span class="pl-smi">date</span><span class="pl-k">=</span><span class="pl-v">self</span>.now,</td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code js-file-line">                                <span class="pl-smi">url</span><span class="pl-k">=</span>standard_page_url,</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code js-file-line">                                <span class="pl-smi">save_as</span><span class="pl-k">=</span>standard_page_url)</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code js-file-line">                <span class="pl-v">self</span>.write_url(fake, fd)</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code js-file-line">            <span class="pl-k">for</span> page <span class="pl-k">in</span> pages:</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code js-file-line">                <span class="pl-v">self</span>.write_url(page, fd)</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code js-file-line">            <span class="pl-k">if</span> <span class="pl-v">self</span>.format <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>xml<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code js-file-line">                fd.write(XML_FOOTER)</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">get_generators</span>(<span class="pl-smi">generators</span>):</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code js-file-line">    <span class="pl-k">return</span> SitemapGenerator</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code js-file-line"><span class="pl-k">def</span> <span class="pl-en">register</span>():</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code js-file-line">    signals.get_generators.connect(get_generators)</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.05737s from github-fe129-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-2c8ae50712a47d2b83d740cb875d55cdbbb3fdbccf303951cc6b7e63731e0c38.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-47790cee6fddf7135caf6ed39b4fcc1aa7dd81dd9ef8935a0bda0da52615af41.js"></script>
      
      

  </body>
</html>

