# Presentalk
## Inspiration 
We wanted to make it easier to navigate presentations. Handheld clickers are useful for going to the next and last slide, but they are unable to skip to specific slides in the presentation. Also, we wanted to make it easier to pull up additional information like maps, charts, and pictures during a presentation without breaking the visual continuity of the presentation. To do that, we added the ability to search for and pull up images using voice commands, without leaving the presentation. 


## What it does
Presentalk solves this problem with voice commands that allow you to  move forward and back, skip to specific slides and keywords, and go to specific images in your presentation using image recognition. 
Presentalk recognizes voice commands, including:
* Next slide
  * Increments the slide number
* Last slide
  * Decrements the slide number
* Go to slide #
  * Goes to a specific slide number
* Go to slide with the *picture* 
  * Uses computer vision to go to a specific picture in the presentation
* Go to the slide titled __
  * Goes to the first slide containing __ in the title
* Search for __
  * Parses the text of each slide for a matching phrase
* Show me __
  * Pulls up an image of __ using a Google custom search engine
  * For example, a teacher might realize they are missing a map or diagram from their presentation, and use the "Show me" command to pull up an example
* Zoom in to __
  * zooms in to an image

## How we built it
* We wrote the backend of the app - speech recognition, pdf downloading and extraction, and parsing - in Python
* We use Flask and json to publish the current slide (and sometimes image urls) to a server
* We use AJAX to pull the data from the server
* We use JS to display the slides


## Challenges we ran into
* Getting voice commands to work accurately and fast
* Requesting permission for and using a mic through the browser


## Accomplishments that we're proud of
* Easy voice commands for moving forward, backwards, and to specific slide numbers
* Using image recognition to move to a slide with a specific image


## What's next for Presentalk
We need to request microphone access through the browser, and use that as the audio stream. After that, we will be able to publish Presentalk as a website.