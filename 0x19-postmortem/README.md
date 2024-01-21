###Posmortem

An outage happened on an isolated Ubuntu 20.04 container running an Apache web server at around 00:10 Eastern African Time (EAT) on the day that ALX School's System Engineering & DevOps project 0x19 was released. When an HTML file specifying a basic ALX WordPress site was expected in response to GET queries on the server, 500 Internal Server Errors were returned.


###Debugging process

Senior system admin Tedros Alem Asfaha encountered the issue upon opening the project and being, well, instructed to address it, roughly at 12:05 EAT. He promptly proceeded to solve the problem.
<ul>
<li>I checked the running processes using ps aux. Two Apache2 processes, root and www-data, were properly running.</li>
<li>I looked in the sites-available folder of the '/etc/apache2/' directory. Determined that the web server was serving content located in /var/www/html/.</li>
<li>In one terminal, I ran strace on the PID of the root Apache process. In another, curled the server. I expected great things, only to be disappointed. Strace provided no useful information.</li>
<li>Repeat step 3, except for the PID of the www-data process. I kept expectations lower this time, but I was rewarded! strace revealed an -1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.</li>
<li>I looked through files in the /var/www/html/ directory one-by-one, using Vim pattern matching to try and locate the erroneous.phpp file extension. I located it in the wp-settings.php file. (Line 87, require_once ( ABSPATH, WPINC, '/class-wp-locale.php' );).</li>
<li>I removed the trailing p from the line.</li>
<li>I tested another curl on the server. 200 A-ok!</li>
<li>I wrote a Puppet manifest to automate the fixing of the error.</li>


###Summation

In full, the WordPress app was encountering a critical error in ‘wp-settings.php’ when trying to load the file ‘class-wp-locale.phpp’. The correct file name, located in the ‘wp-content’ directory of the application folder, was ‘class-wp-locale.php’.
Patch involved a simple fix on the typo, removing the trailing p.


###Prevention

This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.
Test! Test test test. Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.
Status monitoring. Enable some uptime-monitoring service such as UptimeRobot to alert instantly upon outage of the website.
Note that in response to this error, I wrote a Puppet manifest 0-strace_is_your_friend.pp to automate fixing of any such identical errors should they occur in the future. The manifest replaces any ‘phpp’ extensions in the file ‘/var/www/html/wp-settings.php’ with ‘php’.

