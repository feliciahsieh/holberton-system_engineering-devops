<h1 class="gap">0x02. Shell, I/O Redirections and filters</h1>


<h4 class="task">
    0. Hello World
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that prints “Hello, World”, followed by a new line to the standard output.</p>


<h4 class="task">
    1. Confused smiley
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that displays a confused smiley <code>"(Ôo)'</code>.</p>


<h4 class="task">
    2. Let's display a file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display the content of the <code>/etc/passwd</code> file.</p><p>Example:</p>


<h4 class="task">
    3. What about 2?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display the content of <code>/etc/passwd</code> and <code>/etc/hosts</code></p><p>Example:</p>


<h4 class="task">
    4. Last lines of a file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display the last 10 lines of <code>/etc/passwd</code></p><p>Example:</p>


<h4 class="task">
    5. I'd prefer the first ones actually
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display the first 10 lines of <code>/etc/passwd</code></p><p>Example:</p>


<h4 class="task">
    6. Line #2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that displays the third line of the file <code>iacta</code>.</p><p>The file <code>iacta</code> will be in the working directory</p><ul>
<li>You’re not allowed to use <code>sed</code></li>
</ul>


<h4 class="task">
    7. Save current state of directory
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that writes into the file <code>ls_cwd_content</code> the result of the command <code>ls -la</code>. If the file <code>ls_cwd_content</code> already exists, it should be overwritten. If the file <code>ls_cwd_content</code> does not exist, create it.</p>


<h4 class="task">
    8. It is a good file that cuts iron without making a noise
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a shell script that creates a file named exactly <code>\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)</code> containing the text <code>Holberton School</code>  ending by a new line.</p>


<h4 class="task">
    9. Duplicate last line
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that duplicates the last line of the file <code>iacta</code></p><ul>
<li>The file <code>iacta</code> will be in the working directory</li>
</ul>


<h4 class="task">
    10. No more javascript
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that deletes all the regular files (not the directories) with a <code>.js</code> extension that are present in the current directory and all its subfolders.</p>


<h4 class="task">
    11. Don't just count your directories, make your directories count
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that counts the number of directories and sub-directories in the current directory.</p><ul>
<li>The current and parent directories should not be taken into account<br/></li>
<li>Hidden directories should be counted<br/></li>
</ul>


<h4 class="task">
    12. What’s new
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that displays the 10 newest files in the current directory.</p><p>Requirements:</p><ul>
<li>One file per line</li>
<li>Sorted from the newest to the oldest</li>
</ul>


<h4 class="task">
    13. Being unique is better than being perfect
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a scripts that takes a list of words as input and prints only words that appear exactly once.</p><ul>
<li>Input format: One line, one word</li>
<li>Output format: One line, one word</li>
<li>Words should be sorted</li>
</ul>


<h4 class="task">
    14. It must be in that file
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display lines containing the pattern “root” from the file <code>/etc/passwd</code></p>


<h4 class="task">
    15. Count that word
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display the number of lines that contain the pattern “bin” in the file <code>/etc/passwd</code></p>


<h4 class="task">
    16. What's next?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display lines containing the pattern “root” and 3 lines after them in the file <code>/etc/passwd</code>.</p>


<h4 class="task">
    17. I hate bins
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display all the lines in the file <code>/etc/passwd</code> that do not contain the pattern “bin”.</p>


<h4 class="task">
    18. Letters only please
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Display all lines of the file <code>/etc/ssh/sshd_config</code> starting with a letter.</p><ul>
<li>include capital letters as well</li>
</ul>


<h4 class="task">
    19. A to Z
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Replace all characters <code>A</code> and <code>c</code> from input to <code>Z</code> and <code>e</code> respectively.</p>


<h4 class="task">
    20. Without C, you would live in hiago
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Create a script that removes all letters <code>c</code> and <code>C</code> from input.</p>


<h4 class="task">
    21. esreveR
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that reverse its input.</p>


<h4 class="task">
    22. DJ Cut Killer
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
</h4><p>Write a script that displays all users and their home directories, sorted by users.</p><ul>
<li>Based on the the <code>/etc/passwd</code> file</li>
</ul>


<h4 class="task">
    23. Empty casks make the most noise
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a command that finds all empty files and directories in the current directory and all sub-directories.</p><ul>
<li>Only the names of the files and directories should be displayed (not the entire path)<br/></li>
<li>Hidden files should be listed</li>
<li>One file name per line<br/></li>
<li>The listing should end with a new line</li>
<li>You are not allowed to use <code>basename</code>, <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>


<h4 class="task">
    24. A gif is worth ten thousand words
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that lists all the files with a <code>.gif</code> extension in the current directory and all its sub-directories.</p><ul>
<li>Hidden files should be listed</li>
<li>Only regular files (not directories) should be listed</li>
<li>The names of the files should be displayed without their extensions</li>
<li>The files should be sorted by byte values, but case-insensitive (file <code>aaa</code> should be listed before file <code>bbb</code>, file <code>.b</code> should be listed before file <code>a</code>, and file <code>Rona</code> should be listed after file <code>jay</code>) </li>
<li>One file name per line</li>
<li>The listing should end with a new line</li>
<li>You are not allowed to use <code>basename</code>, <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>


<h4 class="task">
    25. Acrostic
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. <a href="/rltoken/V8wUlT1trv0XGLfOIFgu6w" target="_blank" title="Read more">Read more</a>.</p><p>Create a script that decodes acrostics that use the first letter of each line.</p><ul>
<li>The ‘decoded’ message has to end with a new line</li>
<li>You are not allowed to use <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul>


<h4 class="task">
    26. The biggest fan
      <span class="alert alert-info mandatory-optional">
        #advanced
      </span>
</h4><p>Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.</p><ul>
<li>Order by number of requests, most active host or IP at the top</li>
<li>You are not allowed to use <code>grep</code>, <code>egrep</code>, <code>fgrep</code> or <code>rgrep</code></li>
</ul><p>Format:</p>

