Post-Mortem
Sumo Logic Installation on Web Server
1/23/18

UPDATE OF SUMO LOGIC INSTALLATION PROJECT:
The app won. As we're closing on the project deadline, no further progress can be made tonight. In the immortal words of Scarlett O'Hara, "Tomorrow is another day."

GOAL: Install the Sumo Logic application on my webserver per 0x18. Webstack monitoring
OUTAGE: 14 hrs and going starting from 10:00 am earlier today. Got Mandatory working but not the Advanced
IMPACT: This affects only one user (me). The web server, masquerading as 214-web-01, is not serving any critical content. The world remains safe.
ROOT CAUSE: Gremlins. I caught a glance of something like this,
http://ksassets.timeincuk.net/wp/uploads/sites/55/2017/08/2015Gremlins_GettyImages-163067748261115-920x610-920x584.jpg

TIMELINE (aka Felicia's Irish Lament):
10:00 am: Arrived on-site and exchanged a few pleasantries with colleagues.
10:30 am: Found out the iMac was imaged to Apple's High Sierra OS. Uh-oh. Vagrant was gone. Not a trace, even though Vagrant & programs were installed the day before. Have installed Vagrant ~20 times in last 8 months. Call me Ms. Vagrant. Reinstalled vagrant & programs again (~15). Installed my .ssh keys again.

11:00 am: Noticed the new screensaver locks the screen at ~1 minute vs yesterday, which had a longer wait time. Discovered I can’t change the sleep timer anymore. Kiren and I let I.T. know.

11:10 am: Signed up for the Sumo Logic Free Trial with my 214@ email as required. Started installing Sumo Logic onto my Virtual Machine, web01. In the middle of the install, I walked away to attend Stand-up.

11:30 am: Stand-up lasted 30 minutes.

12:00 pm: Returned to my iMac to notice that terminals had an error message. Closed them. Sumologic wizard did not finish. The terminals logged out from inactivity/locked screen. [Insert swear words].

12:10 pm: Tried to sign up for the Sumo Logic Free Trial again with my 2nd holberton email. Got the spinning wheel of death. Decided against using this email because that’s not the requirement. However, did run the wget command, which might have erased the original access key.
Contacted Alex, Sumo Logic Customer Support, via chat. Recommended logging out of Sumo Logic GUI. Lost ability to contact Customer Support. Tried to log back in. GUI asked me for a password, but one was never set. GUI was tricky. [Insert more swear words]

12:45 pm: Found email from Sumo Logic saying to Authorize App. Sumo Logic did not mentioned that the email was their primary key, and it must be acknowledged. Found both emails. Only clicked the button on the first email.

1:00 pm - 1:45 pm: LUNCH because was I was faint with hunger. It was delicious. Thanks for asking.

1:45 pm - 4:00 pm: Opened Sumo Logic Customer Support trouble ticket via email. Eventually, found Alex and started chatting again.
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

6:00 pm: Received a message on iMac that my machine must be rebooted. No one else seems to have this message.

6:20 pm: Told Larry about keeping Time Zone setting as UTC. Walked Larry through Sumo Logic installation in 10 minutes also. Life is absurd.

6:45 pm: Signed up for Sumo Logic’s Slack channel as last-ditch effort to get Advanced portion of project working. Even signing up for the Slack channel was a hassle (required separate password). [Update: A Sumo Logic employee from Australia answered my post at midnight, but I was too tired].

7:00 pm: Could not find the elusive Gremlins. Will need to install cameras around my station.

ROOT CAUSE AND RESOLUTION:
-Guessing the Private Key was erased on the 2nd installation attempt
-If Sumo Logic installation is interrupted (Internet or screen locked), disaster strikes. 
-Sumo Logic GUI is buggy
-Don't ever upgrade to a new MacOS before this project. Computer settings need to be preserved, and Vagrant must be backed up. Screensaver time should be kept at previous setting.
-Suspect High Sierra might have some issues (2 reboots were needed)
-Sumo Logic’s non-use of remote login tool, like LogMeIn, delayed troubleshooting.
-Asking for mercy on the grading since I’ve helped 2 other installations + Advanced.

CORRECTIVE AND PREVENTATIVE MEASURES:
-Sumo Logic to handle graceful recovery if installation of Free version is Interrupted
-Sumo Logic to provide explanation of Installation Process and where to find help.
-Sumo Logic Customer Support was great, but wished it wasn’t necessary.
-Look at alternatives to Sumo Logic as a tool.
-Next time, I should have quit earlier. Time would have been better spent working on my Final Project. Call me stubborn.
-Under pain of death, do not start Sumo Logic install unless I have an hour to babysit the tool.
-Reduce reimaging the iMacs and archive vagrants on all the machines. I wasn’t the only one that lost work and time.
-Need to buy Gremlin repellent.
-Build a bar in the kitchen area. Cheers to that! (clink)
-We are also suffering from extreme chocolate deprivation. Emergency French chocolate must be airlifted to me ASAP.
-I'm considering writing a novel because this is a touchingly sad and eloquent story, worthy of the Blarney Stone.
-[Update 1/24/18 5:08 pm, Andrew found the uninstall command and re-installed, but now nothing works. The saga continues ...]

¯\_(ツ)_/¯