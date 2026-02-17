* Settings *
Library    BuiltIn
Library    Process
Library    SeleniumLibrary

* Test Cases *
Verify Environment setup
    Log To Console    ===== Environment Verification Started =====

    # 1. Verify Python installation
    ${py_result}=    Run Process    python    --version
    Run Keyword If    '${py_result.stderr}' != ''    Fail    Python is not installed or not added to PATH
    Log To Console    Python Version: ${py_result.stdout}

    # 2. Verify Robot Framework installation
    ${rf_result}=    Run Process    robot    --version
    Run Keyword If    '${rf_result.stderr}' != ''    Fail    Robot Framework is not installed
    Log To Console    Robot Framework Version: ${rf_result.stdout}

    # 3. SeleniumLibrary import verification
    Log To Console    SeleniumLibrary imported successfully

    Log To Console    ===== Environment Verification Completed Successfully =====