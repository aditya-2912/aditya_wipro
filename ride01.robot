*** Settings ***
Library           SeleniumLibrary

*** Keywords ***
Open Application
        Open Browser    https://www.google.com    chrome
        Maximize Browser Window

*** Test Cases ***
firstfile.robot
        Open Application
        Title Should Be    Google
        Close Browser
