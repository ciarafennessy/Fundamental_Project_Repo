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
* [Known Issues](#Known-Issues)
* [Future Work](#Future-Work)
 <br>
 
 ### Project Brief: 
 
 <br>
  This project required us to draw on a wide variety of knowledge and skills. We were expected to imlpement project management both in theory and in practice through the use of project management/progress tracking software (jira in the case of this project). Coding the MVP required technical knowledge of Python, Flask and MySQL. Lastly, an understanding of Git and of Pytest were needed, for mainting a VCS (version control system) and for unit testing the application, respectively. 
 We were expected to work alone, with the exception of some help from an instructor upon request. The application could relate to any theme of our choosing, as long as it satisfied the CRUD criteria and utilised at least two tables with a relationship in a database.
 <br>
 Some requirements of the original project brief have been set aside for future work as they were not possible to integrate, either because of time frame changes or changes to the teaching schedule. These include: CI/CD pipeline elements, integration testing and the use of virtual machines. 
 <br>
 
 ### Database Design:
 
  <br>
 I chose to build a recipe application because I am a passionate cook (as you may have seen on my Github profile page). It was also one of the first ideas that came to mind when tasked with creating a CRUD app. One can easily picture a website on which a user may upload their own recipes, make ammendments to those recipes, delete recipes and read the recipes of others! Such a web application is relatively easy to imagine, even if you are unsure of the intricate workings behind the scenes, as I was as a newcomer to all of these technologies. 
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
 These risks were taken into consideration during the development of this app and they influenced the design of this MVP. For example, I chose not to allow the user to create an account which would allow them extra user priveledges on the app, as it was too risky to send login credentials over an unsecured HTTP connection. Likewise, Flask and SQLAlchemy were used to prevent SQL commands from being sent directly to the database. Also, in the development process, all confidential credentials  (Database_URI, Sectrey_Key) were exported as variables to the terminal to prevent a data leak on Github.
 
 <br>

 
 ### Testing:
 
 <br>
 Unit testing was the only kind of testing used on this project thus far, in the future I would also like to implement integration testing and to automate the testing process via Jenkins. Unit tests were written for the create, read, update and delete aspects of the app. The figure below shows how all tests have passed through Pytest, with a 99% coverage report.
 
 ![Pytest](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/pytest_covreport.png)
 
 <br>
 
 ### Project Management:
 
 <br>
 To track the progress of this project I chose to use Jira to help maintain an Agile workflow. Below you can see the roadmap I set out for myself. I broke the project into three separate sprints (mostly to help familiarise myself with how Jira works). The first sprint concentrated on brainstorming and the initial setup, the second focused on database configuration. The third sprint was where the bulk of the work was done, I split it into three epics: MVP creation, Testing and Documentation. Each epic contained multiple user stories with multiple child issues. I gave every issue a story point and time estimate. 
 
 ![Roadmap](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Roadmap.png)
 
 <br>
 Below you can see the Burnup and Cumulative Flow diagrams produced by Jira for my final sprint. They do not follow an ideal pattern, this is for two reasons. Firstly, being new to Jira, I added many of the issues just after I had started the sprint, not knowing that it would affect the insights feature. Secondly, when I created the sprint the projected deadline for this project was two days later than what the final deadline turned out to be. Nonetheless, I am still happy with my choice of Jira over a simple Kanban board as I have learned a lot from using it for this project and I believe it will be the most applicable project management tool for my career after I finish my training. 
 
 
 ![Burnup](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/main/Figures/Burnup-report.png)
 
 ![Cumulative Flow](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/main/Figures/Cumulative%20flow%20diagram.png)
 
 ## The App: 
  <br>
 
 ![home](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Home.png)
 
 <br>
 
 The user is first presented with a home page. The nav bar provides the user with all essential links. To add or view a recipe the user must only click upon the respective link. If they click on 'Add a Recipe' they will be brought to this page:
 
 
 ![Add Recipe](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Add_Recipe.png)
 
 <br>
 Here, the user may add in the title, time and servings related to the recipe they want to add to the web application. Clicking submit redirects them to this page:
 
 ![Add Ingredients](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Add_Ingredients.png)
 
 <br>
 The user may add as many ingredients as the recipe requires. Each time they submit a new ingredient they will be redirected back to the same page to submit another. There is no need to select the recipe that the ingredients belong to every time, as the select box is set to display the last recipe added as the default. When they have added all their ingredients they may click the link to move onto adding instructions to their recipe; which brings them here:
 
 ![Add Instructions](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Add_Instructions.png)
 
 <br>
 As before, the user may fill in as many steps and instructions as the recipe requires. When they are satisfied, they can navigate to the Recipes page where they will find their recipe added to the list of recipes on the site.
 
 ![Recipes](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Recipes.png)
 
 <br>
 Here, they can click the link below the recipe name to find the recipe outlined in full.
 
 ![Recipe1](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Recipe-1.png)
 
 ![Recipe2](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Recipe-2.png)
 
 <br>
 The user can view the recipe with ease and even make adjustments to it. The 'rewrite ingredients' link deletes the ingredient list and redirects the user to the <add ingredients> page so that they can input the ingredient entries again. The 'update instructions' hyperlink exists for every instruction in each recipe, when clicked it redirects the user to the below page.
 
  ![Update Instructions](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Update%20Instruction.png)
 
 Here, the user may overwrite the database entry for the original instruction with an ammended version, clicking submit redirects the user back to the recipe page they were originally on.
 <br>
 As an alternative to finding their recipe among the list on the Recipes page, the user may click the Select Recipe option in the nav bar and select a recipe from the drop-down list. This select feature allows the user to narrow down their search by hovering over the list and typing the first few letters of the recipe they're looking for, this highlights the recipe beginning with those letters in the list.
 <br>
 
 ![Select Recipe1](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Select-Recipe1.png)
 
 
 ![Select Recipe2](https://github.com/ciarafennessy/Fundamental_Project_Repo/blob/Development/Figures/Select-Recipe2.png)
 
 <br>
 
### Known Issues:
 
 <br>
 
 * There is nothing to prevent dublicate recipes, steps or instructions. 
 * The rewrite ingredients option is a little clunky - however, I chose this over having a hyperlink beside every ingredient in every recipe in order to update an individual ingredient. 
<br>
 
 ### Future Work:
 
 <br>
I would like to add a search function that allows users to search recipes by the ingredients they contain
 <br>
As a stretch goal, it would be nice to implement a login system that limits users to being able to update/delete their own recipes only. The login system would also offer other opportunities for advancement, like the ability to save recipes to a personal "favourites" list.

 
 test
 
