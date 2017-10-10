<h1 class="gap">0x09. Web server</h1>


<h4 class="task">
    0. Transfer a file to your server
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a Bash script that transfers a file from our client to a server:</p><p>Requirements:</p><ul>
<li>Accepts 4 parameters

<ol>
<li>The path to the file to be transferred</li>
<li>The IP of the server we want to transfer the file to</li>
<li>The username <code>scp</code> connects with</li>
<li>The path to the SSH private key that <code>scp</code> uses</li>
</ol></li>
<li>Display <code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 3 parameters passed</li>
<li><code>scp</code> must transfer the file to the user home directory <code>~/</code></li>
<li>Strict host key checking must be disabled when using <code>scp</code> </li>
</ul><p>Example:</p>


<h4 class="task">
    1. Install nginx web server
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Readme:</p><ul>
<li><a href="/rltoken/Tcbz_WMUUcFSZd0TjxHRLA" sm-gap" title='&lt;code&gt;-y&lt;/code&gt; on &lt;code&gt;apt-get&lt;/code&gt; command" target=“_blank”&gt;&lt;code&gt;-y&lt;/code&gt; on &lt;code&gt;apt-get&lt;/code&gt; command&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;

&lt;p&gt;Web servers are the piece of software generating and serving HTML pages, let’s install one!&lt;/p&gt;

&lt;p&gt;Requirements:&lt;/p&gt;

&lt;ul&gt;
&lt;li&gt;Install &lt;code&gt;nginx&lt;/code&gt; on your &lt;code&gt;web-01&lt;/code&gt; server&lt;/li&gt;
&lt;li&gt;Nginx should be listening on port 80&lt;/li&gt;
&lt;li&gt;When querying Nginx at its root &lt;code&gt;/&lt;/code&gt; with a GET request (requesting a page)  using &lt;code&gt;curl&lt;/code&gt;, it must return a page that contains the string &lt;code&gt;Holberton School&lt;/code&gt;&lt;/li&gt;
&lt;li&gt;As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements&lt;/li&gt;
&lt;/ul&gt;

&lt;p&gt;Example:&lt;/p&gt;

&lt;pre&gt;&lt;code&gt;sylvain@ubuntu$ curl 34.198.248.145/
Holberton School for the win!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
&lt;/code&gt;&lt;/pre&gt;

&lt;p&gt;In this example &lt;code&gt;34.198.248.145&lt;/code&gt; is the IP of my &lt;code&gt;web-01&lt;/code&gt; server. If you want to query the Nginx that is locally installed on your server, you can use &lt;code&gt;curl 127.0.0.1&lt;/code&gt;.&lt;/p&gt;


  &lt;!-- Task URLs --&gt;

  &lt;!-- Github information --&gt;
    &lt;p class='><strong>Repo:</strong>
<ul>
<li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
<li>Directory: <code>0x09-web_server</code></li>
<li>File: <code>1-install_nginx_web_server</code></li>
</ul>
<div class="student_correction_requests">
<!-- Button test code -->
<!-- Button containers -->
<button class="task_containers_modal btn btn-default " data-container-spec-ids="[1]" data-target="#task-containers-1400-modal" data-task-id="1400" data-toggle="modal">
        Get a container
      </button>
<div class="modal fade task_containers_modal" data-container-spec-ids="[1]" data-task-id="1400" id="task-containers-1400-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Containers</h4>
</div>
<div class="modal-body">
<p>Each container will be available 24h max</p>
<div class="list_containers">
<table class="table table-striped">
<thead>
<tr>
<th>Name</th>
<th>SSH connection</th>
<th>IPs (Public/Private)</th>
<th>Ports mapping</th>
<th>Status</th>
<th colspan="1"></th>
</tr>
</thead>
<tbody>
<tr id="task_1400_container_spec_1">
<td>Ubuntu 14.04</td>
<td class="container_ssh"></td>
<td class="container_ips"></td>
<td class="container_ports"></td>
<td class="container_status"></td>
<td>
<input class="btn btn-primary start_container" data-container-spec-id="1" data-task-id="1400" name="commit" type="submit" value="Start"/>
<input class="btn btn-primary destroy_container" data-container-spec-id="1" data-task-id="1400" name="commit" type="submit" value="Destroy"/>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="error"></div>
<p class="gap">
<b>Private IP? Public IP?</b><br/>
            At school, you must use the <b>private IP</b>. From outside, you must use the <b>public IP</b>.<br/><br/>
<b>Ports mapping</b><br/>
            Each exposed ports are mapped to another, example: the port SSH <code>22</code> is mapped to the port <code>33511</code>.<br/><br/>
<b>SSH access</b><br/>
            To access to your container: <code>ssh root@&lt;public|private&gt; -p &lt;port mapped to 22&gt;</code><br/>
            Example: <code>ssh root@12.12.12.12 -p 33511</code>
</p>
</div>
</div><!-- /.modal-content -->
</div><!-- /.modal-dialog -->
</div>
</div>
</a></li></ul>
<h4 class="task">
    2. Setup a domain name
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p><a href="/rltoken/hKxGLx11hbaww7MDmdxTBg" target="_blank" title="Gandi">Gandi</a> is one of the top 25 domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with Gandi so that you can learn about DNS.</p><p>Gandi worked with domain name registrars to give you access to a free domain name for a year. Please use the promo code <strong>THXBETTY</strong>. Feel free to drop a thank you tweet for <a href="/rltoken/u9yMc-L0d0tLdupPnsG01A" target="_blank" title="Gandi">Gandi</a>.</p><p>Using your Gandi account, acquire a domain name at this <a href="/rltoken/hKxGLx11hbaww7MDmdxTBg" target="_blank" title="address">address</a>, using one of these extensions: </p><ul>
<li><code>.website</code></li>
<li><code>.site</code></li>
<li><code>.space</code></li>
<li><code>.online</code></li>
</ul><p>Provide the domain name in your answer file.</p><p>Requirement:</p><ul>
<li>provide the domain name only (example: <code>foobar.online</code>), no subdomain (example: <code>www.foobar.online</code>)</li>
<li>configure your DNS records with an A entry so that your root domain points to your <code>web-01</code> IP address</li>
<li>go to <a href="/rltoken/fYvJr4-HV1WPnfB7HCue_Q" target="_blank" title="your profile">your profile</a> and enter your domain in the <code>Project website url</code> field</li>
</ul><p>Example:</p>


<h4 class="task">
    3. Redirection
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Readme:</p><ul>
<li><a href="/rltoken/VxTHgC6QPUnYqY808HLAbg" sm-gap" title='Replace a line with multiple lines with &lt;code&gt;sed&lt;/code&gt;“ target=”_blank"&gt;Replace a line with multiple lines with &lt;code&gt;sed&lt;/code&gt;&lt;/a&gt;&lt;/li&gt;
&lt;/ul&gt;

&lt;p&gt;Configure your Nginx server so that &lt;code&gt;/redirect_me&lt;/code&gt; is redirecting to another page.&lt;/p&gt;

&lt;p&gt;Requirements:&lt;/p&gt;

&lt;ul&gt;
&lt;li&gt;The redirection must be a “301 Moved Permanently”&lt;/li&gt;
&lt;li&gt;You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements&lt;/li&gt;
&lt;li&gt;Using what you did with &lt;code&gt;1-install_nginx_web_server&lt;/code&gt;, write &lt;code&gt;3-redirection&lt;/code&gt; so that it configures a brand new Ubuntu machine to the requirements asked in this task&lt;/li&gt;
&lt;/ul&gt;

&lt;p&gt;Example:&lt;/p&gt;

&lt;pre&gt;&lt;code&gt;sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
&lt;/code&gt;&lt;/pre&gt;


  &lt;!-- Task URLs --&gt;

  &lt;!-- Github information --&gt;
    &lt;p class='><strong>Repo:</strong>
<ul>
<li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
<li>Directory: <code>0x09-web_server</code></li>
<li>File: <code>3-redirection</code></li>
</ul>
<div class="student_correction_requests">
<!-- Button test code -->
<!-- Button containers -->
<button class="task_containers_modal btn btn-default " data-container-spec-ids="[1]" data-target="#task-containers-1402-modal" data-task-id="1402" data-toggle="modal">
        Get a container
      </button>
<div class="modal fade task_containers_modal" data-container-spec-ids="[1]" data-task-id="1402" id="task-containers-1402-modal">
<div class="modal-dialog">
<div class="modal-content">
<div class="modal-header">
<button aria-label="Close" class="close" data-dismiss="modal" type="button"><span aria-hidden="true">×</span></button>
<h4 class="modal-title">Containers</h4>
</div>
<div class="modal-body">
<p>Each container will be available 24h max</p>
<div class="list_containers">
<table class="table table-striped">
<thead>
<tr>
<th>Name</th>
<th>SSH connection</th>
<th>IPs (Public/Private)</th>
<th>Ports mapping</th>
<th>Status</th>
<th colspan="1"></th>
</tr>
</thead>
<tbody>
<tr id="task_1402_container_spec_1">
<td>Ubuntu 14.04</td>
<td class="container_ssh"></td>
<td class="container_ips"></td>
<td class="container_ports"></td>
<td class="container_status"></td>
<td>
<input class="btn btn-primary start_container" data-container-spec-id="1" data-task-id="1402" name="commit" type="submit" value="Start"/>
<input class="btn btn-primary destroy_container" data-container-spec-id="1" data-task-id="1402" name="commit" type="submit" value="Destroy"/>
<div class="spinner">
<div class="bounce1"></div>
<div class="bounce2"></div>
<div class="bounce3"></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="error"></div>
<p class="gap">
<b>Private IP? Public IP?</b><br/>
            At school, you must use the <b>private IP</b>. From outside, you must use the <b>public IP</b>.<br/><br/>
<b>Ports mapping</b><br/>
            Each exposed ports are mapped to another, example: the port SSH <code>22</code> is mapped to the port <code>33511</code>.<br/><br/>
<b>SSH access</b><br/>
            To access to your container: <code>ssh root@&lt;public|private&gt; -p &lt;port mapped to 22&gt;</code><br/>
            Example: <code>ssh root@12.12.12.12 -p 33511</code>
</p>
</div>
</div><!-- /.modal-content -->
</div><!-- /.modal-dialog -->
</div>
</div>
</a></li></ul>
<h4 class="task">
    4. Not found page 404
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Configure your Nginx server to have a custom 404 page that contains the string <code>Ceci n'est pas une page</code>.</p><p>Requirements:</p><ul>
<li>The page must return an HTTP 404 error code</li>
<li>The page must contain the string <code>Ceci n'est pas une page</code></li>
<li>Using what you did with <code>3-redirection</code>, write <code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul><p>Example:</p>


<h4 class="task">
    5. Design a beautiful 404 page
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Some of my favorites:</p><ul>
<li><a href="/rltoken/BcOQZUPzoF6sfWd28JAOmA" target="_blank" title="Digital Ocean">Digital Ocean</a></li>
<li><a href="/rltoken/i56pau9DIG49cBUMBwEcPg" target="_blank" title="Github">Github</a></li>
<li><a href="/rltoken/cm7-ZqHoxVdLwhOc1XGwyg" target="_blank" title="Lego">Lego</a></li>
<li><a href="/rltoken/UCBPyeXYTeLDYh3Bi9NgKA" target="_blank" title="Blizzard">Blizzard</a></li>
<li><a href="/rltoken/apZ3b5W6-ms9a49_V0e8cg" target="_blank" title="StickerMule">StickerMule</a></li>
</ul><p>Get creative and impress us! </p><p><img alt="much impressed" src="https://media.giphy.com/media/zbaWHAJJ9ZuCc/giphy.gif"/></p><p>Note that if you decide to have your creative 404 page as the default one, make sure that it still contains the string <code>Ceci n'est pas une page</code> (otherwise the checker will fail your previous project).</p><p>Submit the URL of your 404 page in this <a href="/rltoken/GZRwz0a2cIlDcSHyP5wLDQ" target="_blank" title="form">form</a> and in your answer file.</p><div class="blog_post_div">
<h4> Add URLs here:</h4>
<div class="form-group row">
<div class="col-sm-11">
<input class="form-control" id="input_1407" type="text" value=""/>
</div>
<div class="col-sm-1">
<button class="add_task_url" data-task-id="1407" data-task-requesting="0" data-user-id="214" type="button">
<span aria-hidden="true" class="glyphicon glyphicon-plus"></span>
</button>
</div>
</div>
<ul class="list_1407">
</ul>
</div>


<h4 class="task">
    6. Deploy fast, deploy well
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p><strong>WARNING: Fabric is not (yet) available in Python 3.x</strong></p><p>Readme:</p><ul>
<li><a href="/rltoken/goXJBy2zA53GYpDLqCzL4w" target="_blank" title="How to use Fabric">How to use Fabric</a></li>
<li><a href="/rltoken/3t4UbsAcJTLe3K1UluZirQ" target="_blank" title="CI/CD concept page">CI/CD concept page</a></li>
</ul><p>We’ve seen in <a href="/rltoken/22QWHHCSRrIAQCHiKkAi7g" target="_blank" title="task #0">task #0</a> a very simple way to push a file from our client to a remote server. Let’s build something a bit more robust that will quickly deploy code to servers using Fabric.</p><p><img alt="f**ck it, ship it!" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/173/fitshipit.jpg"/></p><p>Your Fabric config should have 3 functions:</p><ol>
<li><code>pack</code>:

<ul>
<li>Creates a tar gzipped archive of the current directory, the name of the archive must be <code>holbertonwebapp.tar.gz</code> and be place in the local directory</li>
</ul></li>
<li><code>deploy</code>:

<ul>
<li>Uploads the archive to the remote server in the directory <code>/tmp/</code></li>
<li>Creates the directory <code>/tmp/holbertonwebapp</code></li>
<li>Untars the  <code>holbertonwebapp.tar.gz</code> archive in <code>/tmp/holbertonwebapp</code></li>
</ul></li>
<li><code>clean</code>
<ul>
<li>Deletes the <code>holbertonwebapp.tar.gz</code> on your local machine</li>
</ul></li>
</ol><p>Requirements:</p><ul>
<li>Must be done using <a href="/rltoken/bM0w4OyoKxBZUmpPg5duqQ" target="_blank" title="Fabric">Fabric</a></li>
<li>Provide your Fabric deploy code in your answer file</li>
<li>Your Fabric file should not define any host or make sure that your <code>env.hosts</code> variable is commented out</li>
<li>Your Fabric file must define the user to connect with as <code>ubuntu</code></li>
</ul><p>Example:</p>

