<h1 class="gap">0x00. Shell, basics</h1>


<h4 class="task">
    0. Where am I?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the absolute path name of the current working directory.</p><p>Example:</p>


<h4 class="task">
    1. What’s in there?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display the contents list of your current directory.</p><p>Example:</p>


<h4 class="task">
    2. There is no place like home
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the working directory to the user’s home directory.</p><ul>
<li>You are not allowed to use any shell variables</li>
</ul>


<h4 class="task">
    3. The long format
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display current directory contents in a long format</p><p>Example:</p>


<h4 class="task">
    4. Hidden files
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display current directory contents, including hidden files (starting with <code>.</code>). Use the long format.</p><p>Example:</p>


<h4 class="task">
    5. I love numbers
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display current directory contents.</p><ul>
<li>Long format</li>
<li>with user and group IDs displayed numerically</li>
<li>And hidden files (starting with .)</li>
</ul><p>Example:</p>


<h4 class="task">
    6. Welcome holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that creates a directory named <code>holberton</code> in the <code>/tmp/</code> directory.</p><p>Example:</p>


<h4 class="task">
    7. Betty in Holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Move the file <code>betty</code> from <code>/tmp/</code> to <code>/tmp/holberton</code>.</p><p>Example:</p>


<h4 class="task">
    8. Bye bye Betty
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Delete the file <code>betty</code>.</p><ul>
<li>The file <code>betty</code> is in <code>/tmp/holberton</code></li>
</ul><p>Example:</p>


<h4 class="task">
    9. Bye bye Holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Delete the directory <code>holberton</code> that is in the <code>/tmp</code> directory.</p><p>Example:</p>


<h4 class="task">
    10. Back to the future
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that changes the working directory to the previous one.</p>


<h4 class="task">
    11. Lists
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the <code>/boot</code> directory (in this order), in long format.</p>


<h4 class="task">
    12. File type
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints the type of the file named <code>iamafile</code>. The file <code>iamafile</code> will be in the <code>/tmp</code> directory when we will run your script.</p><p>Example</p>


<h4 class="task">
    13. We are symbols, and inhabit symbols
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a symbolic link to <code>/bin/ls</code>, named <code>__ls__</code>.
The symbolic link should be created in the current working directory. </p>


<h4 class="task">
    14. Copy HTML files
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.</p><p>You can consider that all HTML files have the extension <code>.html</code></p>


<h4 class="task">
    15. Let’s move
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that moves all files beginning with an uppercase letter to the directory <code>/tmp/u</code>.</p><p>You can assume that the directory <code>/tmp/u</code> will exist when we will run your script</p>


<h4 class="task">
    16. Clean Emacs
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that deletes all files in the current working directory that end with the character <code>~</code>.</p>


<h4 class="task">
    17. Tree
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that creates the directories <code>welcome/</code>, <code>welcome/to/</code> and <code>welcome/to/holberton</code> in the current directory.</p><p>You are only allowed to use two spaces in your script, not more.</p>


<h4 class="task">
    18. Life is a series of commas, not periods
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a command that lists all the files and directories of the current directory, separated by commas (<code>,</code>).</p><ul>
<li>Directory names should end with a slash (<code>/</code>)<br/></li>
<li>Files and directories starting with a dot (<code>.</code>) should be listed<br/></li>
<li>The listing should be alpha ordered, except for the directories <code>.</code> and <code>..</code> which should be listed at the very beginning</li>
<li>Only digits and letters are used to sort; Digits should come first</li>
<li>You can assume that all the files we will test with will have at least one letter or one digit</li>
<li>The listing should end with a new line<br/></li>
</ul>


<h4 class="task">
    19. File type: Holberton
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Create a magic file <code>holberton.mgc</code> that can be used with the command <code>file</code> to detect <code>Holberton</code> data files. <code>Holberton</code> data files always contain the string <code>HOLBERTON</code> at offset 0.</p><p><strong>holberton.mgc has to be created on Ubuntu 14.04 LTS</strong></p>

