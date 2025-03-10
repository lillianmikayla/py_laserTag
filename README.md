# Instructions to run

We are using python 3.13.2 (latest release), please ensure you have this version installed!


Run these commands to install the dependencies:  
(If pip doesn't work, try pip3)  
$ python3 -m pip3 install --upgrade pip  
$ python3 -m pip3 install dearpygui  
$ sudo apt install libpq-dev python3-dev  
$ python3 -m pip3 install psycopg2  
$ pip install Pillow (<- New!)
  
To run the program:  
$ python3 main.py  
  
# Expected output:  
  
- Splash screen with "PHOTON" should appear.  
- Red and Green team player information in a table: Player number, ID, and codename.
- Three button options at the bottom: "Switch UDP network", "Start", and "Clear".

  If "Start" is pressed:
  - 30 second count down timer begins
  - When timer is up, the play action screen comes up
  - In the first column, there is the red team scores
  - In the second column, there is current game action
  - In the last column, there is the green team scores
  - At the bottom there is the game timer  
   
  If "Clear" is pressed:
  - The data in the tables should all be cleared

# Contributors  

Lillian Morris - lillianmikayla  
Mary-Claire Ridgeway - mc-ridge  
Katelynn Adair - faydellee  
Sophie Phillips - sophmin05  
Samantha Jackson - samichar  
