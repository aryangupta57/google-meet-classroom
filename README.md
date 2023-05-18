# Google Meet Automation : Classroom
To conduct online classes on Google Meet this web-app set-ups meeting automatically, records chat, analytics and provides bot commands

## Requirements

- Python 3
- Flask
- Selenium
- Pandas
- Chrome web browser and respective Chrome driver

```
Flask==2.0.1
pandas==1.3.0
selenium==4.4.0
```

## Installation

1. Download the chrome driver according to your chrome browser version from https://chromedriver.chromium.org/downloads.
1. Add the path to the chrome driver in <b>```constants.py```</b>
1. Install the required python libraries 

## Usage
After installing the required run ```app.py```
- Go to `localhost:5000` - Enter username and password
- Now the meet will be setup automatically and each students/meet particiapnts chat activity will be recorded and analysed
- To stop the meet enter ```!stop``` in the chatbox
