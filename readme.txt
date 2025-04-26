this is a repository where we'll be sharing our advancement for the CAPTCHA solving AI for our AI project


for the "CheckpointNew.pth" file you need to go to this link "https://drive.google.com/drive/folders/1zj0XaMbVoxrVEM4VIIcS8rWatIJYH2M7" and put it inside the directory "captcha_racer"

your working tree should look something like this:

	.
	├── CheckpointNew.pth
	├── cracer.py
	├── ModelLoader.py
	├── __pycache__
	│   └── ModelLoader.cpython-310.pyc
	├── static
	│   ├── images
	│   │   ├── ai_captcha
	│   │   │   └── 
	│   │   ├── captcha
	│   │   │   └──
	│   │   ├── heart-green.png
	│   │   └── heart-red.png
	│   └── styles.css
	└── templates
	    ├── face_the_ai.html
	    ├── home.html
	    ├── multiplayer.html
	    ├── race_ai.html
	    ├── race_the_clock.html
	    ├── solo.html
	    ├── survival_game.html
	    ├── survival.html
	    ├── timer_game.html
	    ├── timer.html
	    └── versus_AI.html

For the captcha racer:
	you need to execute the "cracer.py" file then the server will run on localhost.
	
	you can then select either mode and you will see that it is pretty intuitive to play
	
For the captcha training:
	you can check the file used for training the AI "training.ipynb"
	
	you can also check the file used for generating datasets "gen_cap.py"
	
NOTA:
----
	this project is still under developpement and some functionnalities in the captcha racer game are still to be updated and a multiplayer mode is coming up soon... stay tuned.
	
	the list of fonts used could be changed... we only removed a list of broken fonts that were broken.
	
	
Game rules:
----------
	This game is pretty straight forward, you need to solve captchas correctly, as precisely and as fast as possible.
	Each time you run a game, you will be presented with an image dispalying a 5 chars captcha, below which you will see a text box where you need to enter your answer for the captcha.
	Your score will be updated according to your answer depending on the mode you chose.
	
Modes:
-----
	In this game you have two major modes:
	- Solo mode: in this mode you have two game modes as well:
		- Survival mode: in this mode you can choose among three difficulties (easy, medium and hard), each giving you a fixed amount of lives (resp 5, 3 and 1) that will break whenever you make a mistake (aka enter a wrong captcha).
			Whenever you enter a correct captcha (case sensitive) your score will increase by 5. Otherwise, you will lose a life.
		- Timer challenge: in this mode your goal is again to score as high a score as possible, however, this time since you are running against a clock, your score is gonna increase by 1 for each correctly placed character (case sensitive).
	- Versus AI mode: in this mode you can challenge the captcha soving ai we created, and you can do so in two different modes:
		-Face the ai:
		-Race the ai:
		
			
