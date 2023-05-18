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

##
![vlcsnap-2023-05-18-23h47m16s235](https://github.com/aryangupta57/google-meet-classroom/assets/133975847/b624c8cd-2f69-447f-9e1b-9774208b6197)
![vlcsnap-2023-05-18-23h47m41s593](https://github.com/aryangupta57/google-meet-classroom/assets/133975847/353b5ae9-51e0-4da4-8ea2-6605f3ffe4d0)
![vlcsnap-2023-05-18-23h51m10s518](https://github.com/aryangupta57/google-meet-classroom/assets/133975847/23a81e27-8edf-4a52-8da6-9a16a3f390c1)
![vlcsnap-2023-05-18-23h48m13s563](https://github.com/aryangupta57/google-meet-classroom/assets/133975847/d1ba7f96-ad1c-4211-9c92-81f850dcb009)
