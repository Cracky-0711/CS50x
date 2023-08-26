# Task Management Tool
#### Video Demo:  <https://youtu.be/zZpV8mKvX0o>
#### Description: The following text was translated from Japanese to English using the translation tool DeepL.
#### We have created a web application to manage tasks. Below is a description of what each file does.
#### The first file is app.py. app.py describes the process of moving from one page to another because we used the Flask framework.
#### First, the database model is defined. The database has two tables, User and Task, and the User table stores ID, username, password, and salt. password is a hashed version of the password set by the user, and the salt used to hash it is also stored in the Task table. In the Task table, id, title, deadline, status, and user_id are stored to distinguish which task belongs to which user. The process of navigating to the page of each HTML file is described in the HTML description.
#### Next, the HTML files in the templates folder will be described in order.
#### base.html
#### This file contains the header and footer descriptions common to all pages, as well as the description of the top page.
#### The header menu is created using ul and li tags. I also wanted to write an explanation of how to use my site on the top page, so I used p tags and img tags to display text and images.
#### signup.html
#### This is a signup page using "form". username and password are entered by the user. when the Signup button is pressed, the signup function in app.py is called. If it does not exist, it returns an error. If it does not exist, it hashes the password with the hash_password function and stores the username, hashed password, and the solt used for hashing in the database.
#### login.html
#### This is a login page using the form. login function calls the login function of app.py when the login button is clicked. stored in the database, and checks if it matches the hashed password stored in the database. If it matches, the login_user function is executed and the login status is saved.
#### index.html
#### The tasks added by the logged-in user are listed. The filter function at the top of the page is written in Javascript. script.js contains the code to switch between "flex" and "none" in CSS when a checkbox is checked. Javascript is also used for the hamburger button on the right side of each task. When clicked, it switches between css block and none. Clicking the Delete button in the menu that appears when the hamburger button is pressed calls the delete function in app.py and deletes the task's information from the database.
#### add_task.html
#### This is a page for adding a task using the form, which prompts the user to enter the task name and deadline, and when the Add button is pressed, calls app.py's add_task function to add the new task's information to the database.
#### edit_task.html
#### This is a page for modifying task information using the form, allowing the user to change the Task name, Deadline, and Condition, and when the Save changes button is pressed, it calls the edit_task function in app.py, and replaces the information stored in the database in the database is rewritten to the one after the changes are made.
#### Finally, the static folder is explained.
#### The script.js is explained for each function in the description of each HTML file, so we will skip it here.
#### The images folder contains the header image and images used in Toppage (base.html).
#### styles.css contains CSS that is applied to all HTML. There may be descriptions that are not necessary because I sometimes changed tags in the HTML afterward. I have not done any elaborate design.
#### This concludes the description of my web application.
