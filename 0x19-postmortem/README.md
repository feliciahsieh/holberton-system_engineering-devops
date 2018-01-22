Post-Mortem
Sumo Logic Installation on Web Server
1/23/18

Update of Sumo Logic installation Project
The app won. As we're closing on the deadline install, no further progress can be made tonight. In the immortal words of Scarlett O'Hara, "Tomorrow is another day."

Goal: Install the Sumo Logic application on my webserver per 0x18. Webstack monitoring
Outage: 14 hrs and going starting from 10:00 am earlier today. Cannot track 
Impact: This affects only one user (me). The web server, masquerading as 214-web-01 is not serving any critical content. The world remains safe.
Root cause: Gremlins

Timeline (aka Felicia's Irish Lament)
10:00 am: Arrived on-site and exchanged a few pleasantries with colleagues.
10:30 am: Found out the iMac was imaged to Apple's High Sierra OS. Uh-oh. Vagrant was gone. Not a trace, even though Vagrant & programs were installed the day before. Call me Ms. Vagrant. Reinstalled vagrant & programs again (~15). Installed my my .ssh keys again.

11:00 am: Noticed the new screensaver locks the screen at ~1 minute vs the old way, which had a longer delay. Discovered I can’t change the sleep timer anymore. Kiren and I let I.T. know.

11:10 am: Signed up for the Sumo Logic Free Trial with my 214@ email as required. Started installing Sumo Logic onto my Virtual Machine, web01. Walked away to attend Stand-up.

11:30 am Stand-up lasted 30 minutes. Returned to my iMac to notice that 

12:00 pm Sumologic wizard did not finish. The terminals logged out from inactivity/locked screen. Uh-oh. 

12:10 pm Tried to sign up for the Sumo Logic Free Trial again with my 2nd holberton email. Got the spinning wheel of death. Decided against using this email because that’s not the requirement. However, did run the wget command, which might have erased the original access key.
Contacted Alex, Sumo Logic Customer Support, via chat. Recommended logging out of Sumo Logic GUI. Lost ability to contact Customer Support. Tried to log back in. GUI asked me for a password, but one was never set. GUI was tricky.

12:45 pm Found email from Sumo Logic saying to Authorize App. Sumo Logic did not mentioned that the email was their primary key, and it must be acknowledged. Found both emails. Only clicked the button on the first email.

1:00 pm - 1:45 pm LUNCH because was I was weary

1:45 pm - 4:00 pm Opened Sumo Logic Customer Support trouble ticket via email. Eventually, found Alex and started chatting again.
-Enabled security flag so he could see my settings.
-I discovered my Nginx wasn’t running. Asked for help on Slack. Advice was to run “nginx -t” and discovered a stray *.sql file in sites-enabled directory from some previous testing from weeks ago. Started Nginx up after the file was removed.
-Curled Sumo Logic’s location. Status code=200. No problem with firewall.
-Went through some basic troubleshooting with Alex. He can view my settings but not my screen. Why aren’t they using LogMeIn or similar tool? He’s able to see web01 data, but I can’t.
-While working with Sumo Logic, I found at least 2 bugs their new GUI. You must refresh as occasionally status is not reflected. Also saw a blank screen when there should’ve been data.
-To communicate better, I’m sending screenshots through chat.
Alex discovered that my Time Zone was set to PST but should’ve been left as UTC. Setting the time zone correctly fixed 2 of the 4 panels in “Nginx - Overview”.
-Also in the GUI, adding a “source” from the “Collection” is DIFFERENT from adding it from the “App Catalog>Library”. The panels are different.
-I also tried installing Sumo Logic on my laptop. I saw the “Spinning Wheel of Death” and gave up after awhile.
-Quick 20 min side meeting then went back to debugging with Alex.
-Walked Kiren through the Sumo Logic installation in 10 minutes. Felt ridiculous at this point. Suspect infamous Gremlins that like to hover around my hardware.
-Alex has tools that I cannot see, he shared his panel views for “Nginx - Overview”. This is the mandatory portion. My webserver is fine. Sumo Logic app is not.

6:00 pm - Received a message on iMac that my machine must be rebooted. No one else seems to have this message.

6:20 pm - Told Larry about keeping Time Zone setting as UTC. Walked Larry through Sumo Logic installation in 10 minutes also. Life is absurd.

6:45 pm - Signed up for Sumo Logic’s Slack channel as last-ditch effort to get Advanced portion of project working. Even signing up for the Slack channel was a hassle (required separate password).

7:00 pm - Could not find the elusive Gremlins. Will need to install cameras around my station.

Root Cause and Resolution:
-Guessing the Private Key was erased on the 2nd installation attempt
-If Sumo Logic installation is interrupted (Internet or screen locked), disaster strikes
-Sumo Logic GUI is buggy
-Would have been better if iMacs were rigorously tested before upgrading and settings preserved. Vagrant backed up. Screensaver time kept at previous setting.
-Suspect High Sierra might have some issues (2 reboots were needed)
-Sumo Logic’s non-use of remote login tool, like LogMeIn, delayed troubleshooting
-Asking for mercy on the grading since I’ve helped 2 other installations + Advanced.

Corrective and Preventative Measures:
-Sumo Logic to handle graceful recovery if installation of Free version is Interrupted
-Sumo Logic to provide explanation of Installation Process and where to find help.
-Sumo Logic Customer Support was great, but wished it wasn’t necessary.
-Look at alternatives to Sumo Logic as a tool.
-Next time, I should have quit earlier. Time would have been better spent working on my Final Project. Call me stubborn.
-Not start Sumo Logic install unless I have an hour to babysit the tool.
-Reduce reimaging the iMacs and archive vagrants on all the machines. I wasn’t the only one that lost work and time.
-Need to buy Gremlin repellent.
-Build a bar in the kitchen area. Cheers to that! (clink)
