# DevOps Core Fundamental Project Specification
## PantryPal
This repository contains my submission for the QA DevOps Core Fundamental Project Specification: a CRUD Recipe application called PantryPal. 
<br>
## Contents:
* [Project Brief](#Project-Brief)
* [Database Design](#Database_Design)
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [Project Management](#Project-Management)
* [The App](#The-App)
* [Updates](#Updates)
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)
 <br>
 
 ### Project Brief: 
 
 <br>
  This project required us to draw on a wide variety of knowledge and skills. We were expected to imlpement project management both in theory and in practice through the use of project management/progress tracking software (jira in the case of this project). Coding the MVP required technical knowledge of Python, Flask and MySQL. Lastly,an understanding of Git and of Pytest were needed, for mainting a VCS (version control system) and for unit testing the application, respectively. 
 We were expected to work alone, with the exception of some help from an instructor upon request. The application could relate to any theme of our choosing, as long as it satisfied the CRUD criteria and utilised at least two tables with a relationship in a database.
 <br>
 Some requirements of the original project brief have been set aside for future work as they were not possible to integrate, either because of the time frame changes or changes to the teaching schedule. These include: CI/CD pipeline elements, integration testing and use of virtual machines. 
 <br>
 
 ### Databse Design:
 
  <br>
 I chose to build a recipe application because I am a passionate cook (as you may have seen on my github profile page). It was also one of the first ideas that came to mind when tasked with creating a CRUD app. One can easily picturea website on which a user may upload their own recipes, make ammendments to those recipes, relete recipes and read the recipes of others! Such a web application is relatively easy to imagine, even if you are unsure of the intricate workings behind the scenes, as I was as a newcomer to all of these technologies. 
 <br>
 I started trying to make sense of the aformentioned intricacies by designing an ERD for my database:
 <br>
 
![ERD](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/main/Figures/ERDPantryPal%20copy.png)

<br>

The database contains three tables: a Recipes table, which has a one-to-many relationship with two other tables, Ingredients and Instructions. This allows for each recipe to be associated with any number of instructions, steps and ingredients. 

 ### Risk Assessment:
 
 ![Risk Assessment](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Risk-Assessment.png)
 
 <br>
 
 The above risk assessment outlines the details of possible hazards that may be encountered by either the developer or the user of this web application. 
 These risks were taken into consideration during the development of this app and they influenced the design of this MVP. For example, I chose not to allow the user to create an account which would allow them extra user priveledges on the app, as it was too risky to send login credentials over an unsecured HTTP connection. Likewise, Flask and SQLAlchemy were used to prevent SQL commands from being sent directly to the database. Also, in the development process, all confidential credentials  Database_uri and Sectrey_Key) were exported as variables to the terminal to prevent a data leak on Github.
 
 <br>

 
 ### Testing:
 ### Project Management:
 ## The App: 
 ### Updates:
 ### Known Issues:
 ### Future Work:
