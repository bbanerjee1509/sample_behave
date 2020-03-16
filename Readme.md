# Python Behave Demo on API Testing
A Project to demonstrate how python-behave framework can be used to verify any API functionality

## OMDB API
OMDB API is an open movie data search API which can is our product under test for this demo
`http://www.omdbapi.com/`
The OMDb API is a RESTful web service to obtain movie information, all content and images on the site are contributed and maintained by our users.
This Open API needs to have a registration for a user for non-production purpose which will provide
an API key for each user.
Sample request: 
```buildoutcfg
http://www.omdbapi.com/?t=Friends&apikey=9534a8be
```
where we are searching information about 'Friends' as t=<> where t stands for 'title of the movie/show'

## Background on File Structure
1. There is a feature file which is written in Gherkin Language(Given/When/Then/And). These are normally created under
`<project_root>/features` directory
2. There is a step definition file, which has step definitions for each test steps mentioned. These are
normally created under `<project_root>/steps` directory
3. Finally there is the glue code written in python which runs the underground logic to verify the features

## Installation and execution
1. Download and Install Python 3+ from `https://www.python.org/downloads/`
2. Install git bash from `https://gitforwindows.org/`
3. Clone the git repo by opening the git bash as administrator
`https://github.com/bbanerjee1509/sample_behave.git`
4. Go to the folder open_movie_api. `cd open_movie_api` from git bash command line
5. Run the command `pip3 install -r requirements.txt`
7. Then run the command `behave`
