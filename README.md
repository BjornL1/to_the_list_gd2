# TO THE LIST

TheList is a website whichs primary goal is to empower users with functionality for tracking, sharing, and editing shopping items. Additionally, the platform is well-suited for planning activities, including managing to-do tasks. 


The live link can be found here - [The Easy Eater](https://tothelist-gd-20bd5040c185.herokuapp.com/)

![Colour Palette](docs/readme_images/site_mockup.png)
## Table of Contents

- [TO THE LIST](#to-the-list)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
      - [EPIC | User Profile](#epic--user-profile)
      - [EPIC | User Navigation](#epic--user-navigation)
      - [EPIC | Recipe Management](#epic--recipe-management)
      - [EPIC | Recipe Interaction](#epic--recipe-interaction)
      - [EPIC | Mealplan Management](#epic--mealplan-management)
      - [EPIC | Site Administration](#epic--site-administration)
      - [User stories not yet implemented](#user-stories-not-yet-implemented)
    - [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  - [Agile Methodology](#agile-methodology)
  - [Data Model](#data-model)
  - [Testing](#testing)
  - [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
    - [Custom error pages:](#custom-error-pages)
  - [Features](#features)
    - [Header](#header)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [User Account Pages](#user-account-pages)
    - [Browse Recipes](#browse-recipes)
    - [Recipe Detail Page](#recipe-detail-page)
    - [Add Recipe Form](#add-recipe-form)
    - [Update Recipe Form](#update-recipe-form)
    - [Delete Recipe](#delete-recipe)
    - [My Meal Plan](#my-meal-plan)
    - [My Recipes Page](#my-recipes-page)
    - [My Bookmarks Page](#my-bookmarks-page)
    - [Error Pages](#error-pages)
    - [Future Features](#future-features)
  - [Deployment - Heroku](#deployment---heroku)
    - [Create the Heroku App:](#create-the-heroku-app)
    - [Attach the Postgres database:](#attach-the-postgres-database)
    - [Prepare the environment and settings.py file:](#prepare-the-environment-and-settingspy-file)
    - [Create files / directories](#create-files--directories)
    - [Update Heroku Config Vars](#update-heroku-config-vars)
    - [Deploy](#deploy)
  - [Forking this repository](#forking-this-repository)
  - [Cloning this repository](#cloning-this-repository)
  - [Languages](#languages)
  - [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  - [Credits](#credits)
  - [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
## User Experience (UX)

## User Experience (UX)

A typical user of ToTheList is someone who wants to efficiently manage their shopping lists and facilitate seamless sharing with family and friends, allowing others to contribute and update items collaborativel

### User Stories

#### EPIC User Profile
- As a Site User, I can register an account so that I can create, read, update and delete my lists and items.
- As a Site User, I can log in or log out of my account so that I can keep my account secure.
- As a Site User I can see my login status so that I know if I'm logged in or out.

#### EPIC User Navigation
- As a Site User, I can immediately understand the purpose of the site so that I can decide if it meets my needs.
- As a Site User, I can intuitively navigate around the site so that I can find content and understand where I am on the site.
- As a Site User, I can view which items belong to each list so that I don't misunderstand which items belong to which list.

#### EPIC Lists interaction
- As a Site User, I can create lists so that I can easily organize items.
- As a Site User, I can rename a list so that I don't need to delete and recreate a new list if I accidentally named it wrong.
- As a Site User, I can delete lists so that I can remove ones that are no longer needed.
- As a Site User, I can view and copy an existing list created by another user so that I can reuse items in my own lists.
- As a Site User, I can set my lists to be private or public so that I can control whether I want to share my lists and letting other users adding items to my public list.
- As a Site User, I can see how frequently my lists are copied, so that I can adapt and prioritize sharing lists that are most meaningful. 

#### EPIC Items interaction
- As a Site User, I can add and view items to a list so that I can easily store and find my items.
- As a Site User, I can rename an item so that I don't need to delete and recreate a new item if I accidentally named it wrong.
- As a Site User, I can delete items so that I can remove ones that are no longer needed.
- As a Site User, I can duplicate an item so that I can reuse the name and quantity and quickly create a similar item which can easily be adapted if needed instead of creating a new one.
- As a Site User, I can add/delete/rename my items added to other users' public lists so that I can easily share my items with other users.

#### EPIC Site Administration
- As a Site Administrator, I can create, read, update and delete lists and items.

#### User stories not yet implemented

The following user stories were scoped out of the project due to time constraints and labelled as "Won't Have" on the project board on Github. It is intended that these user stories will be implemented at a later date. 

- As a Site User, I can move items between different lists.
- As a Site User, I can search and filter lists.

### Design

The site's intentionally simple and clean design reflects its overarching goal: to cultivate a serene and organized environment that aligns with its purpose. By embracing minimalism, it aims to evoke a sense of tranquility and provide users with a clutter-free space conducive to efficient organization.

#### Colour Scheme
Colour palette from Coolors

![Colour Palette](docs/readme_images/colour_scheme.png)

The colour scheme of the site is mainly pale cream, pink and brown with thin gold borders. The colours chosen are quite neutral and calming. 

Great care was taken to establish a good contrast between background colours and text at all times to ensure maximum user accessibility. 

#### Imagery
The site features a singular static image, portraying a wall adorned with lists, effectively accentuating the site's core purpose.

#### Fonts
The Montserrat font is the main font used for the body of the website with the Playfair Display font used for the main headings on the home page. These fonts were imported via Google Fonts. Sans Serif is the backup font, in case for any reason the main font isn't being imported into the site correctly.

#### Wireframes

<details>

 <summary>Landing Page</summary>

![Landing Page](docs/wireframes/landing_wireframe.png)
</details>

<details>

<summary>Browse Recipes</summary>

![Browse Recipes](docs/wireframes/browse_wireframe.png)
</details>


<details>

<summary>Add Recipe</summary>

![Add Recipe](docs/wireframes/addrecipe_wireframe.png)
</details>

<details>

<summary>My Recipes</summary>

![My Recipes](docs/wireframes/myrecipes_wireframe.png)
</details>

<details>

<summary>My Bookmarks</summary>

![My Bookmarks](docs/wireframes/mybookmarks_wireframe.png)
</details>

## Agile Methodology

Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/AliOKeeffe/PP4_My_Meal_Planner/projects/2)

The 5 Epics listed above were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone(Epic). Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

## Data Model
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  

Django AllAuth was used for the user authentication system.

In order for the users to create recipes a custom recipe model was required. The recipe author is a foreign key to the User model given a recipe can only have one author.

The Comment model allows users to comment on individual recipes and the Recipe is a foreign key in the comment model given a comment can only be linked to one recipe. 

The meal plan item model allows users to add recipes to a meal plan for a particular day. A meal plan item can only have one user and one recipe and is therefore linked to the User and Recipe models through foreign keys.

The diagram below details the database schema.

![Database Schema](docs/readme_images/database_schema.png)

## Testing

Testing and results can be found [here](/TESTING.md)

## Security Features and Defensive Design

### User Authentication

- Django's LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page. 
- Django's UserPassesTestMixin is used to limit access based on certain permissions i.e. to ensure users can only edit/delete recipes and comments for which they are the author. If the user doesn't pass the test they are shown an HTTP 403 Forbidden error.

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error. 

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database and this was set up before the first push to Github.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

## Features

### Home Page

- The homepage comprises several key features and pieces of information designed to enhance user interaction:

Logo: Positioned prominently, the logo serves as a visual identifier for the platform, fostering brand recognition and trust.

Header: The navigation bar in the header offers intuitive access to various sections and functionalities of the platform, ensuring seamless user experience and easy exploration.

Add List Button: A prominent call-to-action button invites users to initiate list creation swiftly. Placed strategically, this button encourages immediate engagement and facilitates the creation of new lists.

Homepage Information: Informative content provides users with an overview of the platform's features and benefits. This information aims to orient users, helping them understand the platform's value proposition and encouraging further exploration.

![header](docs/readme_images/homepage.png)


### Header

**Logo**
- The logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

**Navigation Bar**

- The navigation bar is consistently located at the top of every page, providing users with convenient access to various sections and functionalities of the platform. Depending on whether the user is logged in or not, the header will dynamically display different links, offering tailored navigation options.

- On smaller screens, such as mobile devices, the header links are concealed under a hamburger button. Upon clicking this symbol, the links are revealed, allowing users to easily navigate through the platform's content.

The header offers various options, including: Home, Learn, Register, Login, Logged in as, and Logout.
- 'Home' provides easy access to the homepage.
- 'Learn' offers a site description and instructions for users.
- 'Register' presents a signup form for creating a new account.
- 'Login' directs users to the sign-in page.
- 'Logout' provides a sign-out option for users to log out of their accounts.
- 'Logged in as:' displays the name of the currently logged-in user.

***Logged-out user***

- The header displays the following options: 'Home', 'Learn', 'Register', and 'Login'.


![header](docs/readme_images/header_logged_out.png)

***Logged-in user***

- The header displays the following options: 'Home', 'Learn', 'Logout', and 'Logged in as:'.

![header](docs/readme_images/header_logged_in.png)

### Footer

![header](docs/readme_images/footer.png)

- The footer section includes links to Facebook, Instagram, Twitter and Youtube.
- Clicking the links in the footer opens a separate browser tab to avoid pulling the user away from the site.


### User Account Pages

**Sign Up**

![header](docs/readme_images/signup.png)

**Log In**

![header](docs/readme_images/signin.png)

**Log Out**

![header](docs/readme_images/signout.png)

- Django allauth was installed and used to create the Sign up, Log in and Log out functionality. 

### Lists
All lists include the following information: Name, Number of Items (quantity), Status of Items (Done or Not Done), and Public/Private or External status, along with an edit/clone button. Their presentation and options depend on whether the user owns the list or not. All lists owned by the logged-in user will be displayed first under the heading 'My Lists,' while public lists owned by other users are displayed under 'Other Lists'."

For a logged-in user, the following information will be presented for all lists (owned by either the logged-in user or other users):

- Name: Name of the list.
- Created by: The owner of the list.
- Clone Count: Displays how many times the list have cloned by other users.
- Number of Items: Number of items added to the list.
- Status of Items: Whether an item has been marked as done or not.

For lists owned by the logged-in user, the following additional information will be displayed:

- Public/Private: For each list, a toggle switch displays the status of the list.
- Public lists are shared lists visible to any logged-in user.
- Private lists are only visible and editable by the logged-in user.
- Edit button: This button leads to an editing page where the user can choose to clone, rename, or delete the list, or access the items that belong to the list.

For public lists shared by other users, the following additional information will be displayed to the logged-in user:
- External: A text indicating that it belongs to another user.
- Clone button: This button allows the logged-in user to clone the list.

**My Lists**

If the logged-in user has created lists, they will be displayed at the top of the page.
If the user adds items to the list, they will be linked under the card and will be scrollable directly below the card.
In the example below, a list has been cloned once. It contains 2 items, one of which has been marked as done, indicated by "1/2" in the card. The list is set to "public," and the edit button is visible since the logged-in user owns the list. 

![header](docs/readme_images/lists.png)


**Other lists**

- This page displays all private and private and public lists owned by the logged in user.
- The user's own lists will be displayed under the header "My Lists."
- Lists owned by the logged-in user will display the following information: Name, Number of Items (quantity), Status of Items (Done or Not Done), and Public/Private status.
- Name: Name of the list.
- Number of Items: Number of items added to the list.
- Status of Items: Whether an item has been marked as done or not.
- Public/Private: For each list, a toggle switch displays the status of the list.
- Public lists are shared lists visible to any logged-in user. 
- Private lists are only visible and editable by the logged-in user.
- Edit button: The button will lead to an editing page where the user can choose to either clone, rename, or delete the list or - access the items that belong to the list.


### Recipe Detail Page
**Recipe Header Section**

### Error Pages

Custom Error Pages were created to give the user more information on the error and to guide them back to the site.

![header](docs/readme_images/features/403_error.png)

- 400 Bad Request - The Easy Eater is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - The Easy Eater is currently unable to handle this request

### Future Features
The following user stories were scoped out of the project due to time constraints and labelled as "Could Have" on the project board in Github. It is intended that these user stories will be implemented at a later date. 

- As a Site User, I can export the ingredients from the recipes on my meal plan to a shopping list and remove the ones that are not necessary so that I can have all my required ingredients for the week in one place.
- As a Site User, I can search and filter recipes so that I can find the one I want.
Searching and filtering

Other potential features include:
- Adding extra categories on the Meal Plan Item for breakfast, lunch, dinner and snacks so the user can plan out their meals for the full day rather than just for dinner.
- Adding vegan and vegetarian labels to the recipe so the user can filter by these options.

## Deployment - Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

### Create the Heroku App:
- Log in to [Heroku](https://dashboard.heroku.com/apps) or create an account.
- On the main page click the button labelled New in the top right corner and from the drop-down menu select "Create New App".
- Enter a unique and meaningful app name.
- Next select your region.
- Click on the Create App button.

### Attach the Postgres database:
- In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.
- Copy the DATABASE_URL located in Config Vars in the Settings Tab.

### Prepare the environment and settings.py file:
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file. 
- Update the settings.py file to import the env.py file and add the SECRETKEY and DATABASE_URL file paths.
- Comment out the default database configuration.
- Save files and make migrations.
- Add Cloudinary URL to env.py
- Add the cloudinary libraries to the list of installed apps.
- Add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
- Link the file to the templates directory in Heroku.
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list the format ['app_name.heroku.com', 'localhost']

### Create files / directories
- Create requirements.txt file
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following: web: gunicorn project-name.wsgi

### Update Heroku Config Vars
Add the following Config Vars in Heroku:
- SECRET_KEY value 
- CLOUDINARY_URL
- PORT = 8000
- DISABLE_COLLECTSTATIC = 1

### Deploy
- NB: Ensure in Django settings, DEBUG is False
- Go to the deploy tab on Heroku and connect to GitHub, then to the required repository. 
- Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
- Click View to view the deployed site.

The site is now live and operational.
## Forking this repository
- Locate the repository at this link [The Easy Eater](https://github.com/AliOKeeffe/PP4_My_Meal_Planner).
- At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
- A copy of the repository is now created.

## Cloning this repository
To clone this repository follow the below steps: 

1. Locate the repository at this link [The Easy Eater](https://github.com/AliOKeeffe/PP4_My_Meal_Planner). 
2. Under **'Code'**, see the different cloning options, HTTPS, SSH, and GitHub CLI. Click the prefered cloning option, and then copy the link provided. 
3. Open **Terminal**.
4. In Terminal, change the current working directory to the desired location of the cloned directory.
5. Type **'git clone'**, and then paste the URL copied from GitHub earlier. 
6. Type **'Enter'** to create the local clone. 

## Languages

- Python
- HTML
- CSS
- Javascript

## Frameworks - Libraries - Programs Used
- [Django](https://www.djangoproject.com/): Main python framework used in the development of this project
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create the user accounts
- [PostgreSQL](https://www.postgresql.org/) was used as the database for this project.
- [Heroku](https://dashboard.heroku.com/login) - was used as the cloud based platform to deploy the site on.
- [Responsinator](http://www.responsinator.com/) - Used to verify responsiveness of website on different devices.
- [Balsamiq](https://balsamiq.com/) - Used to generate Wireframe images.
- [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) - Used for overall development and tweaking, including testing responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) - Used for icons in information bar.
- [GitHub](https://github.com/) - Used for version control and agile tool.
- [Google Fonts](https://fonts.google.com/) - Used to import and alter fonts on the page.
- [W3C](https://www.w3.org/) - Used for HTML & CSS Validation.
- [PEP8 Online](http://pep8online.com/) - used to validate all the Python code
- [Jshint](https://jshint.com/) - used to validate javascript
- [Coolors](https://coolors.co/) - Used to create colour palette.
- [Favicon](https://favicon.io/) - Used to create the favicon.
- [Lucidchart](https://lucid.app/documents#/dashboard) - used to create the database schema design
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md
- [Summernote](https://summernote.org/): A WYSIWYG editor to allow users to edit their posts
- [Techsini](https://techsini.com/multi-mockup/index.php) - Site mockup generator
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) used to manage Django Forms
- [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/): CSS Framework for developing responsiveness and styling
- [Hatchful](https://hatchful.shopify.com/): Used to generate custom logo
- [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to convert excel testing tables to markdown

## Credits

- [W3Schools](https://www.w3schools.com/)
- [Django Docs](https://docs.djangoproject.com/en/4.0/)
- [Bootstrap 4.6 Docs](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- [Stack Overflow](https://stackoverflow.com/)
- [Pexels](https://www.pexels.com/): All imagery on the site was sourced from Pexels.com
- [BBC Goodfood](https://www.bbcgoodfood.com/): All recipe content was sourced from BBC Goodfood.
- [Update View](https://pytutorial.com/django-updateview-example)
- [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/#using-paginator-in-a-view)
- [AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)
- [Code Institute - Blog Walkthrough Project](https://github.com/Code-Institute-Solutions/Django3blog)
- [Ian Meigh - Custom Validator function](eateasy/validators.py)

## Acknowledgments

Many thanks to my mentor Antonio for his support and advice. Thanks to 
The Code Institute slack community for their quick responses and very helpful feedback in particular Ian Meigh.

