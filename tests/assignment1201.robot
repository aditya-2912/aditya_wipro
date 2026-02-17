* Settings *
Library    BuiltIn

* Variables *
${USERNAME}      RobotUser
${ENV}           Test
@{NUMBERS}       10    20    30    40

* Test Cases *
Log Scalar Variables
    [Documentation]    Demonstrates scalar variables and logging
    Log    Username is ${USERNAME}
    Log    Environment is ${ENV}
    Log To Console    Running test for ${USERNAME} in ${ENV} environment

Log List Variables
    [Documentation]    Demonstrates list variables and logging
    Log    Numbers list is: ${NUMBERS}
    Log To Console    First number is ${NUMBERS}[0]
    Log To Console    Second number is ${NUMBERS}[1]