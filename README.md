# Hangman
Hangman is a Python terminal game which runs on Heroku.

Hangman is a word guessing game. This started out as a paper-and-pencil game that can involve two or more players. One player will think of a word, phrase or sentence and the other player(s) will try to guess the word within a certain number of guesses. Each incorrect guess will cause an element of hangman being drawn. If the players guess the word before the drawing is complete they win otherwise they lose to the player who set the word.

In this game the user plays against the computer which will generate a random word to be guessed. Instructions are provided in the game to teach the user how to play.

[Link to Hangman game]()

![Game shown on a range of devices](docs/amiresponsive.png)

* [How to play](#How-to-play)
* [User Experience (UX)](#User-Experience-(UX))
  * [Initial Discussion](#Initial-Discussion)
  * [User Stories](#User-Stories)

* [Design](#Design)
  * [Colour Scheme](#Colour-Scheme)
  * [Graphics](#Graphics)
  * [Flowchart](#Flowchart)
  
* [Features](#Features)
  * [Future features](#Future-features)

* [Technologies Used](#Technologies-Used)
  * [Languages Used](#Languages-Used)
  * [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)

* [Testing](#Testing)
  * [Solved Bugs](#Solved-Bugs)
  * [Known Bugs](#Known-Bugs)
  * [PEP8](#PEP8)
  * [Manual Testing](#Manual-Testing)

* [Deployment](#Deployment)
  * [Local Deployment](#Local-Deployment)
  * [Remote Deployment](#Remote-Deployment)
  * [Deploy project to Heroku](#Deploy-project-to-Heroku)
  
* [Credits](#Credits)
  * [Code](#Code)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

- - -

## How to play

The object of the game is to figure out the unknown word by guessing letters. 
The length of the word is explicitly stated and is marked by underscores for each letter to be guessed. 
If the letter guessed by the user is in the unknown word it will display by replacing the underscores wherever the letter occurs.
If the guessed letter is not in the unknown word the user will lose a try. This will correspond to a person on the gallow being drawn, one part for each incorrect letter guessed. 
i.e. in the order: head, body, left arm, right arm, left leg, right leg.
As such the user will have 6 tries to guess the word before the drawing is complete and they are hanged.
If the user successfully guesses the word before they run out of tries they win the game.
To assist the user, a hint is provided that words to be guessed in this game are animals.

- - -

## User Experience (UX)

### Initial Discussion

#### Key information:

### User Stories

#### Client Goals

#### First Time Visitor Goals

#### Returning Visitor Goals

#### Frequent Visitor Goals

- - -

## Design

### Colour Scheme
The term color module was used to print colored text.

Bright and bold colors were used throughout the game to draw the users attention.

Color consistancy is used in the below instances:
* Cyan is used largely when requesting user input.
* Magenta is used largely when the user's chosen name is called alongside text to draw their attention.
* Red is used largely when error messages are raised for invalid input.

### Graphics
* ASCII art was taken from [Texteditor](https://texteditor.com/gallery/)
* Hangman array was taken from [Invent with Python](https://inventwithpython.com/invent4thed/chapter8.html)

### Flowchart
Below is the initial design put together using [Lucid Chart](https://lucid.app/) to plan the logic of the game.

![Flowchart](docs/flowchart.png)

- - -

## Features

### Future features

- - -

## Technologies Used

### Languages Used
Python

### Frameworks, Libraries & Programs Used
* [Am I responsive?](https://ui.dev/amiresponsive) - to show website across a range of devices.
* Git - for version control. Using GitPod terminal to commit to Git and push to GitHub.
* GitHub - to save and store the code pushed from Git.
* [Lucid Chart](https://lucid.app/) - to create the flow chart.

- - -

## Testing 
Issues raised in my project meetings with my mentor [Chris Quinn](https://github.com/10xOXR) :

### Solved Bugs

### Known Bugs

### PEP8 
Testing carried out via [PEP8 Validator](https://pep8ci.herokuapp.com/):
* run.py - All clear, no errors found
* hangman.py - 6 messages showing for, invalid escape sequence '\ '. These do not seem to affect the functionality of the game.
* words.py - All clear, no errors found

### Manual Testing
* Tested responsiveness with the different dimensions in dev tools and via [Responsive design checker](https://responsivedesignchecker.com/).
* Tested website on mobile with [Chrome](docs/testing/manualtesting/chrome-mobile.jpg) & [Samsung internet](docs/testing/manualtesting/samsunginternet-mobile.jpg)
* Tested on tablet with [Amazon Silk browser](docs/testing/manualtesting/amazonsilkbrowser-tablet.png), laptop with [Microsoft Edge](docs/testing/manualtesting/microsoftedge-laptop.png) and desktop with [Microsoft Edge](docs/testing/manualtesting/microsoftedge-desktop.png).

- - -

## Deployment 

### Local Deployment

#### How to Clone
1. Sign up or log in to GitHub
2. Go to the repository https://github.com/Sarohia94/Project-3-Hangman
3. Go to the code dropdown and select how you'd like clone and copy the link provided
4. Go to the new repo and enter in your workspace terminal, "git clone" followed by the link copied

#### How to Fork
1. Sign up or log in to GitHub
2. Go to the repository https://github.com/Sarohia94/Project-3-Hangman
3. Click on the fork button towards the top right of the page 

### Remote Deployment
The website was deployed to GitHub Pages as follows:
1. Log in to GitHub
2. Assuming you have cloned or forked the repository, go on the "Settings" link for this repository
3. Click on the "Pages" link on the left hand side of the page
4. Under "Source" select "Deploy from branch" from the dropdown
5. Under "Branch" select "main" from the dropdown
6. Click "Save" which will then refresh the page
7. It might take a few mins before you can refresh and view the link to the site published

### Deploy project to Heroku
1. Sign up or log in to Heroku
2. Create a new Heroku app
3. Set the buildbacks to Python and NodeJS, in that order
4. Link the Heroku app to the repositry 
5. Click on Deploy

- - -

## Credits

### Code
* The [Invent with Python](https://inventwithpython.com/invent4thed/chapter8.html) tutorial helped break down how I could go about writing the code. I used this primarily to learn how to store and print correct and incorrect guesses. The hangman array was taken from this website too.
* The [How to build HANGMAN with Python in 10 MINUTES](https://www.youtube.com/watch?v=m4nEnsavl6w) was very useful as it gave me an overview on how to create a functioning minimum viable project. The code to update guesses to the underscores as they occur in the word was taken from this tutorial (run.py file, lines 218-223)
* Joshua from tutor support advised on how to best break my code down in to smaller functions. When I was initially splitting out my code into smaller functions I was passing 3 or more arguments and the structure wasn't as clean as it could be so I was running in to issues aplenty. Joshua was able to assist in directing me how I may want to organise the code given what I had written already.
* Oisin from tutor support for helping me work through the kinks in my code. It helped a lot in making me think differently on how I can investigate issues and how to make the most out of print statments to check my code. 
* [Chris Quinn](https://github.com/10xOXR), for helping me resolve and understand the error messages showing on gitpod. He also helped to resolve the issue where correct guesses were not displaying to the word. I followed his example in writing prnt statements with the line number of the code included. This really improved my ability to pin point where issues occur and what is being affected in the background. As such I was able to resolve subsequent issues on my own much faster.

### Content
* The content was written by the developer Amritpreet Sarohia.
* ASCII art was taken from [Texteditor](https://texteditor.com/gallery/)

### Acknowledgements 
Thank you to anyone taking the time to view my third project. Special thanks to the Slack community and the below individuals:
* [Chris Quinn](https://github.com/10xOXR), my mentor. Thank you for your guidance and feedback.
* To the tutors from tutor support for their help and assistance: Scott, Joshua and Oisin