<h1 class="gap">Using cURL to debug</h1>


<p>
  Higher-level programming
</p>




<hr>


<div class="gap formatted-content">
    <p>cURL is a computer software project providing a library and command-line tool for transferring data using various protocols. 
It’s a command line tool for getting or sending files using URL syntax.</p>

<p>With this tool, you can request a webpage, an API or a RestAPI easily.</p>

<p>You can test on this <a href="/rltoken/OpuT5WDKqiHKt8AST8gQLA" title="simple RestAPI" target="_blank">simple RestAPI</a></p>

<p>For example: get the homepage of Google:</p>

<pre><code>i-love-curl $ curl "http://www.google.com"
&lt;!doctype html&gt;&lt;html itemscope="" itemtype="http://schema.org/WebPage" lang="en"&gt;&lt;head&gt;&lt;meta content="Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking for." name="description"&gt;&lt;meta content="noodp" name="robots"&gt;&lt;me ....
....
0,"sce":5,"stok":"dS2NgmCFVVJ61nWw37vHdkjsH_I"},"d":{}};google.y.first.push(function(){if(google.med){google.med('init');google.initHistory();google.med('history');}});if(google.j&amp;&amp;google.j.en&amp;&amp;google.j.xi){window.setTimeout(google.j.xi,0);}
&lt;/script&gt;&lt;/div&gt;&lt;/body&gt;&lt;/html&gt; i-love-curl $ 
</code></pre>

<p>Or, request a film for the RestAPI <a href="/rltoken/e75xwvvKHIMqlq1amUuYiw" title="Swapi" target="_blank">Swapi</a> (Star Wars API)</p>

<pre><code>i-love-curl $ curl https://swapi-api.hbtn.io/api/films/1/
{"title":"A New Hope","episode_id":4,"opening_crawl":"It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....","director":"George Lucas","producer":"Gary Kurtz, Rick McCallum","release_date":"1977-05-25","characters":["https://swapi-api.hbtn.io/api/people/1/","https://swapi-api.hbtn.io/api/people/2/","https://swapi-api.hbtn.io/api/people/3/","https://swapi-api.hbtn.io/api/people/4/","https://swapi-api.hbtn.io/api/people/5/","https://swapi-api.hbtn.io/api/people/6/","https://swapi-api.hbtn.io/api/people/7/","https://swapi-api.hbtn.io/api/people/8/","https://swapi-api.hbtn.io/api/people/9/","https://swapi-api.hbtn.io/api/people/10/","https://swapi-api.hbtn.io/api/people/12/","https://swapi-api.hbtn.io/api/people/13/","https://swapi-api.hbtn.io/api/people/14/","https://swapi-api.hbtn.io/api/people/15/","https://swapi-api.hbtn.io/api/people/16/","https://swapi-api.hbtn.io/api/people/18/","https://swapi-api.hbtn.io/api/people/19/","https://swapi-api.hbtn.io/api/people/81/"],"planets":["https://swapi-api.hbtn.io/api/planets/2/","https://swapi-api.hbtn.io/api/planets/3/","https://swapi-api.hbtn.io/api/planets/1/"],"starships":["https://swapi-api.hbtn.io/api/starships/2/","https://swapi-api.hbtn.io/api/starships/3/","https://swapi-api.hbtn.io/api/starships/5/","https://swapi-api.hbtn.io/api/starships/9/","https://swapi-api.hbtn.io/api/starships/10/","https://swapi-api.hbtn.io/api/starships/11/","https://swapi-api.hbtn.io/api/starships/12/","https://swapi-api.hbtn.io/api/starships/13/"],"vehicles":["https://swapi-api.hbtn.io/api/vehicles/4/","https://swapi-api.hbtn.io/api/vehicles/6/","https://swapi-api.hbtn.io/api/vehicles/7/","https://swapi-api.hbtn.io/api/vehicles/8/"],"species":["https://swapi-api.hbtn.io/api/species/5/","https://swapi-api.hbtn.io/api/species/3/","https://swapi-api.hbtn.io/api/species/2/","https://swapi-api.hbtn.io/api/species/1/","https://swapi-api.hbtn.io/api/species/4/"],"created":"2014-12-10T14:23:31.880000Z","edited":"2015-04-11T09:46:52.774897Z","url":"https://swapi-api.hbtn.io/api/films/1/"} i-love-curl $ 
</code></pre>

<h2>Some wording/vocabulary</h2>

<p>First, I really encourage you to read the Bilal post about HTTP headers <a href="/rltoken/MlSvPkGKRVEaEnkjc2fMhw" title="here" target="_blank">here</a></p>

<ul>
<li><strong>URL</strong>: “Uniform Resource Locator”, defines the web address to a specific resource. An URL is composed in 4 parts:

<ul>
<li><strong>protocol</strong>: <code>http://</code> or <code>https://</code> or <code>ftp://</code>… =&gt; defines also on which port the server will be requested</li>
<li><strong>host</strong>: <code>www.example.com</code> or <code>intranet.hbtn.io</code>… =&gt; will be resolved by the DNS = hostname to IP address</li>
<li><strong>path</strong>: <code>/index.html</code> or <code>/states/1/cities</code>… =&gt; path from the root of the website or webservice on this host</li>
<li><strong>query string</strong>: <code>?name=Jon</code> or <code>?q=dress&amp;color=FF0000</code>… =&gt; always starts by the symbol <strong>?</strong> and follow by a list of parameters (key=value) separated by the symbol <strong>&amp;</strong></li>
</ul></li>
<li><strong>request</strong>: action of client to send “data” to a specific URL and return a response</li>
<li><strong>response</strong>: result of a request return from the server to the client</li>
<li><strong>HTTP method</strong>: or called “verb” for a RestAPI. It’s part of the HTTP protocol only (http and https request):

<ul>
<li><code>GET</code>: most common method to retreive information from the server (read). When you are surfing in Google or other website, your web browser is doing GET requests to each website to reteive HTML/CSS/JS etc… to render correctly the website. Client can send some information to the server via query string.</li>
<li><code>POST</code>: use to send datas to the server (write) contain in the request body (see below)</li>
<li><code>HEAD</code>: same as GET but with an empty response. It’s mainly used to check if a resource is available but without get it.</li>
<li><code>PUT</code>/<code>PATCH</code>: to update a resource with datas contain in the request body</li>
<li><code>DELETE</code>: to remove a resource in the server (mainly used for an RestAPI) </li>
<li><a href="/rltoken/xRnHnC0KMPw2R6dDD7Edvw" title="others" target="_blank">others</a>…</li>
</ul></li>
<li><strong>Header</strong>: an header is a hash of Key-Value information. You can have <strong>request header</strong> (informations from the client to the server), but also <strong>response header</strong> (server to client). Headers are really useful and some “Keys-Values” are standardized: 

<ul>
<li><code>User-Agent</code>: from the client to the server for describing the client. Ex: Chrome used as User-Agent: “Mozilla/5.0 (Macintosh; Intel Mac OS X 10<em>11</em>6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36”</li>
<li><code>Origin</code>: from the client to the server for giving information of where come from the request to the server</li>
<li><code>Content-Type</code>: define how the body can be read. Ex: “https://swapi-api.hbtn.io/api/planets/1/” =&gt; “Content-Type: application/json” because the response body is a JSON</li>
<li><code>Content-Length</code>: size in Bytes of the request/response body</li>
<li><a href="/rltoken/8P6Suw6oQAzMB8Qiefibww" title="others" target="_blank">others</a></li>
</ul></li>
<li><strong>Body</strong>: a body is Bytes transmitted in HTTP. You can have <strong>request body</strong> (parameters from the client to the server) and <strong>response body</strong> (return result of the server to the client)</li>
<li><strong>URL encoding</strong>: action to transcode regular string to query string. It’s also used for request body in case of <code>Content-Type: application/x-www-form-urlencoded</code></li>
</ul>

<p>Some cool options:</p>

<h3>Verbose mode</h3>

<p><code>-vvv</code> will print all headers and transfer state of a request/response</p>

<h3>Output direction</h3>

<p><code>-o</code> redirect the response body of a request to a file:</p>

<pre><code>i-love-curl $ curl "http://www.google.com" -o google_homepage.html
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 11279    0 11279    0     0   145k      0 --:--:-- --:--:-- --:--:--  146k
i-love-curl $ ls
google_homepage.html
i-love-curl $
</code></pre>

<p>or to nothing:</p>

<pre><code>i-love-curl $ curl "http://www.google.com" -o /dev/null
i-love-curl $ 
</code></pre>

<h3>HTTP method</h3>

<p><code>-X</code> define which HTTP: </p>

<ul>
<li><code>-X GET</code>: to do a GET request (by default)</li>
<li><code>-X POST</code>: to do a POST request</li>
<li><code>-X PUT</code>: to do a PUT request</li>
<li><code>-X DELETE</code>: to do a DELETE request</li>
</ul>

<h3>Body / parameters</h3>

<p>All query string parameters can be directly add to the URL. But for other HTTP method, you should use the attribute <code>-d</code>.
You can use only one and it should be url encoded (separated by the symbol &amp;) or multiples. By default, the <code>Content-Type: application/x-www-form-urlencoded</code></p>

<p>Add a new state to a RestAPI:</p>

<pre><code>i-love-curl $ curl "http://localhost:5555/states" -X POST -d "name=California&amp;code=CA"
{ "id": 12, "name": "California", "code": "CA" }
i-love-curl $ 
</code></pre>

<p>or for update a state to a RestAPI:</p>

<pre><code>i-love-curl $ curl "http://localhost:5555/states/12" -X PUT -d "name=California Forever" -d "code=CAF"
{ "id": 12, "name": "California Forever", "code": "CAF" }
i-love-curl $ 
</code></pre>

<p>and if you encode the request body as JSON (by setting a correct Content-Type in the header) and your server understand it:</p>

<pre><code>i-love-curl $ curl "http://localhost:5555/states" -X POST -H "Content-Type: application/json" -d "{ \"name\": \"California\", \"code\": \"CA\" }"
{ "id": 13, "name": "California", "code": "CA" }
i-love-curl $ 
</code></pre>

<h3>Header values</h3>

<p><code>-H</code> will set your parameter in the Header part.</p>

<p>For example, to send a custom Header (by convention, it will start by <code>X-</code>):</p>

<pre><code>i-love-curl $ curl "http://localhost:5555/states" -X GET -H "X-Application-id: 14"
[{ "id": 12, "name": "California Forever", "code": "CAF" }, { "id": 13, "name": "California", "code": "CA" }]
i-love-curl $ 
</code></pre>

<p>or overwriting a standard Header (here Content-Type and User-Agent):</p>

<pre><code>i-love-curl $ curl "http://localhost:5555/states" -X GET -H "X-Application-id: 14" -H "Content-Type: text/xml" -H "User-Agent: MyCustomClient"
&lt;xml&gt;
  &lt;states&gt;
    &lt;state id="12" code="CAF"&gt;
      &lt;name&gt;California Forever&lt;/name&gt;
    &lt;/state&gt;
    &lt;state id="13" code="CA"&gt;
      &lt;name&gt;California&lt;/name&gt;
    &lt;/state&gt;
  &lt;/states&gt;
&lt;/xml&gt;
i-love-curl $ 
</code></pre>

</div>
            





<br>
<br>
      