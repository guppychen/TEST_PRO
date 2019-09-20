*** Settings ***
Resource          ./base.robot
*** Test Cases ***
    
case add
    ${d}    add    ${n}    ${m}
    log    ${d}
    log to console    ${d}