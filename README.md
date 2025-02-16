# Instructions to run

We are using python 3.13.2 (latest release), please ensure you have this version installed!


Run these commands to install the dependencies:  
(If pip doesn't work, try pip3)  
$ python3 -m ensurepip --upgrade  
$ python3 -m pip3 install --upgrade pip  
$ python3 -m pip3 install dearpygui  
$ sudo apt install libpq-dev python3-dev  
$ python3 -m pip3 install psycopg2  
  
To run the program:  
$ python3 main.py  
  
# Expected output:  
  
- Splash screen with "PHOTON" should appear.  
- Red and Green team player information in a table: Player number, ID, and codename.  
- You are able to add two players via the console.  
- An example terminal output:  
'''
[STARTING] Server is starting...  
Add players to database via the GUI - can also uncomment  
the runTest() function to add players to the database directly  
  
Equipment ID is input via the console.  
  
Enter equipment ID of player 1: 1  
[SERVER] Here is player's equipment number: b'1'  
Enter equipment ID of plater 2: 6  
[SERVER] Here is player's equipment number: b'6'  
Enter equipment ID of plater 3: 3  
[SERVER] Here is player's equipment number: b'3'  
Enter equipment ID of plater 4: 2  
[SERVER] Here is player's equipment number: b'2'  
''' 
# Contributors  

Lillian Morris - lillianmikayla  
Mary-Claire Ridgeway - mc-ridge  
Katelynn Adair - faydellee  
Sophie Phillips - sophmin05  
Samantha Jackson - samichar  
