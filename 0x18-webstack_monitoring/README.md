<h1 class="gap">0x18. Webstack monitoring</h1>


<h4 class="task">
    0. Monitor your Nginx traffic
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Let’s monitor our Nginx server traffic (access log and error log), by installing <a href="/rltoken/iZXLFtq7EfU2-iObKg2xEg" target="_blank" title="Sumlogic">Sumlogic</a> on <code>web-01</code> (feel free to do it on other servers a well). Create an account and follow the setup wizard flow.</p><p>Requirements:</p><ul>
<li>The account must be a <code>SUMO LOGIC FREE</code></li>
<li>The account must be configured for <code>NORTH AMERICA</code></li>
<li>You must use your <code>ID@holbertonschool.com</code> email address</li>
<li>You must select <code>Nginx</code> as Data Type to import</li>
<li>Create a Sumo Logic access key, share it in your answer file:

<ul>
<li>First line: <code>Access ID</code></li>
<li>Second line: <code>Access Key</code></li>
</ul></li>
</ul><p>After you are done, you should see a “Nginx - Overview” tab in your Dashboard menu</p><p><img alt="Nginx overview dashboard" src="http://i.imgur.com/a6d20PJ.jpg"/></p>


<h4 class="task">
    1. Monitor your server
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Your Nginx is running on a server and its health will impact how well Nginx and other server running on it perform. A server that is overloaded with tasks that are too CPU, memory, disk or network intensive will end up not performing as expected, might just freeze and crash.</p><p>Configure Sumo Logic to monitor your servers memory, CPU, network and disk. Once you are done you should be able to explore your machine performances in the metric tab:</p><p><img alt="Sumo Logic metric tab" src="https://i.imgur.com/OKYDhCv.png"/></p>

