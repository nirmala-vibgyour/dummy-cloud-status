# To check the status of a dummy aws cloud configured via the AVI LB APIs

## Script uses the following libs.
- requests
- urllib3
- os
- dotenv

## Endpoints
 
 -  **Login**
   - `POST /login`
   - Body:
     ```json
     {
       "username": "admin",
       "password": "root@123"
     }
     ```
   - Used to authenticate and retrieve `sessionid` and `csrftoken`.

 - **Create Cloud**
   - `POST /api/cloud`
   - Body:
     ```json
     {
       "name": "aws-cloud-nirmalawrk",
       "vtype": "CLOUD_AWS",
       "aws_configuration": {
         "access_key_id": "AKIAEXAMPLEDUMMY1234",
         "secret_access_key": "dUMmySeCrEtKeY1234567890abcDEF4567890abcd",
         "region": "ap-south-1",
         "vpc_id": "vpc-dummy123",
         "availability_zones": ["ap-south-1a"]
       }
     }
     ```
    - Headers:
        - Content-Type: application/json
        - Cookie: {{sessionid}}
        - X-CSRFToken: {{csrftoken}}
        - X-Avi-Version: 30.2.3
        - Referer: https://35.200.176.139/
        - X-Avi-Tenant: admin
        - Cookies were added to the request, including both sessionid and csrftoken.

 - **Verify Cloud Status**
   - `GET /api/cloud/<cloud-uuid>/status`
   - No body required.
   - UUID from the response of the above api
   - Headers: same as in the above
   - Cookies: same as in the above


## Below are done using Postman
- Logged in to the Avi controller using `POST /login`.
- Created a dummy AWS cloud using `POST /api/cloud` with dummy credentials and region.
- Verified the cloud’s status using `GET /api/cloud/<uuid>/status`. (automated with the script)