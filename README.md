<center>
# Dailymotion Account Management Framework
</center>

<center><img src="http://i.imgur.com/Qq2vVjP.gif"></center>

Dailymotion.com is a video hosting service that is similar to Youtube.
Users can upload their videos, and get a share of the ad revenue generated when said videos are viewed.

Sometime has passed since this became popular, now I can release this project for my portfolio.

Professionally, I have moved away from using <a href="https://docs.python.org/2/library/tkinter.html">Tkinter</a> since it is a pain in the ass and outdated. Not to mention it is very unstable when using threads (Yes, I know about mtTkinter). <i>I could go on</i>...

PyQt is my favorite toolkit to save time with design. However, I was away from my desktop when I developed this GUI.

<center>
# Motivation:
</center>

I came across this image on a forum that really sparked my interest in getting behind this.

<center><img src="http://i.imgur.com/22Wi1e6.png"></center>

<center>
# Operation:
</center>

The goal was to create many accounts, upload videos, and then use traffic exchange platforms like <a href="https://www.websyndic.com/?ref=996321">Websyndic</a> to generate views. Youtube requires time and commitment to earn revenue from their system. Here all we have to do is fill out a CAPTCHA and verify an email.

<center>
<h3>Phase 1: Create Accounts</h3>
</center>

Using <a href="http://www.seleniumhq.org/docs/03_webdriver.jsp"?Selenium Webdriver</a?, I would control <a href="http://phantomjs.org/">PhantomJS</a> and point the browser to <a href="http://www.dailymotion.com/signin">dailymotion.com/signin</a>.

From there, I would enter an email address which was composed using an <a href="http://www.unixtimestamp.com/">Unix Timestamp</a> to ensure each was unique. For example: 1472215955. (Don't worry, you can't recover the accounts by brute force :P)

<center><img src="http://i.imgur.com/WVODYxu.png"></center>

I decided to just do the bloody CAPTCHA's manually, which is what started the GUI. Being able to quickly cue the CAPTCHA's, I figured 1000 accounts was a pretty small goal, and it was.

<center><img src="http://i.imgur.com/3sLdGjb.png"></center>

Once signed up, and the email verified, I would point PhantomJS to the account settings page to turn on the monetization function of the accounts.

<center><img src="http://i.imgur.com/t1wP5Ul.png"></center>

After a mandatory 2 weeks from signing up, I would then connect the accounts to the prepaid card Dailymotion sent me for my primary account.

<center><img src="http://i.imgur.com/IMC2g2B.png" width=300px height=175px></center>

<b>Since Dailymotion used a third party company to handle payouts, I was able to use one account on <a href="https://www.payoneer.com/en/">Payoneer</a> to connect all my Dailymotion accounts to my prepaid card.</b>

<center><img src="http://i.imgur.com/NbKwn9e.png"></center>

<hr>

<center><h3>Phase 2: Add Content</h3></center>

This part was easy. I did not embed this part to the GUI, but I will talk about the script here for you.

Using <a href="https://rg3.github.io/youtube-dl/">youtube_dl</a> and <a href="https://github.com/dailymotion/dailymotion-sdk-python">Dailymotion SDK</a>, the script would crawl youtube for videos matching the desired criteria then scrape the video to upload over onto Dailymotion.

After some digging around, I managed to compile some notes that others shared to increase the ad revenue per view.
However, I haven't done any testing myself and when I found tips online, they always lacked experiment details that went behind the conclusions.

So, here is the copy and pasted voodoo I found:
<i>
- If you have multiple channels you should use VPS to access each account.
- 15 to 20 videos in your channel to start.
- Add 1 or 2 videos each week.
- Upload videos between 4 to 10 minutes.
- Earnings are updated 2 or 3 times a week.
- Dailymotion does not pay you for amount of hits you send to your videos, they pay for time a videos is watched.
- Do not click on ads which appears around your videos because its violate the dailymotion term and condition. dailymotion terminate your account too.
- 
</i>


<center><h3>Phase 3: Traffic Exchange</h3></center>

I could have done a (<i>extreamly</i>) better job writing this script, <a href="http://pastebin.com/b866QAXr">Tor Traffic Exchange</a>.

It will launch Tor and a web browser, point it to the Websyndic "lite viewer" URL, wait 3000 seconds, close the browser to keep memory consumption low, and repeat.

Soon I will put out something that will take advantage of multiple traffic exchange platforms ^_^.
