William Wright, Anthony Italiano, Derek Studer

Hostname of our server: fubarGroup
IP of our server: 172.17.9.15 -- subject to change, apparently. Our IP keeps changing.

We added each user using adduser and then our usernames.


We then asked Louis to sign in so we could verify our sudo permissions worked when we added them
to the groups file. -- they did.

We used the command "17 4    * * *   root    tar -zcf /backups/home.tgz /home/"
to run backups every night at 4:17 in the morning. The backups will be copied to the backup folder
inside the root. This will backup the /home folder, which includes every user.
After neglecting this crontab for a few days, we realized it didn't even work. On Wednesday,
december 6th, I used "sudo su" to login as root and then modify the crontab using the command above. This hopefully, will work. 

We installed the ssh server and LAMP stack by selecting them when we were prompted.. Then we created a default account named administrator, which we then used as to create all our accounts.

We updated the software by using
sudo apt-get update to retreive the latest files

and sudo apt-get upgrade to download all the updates necessary. Then, we used sudo reboot to reboot and install.

Anthony created a basic and appealing HTMl page for our group and put it in the /var/www/html directory so that it would be loaded once our server was. we also made public_html folders for each user and loaded in files for all but administrator. The files were simply index.html for each specific user, this are very basic and useless. 

Userdir: 

we made sure it was enabled by typing sudo a2enmod userdir

then used:

sudo nano /etc/apache2/mods-enabled/userdir.conf to decide which directories to allow access to.

We ran into issues here because we kept getting a "Forbidden" error, which can either stem from an encrypted home directory (we don't have that) or, as a new feature in apache2.4, old systems and new systems, (old:Order allow,deny \n Allow from all) cannot mix, and so I had to change everything to be the newer, cleaner access modifier. I then allowed access to our HTML using "Require all granted" in the fields that used to say "Order allow,deny"

Everything above took place in the userdir.conf.

Below is where we enabled php usage. We had to comment out a block of code to bypass a php filter. This was done in php7.0.conf using the command:

sudo nano /etc/apache2/mods-available/php7.0.conf

The code actually tells you exactly what to comment out, so once we did that, we had no issues. 

Our webpage works, and so do the individual sites. We should get 100% on this assignment.

