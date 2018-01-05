<h1 class="gap">0x01. Shell, permissions</h1>


<h4 class="task">
    0. My name is Betty
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that changes your user ID to <code>betty</code>.</p><ul>
<li>You should use exactly 8 characters for your command (+1 character for the new line)</li>
<li>You can assume that the user <code>betty</code> will exist when we will run your script</li>
</ul>


<h4 class="task">
    1. Who am I
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the effective userid of the current user.</p>


<h4 class="task">
    2. Empty!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that creates an empty file called <code>hello</code>.</p>


<h4 class="task">
    3. Groups
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints all the groups the current user is part of.</p>


<h4 class="task">
    4. New owner
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the owner of the file <code>hello</code> to the user <code>betty</code>.</p>


<h4 class="task">
    5. Execute
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that adds execute permission to the owner of the file <code>hello</code>.</p><ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>


<h4 class="task">
    6. Multiple permissions
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file <code>hello</code>.</p><ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>


<h4 class="task">
    7. Everybody!
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that adds execution permission to the owner, the group owner and the other users, to the file <code>hello</code></p><ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>You are not allowed to use commas for this script</li>
</ul>


<h4 class="task">
    8. James Bond
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that sets the permission to the file <code>hello</code> as follows:</p><ul>
<li>Owner: no permission at all</li>
<li>Group: no permission at all</li>
<li>Other users: all the permissions</li>
</ul><p>The file <code>hello</code> will be in the working directory
You are not allowed to use commas for this script</p>


<h4 class="task">
    9. John Doe
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that sets the mode of the file <code>hello</code> to this:</p>


<h4 class="task">
    10. Look in the mirror
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that sets the mode of the file <code>hello</code> the same as <code>olleh</code>’s mode.</p><ul>
<li>The file <code>hello</code> will be in the working directory</li>
<li>The file <code>olleh</code> will be in the working directory</li>
</ul>


<h4 class="task">
    11. Directories
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that adds execute permission to all subdirectories of the current directory for  the owner, the group owner and all other users. Regular files should not be changed.</p>


<h4 class="task">
    12. More directories
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that creates a directory called <code>dir_holberton</code> with permissions 751 in the working directory.</p>


<h4 class="task">
    13. Change group
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the group owner to <code>holberton</code> for the file <code>hello</code></p><ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>


<h4 class="task">
    14. Owner and group
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the owner to <code>betty</code> and the group owner to <code>holberton</code> for all the files and directories in the working directory.</p>


<h4 class="task">
    15. Symbolic links
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the owner and the group owner of the file <code>_hello</code> to <code>betty</code> and <code>holberton</code> respectively.</p><ul>
<li>The file <code>_hello</code> is in the working directory</li>
<li>The file <code>_hello</code> is a symbolic link</li>
</ul>


<h4 class="task">
    16. If only
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the owner of the file <code>hello</code> to <code>betty</code> only if it is owned by the user <code>guillaume</code>.</p><ul>
<li>The file <code>hello</code> will be in the working directory</li>
</ul>


<h4 class="task">
    17. Star Wars
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that will play the StarWars IV episode in the terminal.</p>


<h4 class="task">
    18. RTFM
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Create a man that looks exactly like this one and passes all checks.</p>

