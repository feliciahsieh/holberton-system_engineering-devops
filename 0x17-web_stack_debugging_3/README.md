<h1 class="gap">0x17. Web stack debugging #3</h1>


<h4 class="task">
    0. Strace is you friend
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p><a href="https://www.youtube.com/watch?v=80XQ0TI2zb4&amp;feature=youtu.be" target="_blank"><img alt="webstack debugging" src="https://image.ibb.co/ijfyqa/web_stack_debugging_3.jpg"/></a></p><p>Using <code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).</p><p>Hint:</p><ul>
<li><code>strace</code> can attach to a current running process</li>
<li>You can use <code>tmux</code> to run <code>strace</code> in one windows and <code>curl</code> in another one</li>
</ul><p>Requirements:</p><ul>
<li>Your <code>0-strace_is_your_friend.pp</code> file must contain Puppet code</li>
<li>You can use whatever Puppet resource type you want for you fix</li>
</ul><p>Example:</p>

