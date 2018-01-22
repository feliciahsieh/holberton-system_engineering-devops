<h1 class="gap">0x1A. Application server #0</h1>


<h4 class="task">
    0. Welcome Gunicorn
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s serve what you built for <a href="/rltoken/QpuOAVJIVqCwq-8BAqemXQ" target="_blank" title="AirBnB clone - Web framework">AirBnB clone - Web framework</a> on <code>web01</code>.</p><p>Requirements:</p><ul>
<li>Git clone your Airbnb clone</li>
<li>Install Gunicorn and other libraries required by your application</li>
<li>Create an Upstart script that starts Gunicorn to serve <code>web_flask/0-hello_route.py</code> from your Airbnb clone</li>
<li>Setup Nginx so that the route <code>/airbnb-onepage/</code> points to Gunicorn</li>
<li>Nginx must serve this locally but also on its public IP on port <code>80</code></li>
<li>Provide the Upstart config file you wrote, upload it as answer file with the name <code>0-welcome_gunicorn-upstart_config</code></li>
<li>Provide the Nginx config file you wrote, upload it as answer file with the name <code>0-welcome_gunicorn-nginx_config</code></li>
</ul><p>Do not forget that logs are your friends, for <code>nginx</code> for instance, they are located in <code>/var/log/nginx</code>.
Also <code>init-checkconf</code> is your friend to check your <code>upstart</code> config files.</p><p>Example:</p>


<h4 class="task">
    1. Pass a query parameter
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s serve what you built for <a href="/rltoken/QpuOAVJIVqCwq-8BAqemXQ" target="_blank" title="AirBnB clone - Web framework">AirBnB clone - Web framework</a> on <code>web01</code>.</p><p>Requirements:</p><ul>
<li>Create an Upstart script that starts Gunicorn to serve <code>web_flask/6-number_odd_or_even.py</code> from your Airbnb clone</li>
<li>Setup Nginx so that the route <code>/airbnb-dynamic/</code> points to Gunicorn</li>
<li>Nginx must serve this locally but also on its public IP on port <code>80</code></li>
<li>Provide your Upstart config file, name it <code>1-pass_parameter-upstart_config</code></li>
<li>Provide your Nginx config file, name it <code>1-pass_parameter-nginx_config</code></li>
</ul><p>Example:</p>


<h4 class="task">
    2. Let's do this for your API
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s serve what you built for <a href="/rltoken/xGlaeRxMSbgYHBodxjsOhQ" target="_blank" title="AirBnB clone - RESTful API">AirBnB clone - RESTful API</a> on <code>web01</code>.</p><p>Requirements:</p><ul>
<li>Setup MySQL 5.7 and import your production data dump</li>
<li>Make sure to use the necessary environment variables for your Airbnb clone app</li>
<li>Create an Upstart script that starts Gunicorn to serve <code>api/v1/app.py</code> from your Airbnb clone</li>
<li>Setup Nginx so that the route <code>/api/</code> points to Gunicorn</li>
<li>Nginx must serve this locally but also on its public IP on port <code>80</code></li>
<li>Provide your Upstart config file, name it <code>2-api-upstart_config</code></li>
<li>Provide your Nginx config file, name it <code>2-api-nginx_config</code></li>
</ul><p>Example:</p>


<h4 class="task">
    3. Serve your complete Airbnb clone
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s serve what you built for <a href="/rltoken/JT84WCBQuTsYVyBRTJufLA" target="_blank" title="AirBnB clone - Web dynamic">AirBnB clone - Web dynamic</a> on <code>web01</code>.</p><p>Requirements:</p><ul>
<li>Create an Upstart script that starts Gunicorn to serve <code>web_dynamic/2-hbnb.py</code> from your Airbnb clone</li>
<li>Setup Nginx so that the route <code>/</code> points to Gunicorn</li>
<li>Setup Nginx so that it serves properly static assets contained in <code>web_dynamic/static/</code></li>
<li>For your website to be fully functional, you will need to adapt <code>web_dynamic/static/scripts/2-hbnb.js</code> to the IP and port situation</li>
<li>Nginx must serve this locally but also on its public IP on port <code>80</code></li>
<li>Make sure to pull up your Developer Tool on your favorite browser to verify that you have no error</li>
<li>Provide your Upstart config file, name it <code>3-complete_webapp-upstart_config</code></li>
<li>Provide your Nginx config file, name it <code>3-complete_webapp-nginx_config</code></li>
</ul><p>Example:</p>


<h4 class="task">
    4. No service interuption
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>One of the most important metrics for any Internet-based business is its uptime. It is the percentage of the time over a given period that the service/product is accessible to customers. Let’s pick the example of Amazon.com, for every minute of downtime (which is the opposite of uptime), <a href="/rltoken/MiyMSU6BKTP4jybinNLSZA" target="_blank" title="it costs the company $2M">it costs the company $2M</a>. Yet, application servers often need to restart to update with the new version of the code or new configuration, when doing this operation, an application server cannot serve traffic, which meant downtime.</p><p>To avoid this; application servers are designed with a master/workers infrastructure. The master is in charge of:</p><ul>
<li>Receiving requests</li>
<li>Managing workers (starting, stopping)</li>
<li>Distributing requests to workers</li>
</ul><p>Workers are the actual ones processing the query by generation dynamic content by processing the application code.</p><p>To update an application without downtime, the master will proceed with a progressive rollout of the update. It will gracefully shut down some workers ( meaning that it will tell workers to finish processing the request they are working on, but will not send them new requests, once the worker is done, it’s will be shutdown) and start new ones with the new application code or configuration, then move on to the other old workers until it has renewed the whole pool.</p><p>Write a simple Bash script to reload Gunicorn in a graceful way.</p><p>Example:</p>

