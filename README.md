# Awwwards-Clone 

## Api Documentation
### Get Requests
/api-overview/ - api overview and api links
/api/profiles/ - returns all the profiles in the system database
/api/<user_id>/profile - returns a specific user profile
/api/projects/ - gets all projects
/api/<user_id>/projects/ - gets all the projects of a specific user
/api/project/<pk> - returns a specific project

### Post Requests
(requires logged in user)
/api/create-profile/ - Posts a new profile for a user
/api/update-profile/ - Updates the user profile
/api/create/project/ - Creates a project object
/api/update/project/<pk> - Update project data
/api/delete/project<pk> - deletes project instance given

## About
This is a project where you can post projects and have them rated and reviewed by other users.

## Tech used 
- html
- css
- js
- python(django)

## User Stories
Login to be able to do everything apart from the site preview.

### Author
[Reilly](https://github.com/Reilly-Oduory)
