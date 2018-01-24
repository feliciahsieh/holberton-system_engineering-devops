Issue Summary (that is often what executives will read) must contain:
-duration of the outage with start and end times (including timezone)
-what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
-what was the root cause

Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:
-when was the issue detected
-how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
-actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
-misleading investigation/debugging paths that were taken
-which team/individuals was the incident escalated to
-how the incident was resolved

Root cause and resolution must contain:
-explain in detail what was causing the issue
-explain in detail how the issue was fixed

Corrective and preventative measures must contain:
-what are the things that can be improved/fixed (broadly speaking)
-a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)

400 to 600 words
-----------------------
Issues with Holberton iMac / Sumologic

Issue was to work on holberton-system_engineering-devops/0x18. Webstack monitoring

10:30am: Found out the iMac was imaged to Apple's High Sierra, which means vagrant was gone. Reinstalled vagrant, all programs running on vagrant (~15), including my .ssh keys. Referred to the intranet to find the exact versions to install.
-The new screen saver kept locking the screen at ~1 minute. Discovered users can’t change this setting anymore. Kiren and I let Jul know.
-Signed up for the Sumologic Free Trial with my 214@ email. Started installing Sumologic onto my Virtual Machine, web01.
11:30am Standup, that lasted 30 minutes.
12:00pm Sumologic wizard did not finish. The terminals logged out from inactivity/locked screen. Thus began the ordeal.
12:10pm Tried to sign up for the Sumologic Free Trial again with my 2nd holberton email. Got the spinning wheel of death.
12:30pm Contacted Sumologic Customer Support. Recommended logging out of Sumologic GUI. Lost ability to contact Customer Support. Tried to log back in. It asked me for a PASSWORD that was never set.
12:45pm Found email from Sumologic saying to Authorize App. Note, they never mentioned that the email was their primary key and it must be acknowledged. Found both emails.
1:00pm - 1:45pm LUNCH because was faint with hunger
1:45pm - 4:00 pm Contacted Sumologic Customer Support, Alex. Enabled security flag so he could see my settings. Went through some basic troubleshooting, but he can view my settings BUT NOT my screen. It is odd that they are not using LogMeIn so they can see my screen. He’s able to see web01 data, but I can’t.

-Discovered Nginx had a stray *.sql file from previous project testing. Found with “nginx -t”
-Nginx started up
-Found at least 2 bugs with Sumologic new GUI, Refresh occasionally doesn’t work. Also saw a blank screen when there should’ve been data.
-LUNCH
-Contacted Sumologic Tech Support. Sending screenshots back and forth.
-Time zone was set to PST but should’ve been left as UTC. Setting the time zone incorrectly did not reset the panels
-Another Sumologic bug is adding a “source” from the “Collection” is DIFFERENT from adding it from the “App Catalog>Library”
-Chatted with Sumologic customer support, Alex for 3 hours
-Tried installing on my laptop. Saw the “Spinning Wheel of Death”
-Quick 20 min meeting
-Continued Sumologic debugging with Alex
-Walked Kiren through the Sumologic install in 10 minutes
-Suspect infamous gremlins that hover around Felicia when she's near hardware.

Post Mortem
-Never use Sumologic. Never use Sumologic on Vagrant on iMac on 

There's also a typo on the Holberton Intranet, ironically on the "Sumlogic" link

6pm - Machine must be rebooted