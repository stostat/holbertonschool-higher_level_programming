
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="Holberton School">
    <meta name="google" content="notranslate" />
    
    <link rel="stylesheet" href="https://use.typekit.net/xgz4ilr.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    
    <title>Holberton Intranet</title>

    <link rel="stylesheet" media="all" href="/assets/application-fc4cc0e4df85c1674b4703388fc7dab2b3c15ef4f8a64ac0e3a44d4e249ebf64.css" />
    <script src="https://www.gstatic.com/charts/loader.js"></script>
	  <script src="/assets/application-79fdee72b4991b4ae2fb0fc9253f684192d271c7e31b2c64fe36359ee2726cc7.js"></script>
	  <link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-80dd4e2b2b534776f1430ecc265116b6135be1872b6a06edb53a0fa80e97a308.ico" />
	  <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="GkG8mPpfxAiQ9+yjiNckOBAj3CMh7Cc4DOfTI5Yulrlykt4pQjlDLLHKgtwoyh+9y2+RlJIg2Vh5nCawnzirIQ==" />

    <link rel="apple-touch-icon" href="/apple-touch-icon.png" />

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Video player -->
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/clappr@latest/dist/clappr.min.js"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/gh/ewwink/clappr-quality-selector-plugin@latest/quality-selector.js"></script>

    <!-- Store user timezone -->
    <script>
      Cookies.set('timezone', (new Date()).getTimezoneOffset() / -60.0);
    </script>

    <script src="/packs/js/application-f0e59c44581136cb2218.js"></script>
  </head>

  <body class="
     
    env_production
    
    " 
    translate="no" 
    class="notranslate"
    data-theme-suffix=""
    data-checker-special-theme="">


    <main>


      <div id="layout-bars">
        

        

        

        
      </div>
      

      <article class="">
        <div class="logged_out_form">

  <h2 class="hbtn_logo">
  </h2>

  <form class="sm-gap" id="new_user" action="/auth/sign_in" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="g64feRlyFn6DcfbKI23aBhJz89z4+ieOJ7tE24OCT03rfX3IoRSRWqJMmLWDcOGDyT++a0s22e5SwLFIipRy1Q==" />

  
    <div class="field">
      <label class="control-label" for="user_login">Email</label><br />
      <input autofocus="autofocus" class="form-control" type="text" name="user[login]" id="user_login" />
    </div>

    <div class="field">
      <label class="control-label" for="user_password">Password</label><br />
      <input autocomplete="off" class="form-control" type="password" name="user[password]" id="user_password" />
    </div>

      <div class="field">
        <input name="user[remember_me]" type="hidden" value="0" /><input type="checkbox" value="1" name="user[remember_me]" id="user_remember_me" />
        <label class="control-label" for="user_remember_me">Remember me</label>
      </div>

    <div class="actions">
      <input type="submit" name="commit" value="Log in" class="btn btn-primary" />
    </div>
</form>
  <ul id="devise_links" class="gap">



		<li>
			<a href="/auth/password/new">Forgot your password?</a>
		</li>


		<li>
			<!--<a href="/auth/unlock/new">Didn&#39;t receive unlock instructions?</a>-->
		</li>


	<!--
	<li>
		<a href="https://aka.ms/ssprsetup">Forgot your password?</a>
	</li>
	-->
</ul>

</div>
      </article>
      
      <div class="copyright">Copyright &copy; 2020 Holberton School. All rights reserved.</div>
    </main>



    
      <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create', 
            'UA-67152800-6', 
            'auto');

        ga('send', 'pageview');

        $(document).ready(function() { 
          ga(function(tracker) { 
            var clientId = tracker.get('clientId'); 
            $('.ga-client-id').val(clientId); 
          }); 
        });
      </script>



      <input id="checker_pride_assets" type="hidden" value="[]" />
  </body>
</html>
