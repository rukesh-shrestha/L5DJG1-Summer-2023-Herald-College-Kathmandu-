# Blog Application Summer Django Class
#### L5DJG1 - Summer 2023 - Herald College Kathmandu 

To download and use the projecct in your local machine. Follow the below mention steps:
- Clone the Project
  - If the SHH is not set in your local machine and github you can go with option 1 otherwise option 2.
    - Option 1
      ```
      git clone https://github.com/rukesh-shrestha/group2Django.git summerproject
      ```
    - Option 2

      ```
      git clone git@github.com:rukesh-shrestha/group2Django.git summerproject
      ```
- Setup the Environment
  - Go to the folder
    
    ```
    cd summerproject
    ```
  - Create the virtual environment
    - You can create the virtualenv with virtualenv library or the pythonenv.
      - You can click [here](https://pypi.org/project/virtualenv/) for the documentation to know about the virtual environment.
      - You can also skip this project can go with the installing the library step.
    - Installing the library
      - Install from requirements.txt
        
        ```
        pip install -r requirements.txt
        ```
    - setting up the environment variables
      - In the root project create the .env file.
      - You can open the project with VS code to create the file.
          
      ```
      code summerproject
      ```
      -  Populate the file with below variables
         - SECRET_KEY=YOUR-SECKET-KEY
         - DATABASE=YOUR-DATABASE-URL
         - EMAIL_HOST_USER=YOUR-EMAIL
         - EMAIL_HOST_PASSWORD=PASSWORD-EMAIL
         - EMAIL_PORT=EMAIL-PORT
         - DEFAULT_FROM_EMAIL=YOUR-EMAIL
        
          
- Run the project
  - Migrate the databas
    
    ```
    python manage.py migrate
    ```
  - Run server
    
    ```
    python manage.py runserver
    ```
  - Nagivate to the localhost and enjoy 


# Main Feature
- User Management System.
- Dynamic Email Sending.
- CRUD operation for the Blog.

# Want to Collaborate
- You can add new feature, push to the new branch and send the pull request. 
      
  
