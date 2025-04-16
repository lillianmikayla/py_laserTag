# Instructions to run

We are using python 3.13.2 (latest release), please ensure you have this version installed!


Run these commands to install the dependencies:  
(If pip doesn't work, try pip3 or python3 -m pip3)  
$ sudo apt-get install python3-pip  
$ pip install --upgrade pip  
$ pip install dearpygui  
$ sudo apt install libpq-dev python3-dev  
$ python3 -m pip install psycopg2  
$ sudo apt-get install python3-tk  
$ pip install Pillow  
$ pip install pygame (<-- NEW!!)  
  
To run the program:  
$ python3 main.py  
  
# Expected output:  
  
- Splash screen with "PHOTON" should appear.   
- Red and Green team player information in a table: Player number, ID, and codename.  
- Three button options at the bottom: "Switch UDP network", "Start", and "Clear".  

  If "Start" is pressed:  
  - 30 second count down timer begins  
  - When timer is up, the play action screen comes up  
  - In the first column, there is the red team codenames and scores  
  - In the second column, there is current game action. This will update with events according to the traffic generator.  
  - In the last column, there is the green team codenames and scores  
  - At the bottom there is the game timer that counts down from 6 minutes  
  - When the timer is up, there will be a "Game Over" text that appears  
  - Winning teams score will highlight  
  - A stylized B will be added to player names who touch base
  - Music will play throughout the game  
   
  If "Clear" is pressed:
  - The data in the tables should all be cleared

# Contributors  

Lillian Morris - lillianmikayla  
Mary-Claire Ridgeway - mc-ridge  
Katelynn Adair - faydellee  
Sophie Phillips - sophmin05  
Samantha Jackson - samichar  
