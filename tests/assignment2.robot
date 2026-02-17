* Settings *
Library    SeleniumLibrary

* Variables *
${URL}      https://tutorialsninja.com/demo/
${BROWSER}  chrome

* Test Cases *
Form Interaction Using BuiltIn Keywords
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    Click Element    xpath=//a[@title='My Account']
    Click Link       Register

    # Text Box
    Input Text    id=input-firstname    John
    Input Text    id=input-lastname     Doe
    Input Text    id=input-email        john${RANDOM}@mail.com
    Input Text    id=input-telephone    9876543210

    # Password fields
    Input Text    id=input-password     Test@123
    Input Text    id=input-confirm      Test@123

    # Radio Button (Newsletter = No)
    Click Element    xpath=//input[@name='newsletter' and @value='0']

    # Check Box (Privacy Policy)
    Click Element    name=agree

    # Built-in keyword: Run Keyword If
    Run Keyword If    'Test@123'=='Test@123'    Log    Passwords match

    # Built-in keyword: Sleep
    Sleep    3s

    # Submit form
    Click Button    xpath=//input[@type='submit']

    # Validation
    Page Should Contain    Your Account Has Been Created!
    Should Be Equal    ${TRUE}    ${TRUE}

    Close Browser