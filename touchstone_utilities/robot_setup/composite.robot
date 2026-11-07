#
#  requirements:
#        robotframework-requests==0.7.0
#
#
#
#


*** Settings ***
Library    RequestsLibrary
Library    Collections


*** Variables ***
${HOST}                         http://172.16.227.48/api/v2
# ${HOST}                         http://127.0.0.1:5000/api/v2
${USERNAME}                     admin
${PASSWORD}                     Touch@dmin123
${TEAM}                         553ccbcf-c300-11e6-812a-766d78a9d835
${USAGE_MODE}                   Custom Config Mode


*** Keywords ***
setup touchstone session
  Create Session                touchstone_admin           ${HOST}

set proper headers
  ${HEADERS}=                   Create Dictionary          Accept=application/json, text/plain, */*    Content-Type=application/json    team=${TEAM}    usageMode=${USAGE_MODE}
  [Return]    ${HEADERS}

do admin login
  # POST Request for Login
  ${HEADERS}=                   set proper headers
  ${LOGIN_CREDS}=               Create Dictionary          login=${USERNAME}    passwd=${PASSWORD}
  ${response}=                  Post Request               touchstone_admin     login    headers=${HEADERS}    data=${LOGIN_CREDS}
  [Return]    ${response}

do environment listing
  # GET Request for OpenStack environments
  ${login_response}=            do admin login
  ${HEADERS}=                   set proper headers
  Set To Dictionary             ${HEADERS}  token  ${login_response.json()['token']}
  Remove From Dictionary        ${HEADERS}  Content-Type
  ${response}=                  Get Request             touchstone_admin    os/environments    headers=${HEADERS}
  [Return]    ${response}

do admin logout
  # DELETE Request for Logout
  ${login_response}=            do admin login
  ${HEADERS}=                   set proper headers
  Set To Dictionary             ${HEADERS}  token  ${login_response.json()['token']}
  Remove From Dictionary        ${HEADERS}  Content-Type
  ${response}=                  Delete Request             touchstone_admin    login    headers=${HEADERS}
  [Return]    ${response}

api ${received_response} should be ${expected_response}
  Should be equal as strings    ${received_response.status_code}    ${expected_response}



*** Test Cases ***
Do a valid login
  setup touchstone session
  ${response}=    do admin login
  api ${response} should be 201

List environments
  setup touchstone session
  ${response}=    do environment listing
  Log  ${response.json()}
  api ${response} should be 200

Do logout
  setup touchstone session
  ${response}=    do admin logout
  api ${response} should be 204
