Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [Browse Recipes Page](#browse-recipes-page)
  * [Recipe Detail Page](#recipe-detail-page)
  * [Add Recipe Page](#add-recipe-page)
  * [Update Recipe Page](#update-recipe-page)
  * [Confirm Delete Recipe Page](#confirm-delete-recipe-page)
  * [My Recipes Page](#my-recipes-page)
  * [My Bookmarks Page](#my-bookmarks-page)
  * [My Meal Plan Page](#my-meal-plan-page)
  * [Django All Auth Pages](#django-all-auth-pages)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
    + [Overwrite Meal Plan Items](#overwrite-meal-plan-items)
    + [Required fields using Summernote extension submit with just whitespace entered](#required-fields-using-summernote-extension-submit-with-just-whitespace-entered)
    + [No Reverse Match Error](#no-reverse-match-error)
    + [Cloudinary Images not Displaying](#cloudinary-images-not-displaying)
    + [Footer not staying at bottom of screen](#footer-not-staying-at-bottom-of-screen)
  * [Unfixed bugs:](#unfixed-bugs-)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## User Story Testing

### EPIC | User Profile

*As a Site User, I can register an account so that I can create, read, update and delete my lists and items.*

- A "Sign Up" button is prominently displayed on the landing page, serving as a clear call to action for users to begin their journey. Clicking this button redirects users to the sign-up page.
- Additionally, a "Sign Up" button is available in the header for easy access.

![header](docs/readme_images/features/call_out.png)


*As a Site User, I can log in or log out of my account so that I can keep my account secure.*

If the user has registered an account they can access the login and logout buttons in the Navbar.

![header](docs/readme_images/features/login_dropdown.png)


*As a Site User I can see my login status so that I know if I'm logged in or out.*

- Once the user has logged into their account, their username is displayed on the Navbar alongside a profile icon.

![header](docs/readme_images/features/logout_dropdown.png)


### EPIC | User Navigation

 *As a User I can immediately understand the purpose of the site so that I can decide if it meets my needs*

- In the center of the landing page, there is a section entitled with an information message that provides a brief overview of what the site has to offer. Additionally, there is a button labeled "Add list" to further emphasize the message.

![header](docs/readme_images/features/what_we_do.png)



*As a user, I can intuitively navigate around the site so that I can find content*

- A navigation bar is visible on every page of the site, which is fully responsive across different screen sizes.

![header](docs/readme_images/features/what_we_do.png)


*As a Site User, I can view which items belong to each list so that I don't misunderstand which items belong to which list.*

- The list page displays all lists in the database, initially filtered to show 'My lists' first, followed by other public lists.

![header](docs/readme_images/features/what_we_do.png)



### EPIC List management

*- As a Site User, I can create lists so that I can easily organize items.*
- Once the user has logged in, a create recipe button is immediately visible on the landing page as a call to action for the user to add a recipe. When the user clicks the button they are taken to the add recipe form.

![header](docs/readme_images/features/callout_logged_in.png)

![header](docs/readme_images/features/add_recipe.png)



*As a Site User, I can rename a list so that I don't need to delete and recreate a new list if I accidentally named it wrong*.

- The rename page is accessed from the edit list menu.
- Clicking the rename button displays the page to rename the list.


*As a Site User, I can delete lists so that I can remove ones that are no longer needed*

- The delete page is accessed from the edit list menu.
- Clicking the delete button displays the confirmation message page, allowing the user to confirm the deletion if needed.
- The deletion of the list is confirmed to the user with a confirmation page.


*As a Site User, I can view and copy an existing list created by another user so that I can reuse items in my own lists*

- By clicking on the edit button in the list view, the option to clone the list is displayed.
- Clicking on "Clone list" will display a page for entering a new name.
- After entering a new name and clicking "Clone list," the new list will be created.
- Confirmation message and the newly cloned list will be displayed as the final step

*As a Site User, I can set my lists to be private or public so that I can control whether I want to share my lists and letting other users adding items to my public list*

- When clicking on a list marked with the toggle switch positioned to the left and labeled as "public," the switch moves to the right position, and the text is updated from "public" to "private."
- When clicking on a list marked with the toggle switch positioned to the right and labeled as "private," the switch moves to the left position, and the text is updated from "private" to "public."
- After logging out and logging in again, I can confirm that the latest saved status (public or private) is correctly maintained.

*As a Site User, I can see how frequently my lists are copied, so that I can adapt and prioritize sharing lists that are most meaningful.*

- By viewing the "Clone Count" variable I will see number of the time the list has been cloned.
- By testing to clone a list I can see how the clone count increases by one for the list that was cloned.


### EPIC Item management

*As a Site User, I can save other users' recipes to my bookmarks so that I can find them easily at a later date.*
- Each recipe has a bookmark button which can be toggled by signed in users to bookmark the recipe or remove from bookmarks.




### EPIC | Site Administration
*As a Site Administrator, I can create, read, update and delete recipes, comments and meal plan items so that I can manage the app content*
-  Admins have full access to CRUD functionality for all recipes, comments and meal plans in the admin panel.

![header](docs/readme_images/features/admin_panel.png)


## Validator Testing

### HTML

All HTML pages were run through the [W3C HTML Validator](https://validator.w3.org/). See results in below table.

| Page                 | Logged Out | Logged In |
|----------------------|------------|-----------|
| add_recipe.html      | N/A        | Note 1    |
| base.html            | No errors  | No errors |
| browse_receipes.html | No errors  | No errors |
| delete_comment.html  | N/A        | No errors |
| delete_recipes.html  | N/A        | No errors |
| index.html           | No errors  | No errors |
| my_bookmarks.html    | N/A        | No errors |
| my_mealplan.html     | N/A        | No errors |
| my_recipes.html      | N/A        | No errors |
| paginator.html       | No errors  | No errors |
| recipe_detail.html   | No errors  | No errors |
| update_comment.html  | N/A        | No errors |
| update_recipe.html   | N/A        | Note 1    |
| login.html           | No errors  | N/A       |
| logout.html          | N/A        | No errors |
| signup.html          | No errors  | N/A       |
| 400.html             | No errors  | No errors |
| 403.html             | N/A        | No errors |
| 404.html             | No errors  | No errors |
| 500.html             | No errors  | No errors |

#### Note 1: Summernote Errors
When validating the Add Recipe and Edit Recipe forms I received a number of errors which were caused by the installed Summernote library which runs when using the form on these pages. I could not rectify these errors given that they weren't in my own code therefore they are unresolved. 

 <details>

 <summary>Summernote Errors</summary>

![Summernote Errors](docs/readme_images/summernote_errors.png)
 </details>

#### Fixed Errors
When validating the Recipe Detail page I received an error in relation to an extra `</p>` tag in the 'Recipe Method' field which had been created using the summernote editor. The issue was due to Summernote including `<p>` tags around the form field. I resolved the error by removing the surrounding `<p>` tags in my HTML when rendering a summernote field in my Recipe Detail page.

### CSS
No errors were found when passing my CSS file through the official [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

 <details>

 <summary>CSS</summary>

![CSS Validation](docs/readme_images/css_validation.png)
 </details>

### Javascript
No errors were found when passing my javascript through [Jshint](https://jshint.com/) 

<details>

<summary>Jshint</summary>

![Jshint](docs/readme_images/jshint_validation.png)
</details>

### Python
All Python files were run through [Pep8](http://pep8online.com/) with no errors found. 

### Lighthouse

Lighthouse validation was run on all pages (both mobile and desktop) in order to check accessibility and performance. At first I received the warning *'Background and foreground colors do not have a sufficient contrast ratio'* in relation to buttons where I had used the Bootstrap class `btn-info`. After I updated the button styling I received the below scores. 

| Page           | Performance  | Accessibility | Best Practices  | SEO |
|----------------|:------------:|:-------------:|:---------------:|:---:|
|                |              |               |                 |     |
| Desktop        |              |               |                 |     |
| Home           |          100 |           100 |             100 | 100 |
| Browse Recipes |           98 |           100 |             100 | 100 |
| Recipe Detail  |           99 |            99 |             100 | 100 |
| Add Recipe     |           99 |            98 |             100 | 100 |
| My Recipes     |           99 |           100 |             100 | 100 |
| My Bookmarks   |           99 |           100 |             100 | 100 |
| My Meal Plan   |           99 |           100 |             100 | 100 |
| Update Recipe  |           99 |            98 |             100 | 100 |
| Delete Recipe  |           99 |           100 |             100 | 100 |
| Update Comment |           99 |           100 |             100 | 100 |
| Delete Comment |           99 |           100 |             100 | 100 |
| Login          |           99 |           100 |             100 | 100 |
| Logout         |           99 |           100 |             100 | 100 |
| Signup         |           99 |           100 |             100 | 100 |
|                |              |               |                 |     |
| Mobile         |              |               |                 |     |
| Home           |           94 |           100 |             100 | 100 |
| Browse Recipes |           94 |           100 |             100 | 100 |
| Recipe Detail  |           93 |            98 |             100 | 100 |
| Add Recipe     |           86 |            98 |             100 | 100 |
| My Recipes     |           94 |           100 |             100 | 100 |
| My Bookmarks   |           95 |           100 |             100 | 100 |
| My Meal Plan   |           95 |           100 |             100 | 100 |
| Update Recipe  |           83 |            98 |             100 | 100 |
| Delete Recipe  |           94 |           100 |             100 | 100 |
| Update Comment |           94 |           100 |             100 | 100 |
| Delete Comment |           94 |           100 |             100 | 100 |
| Login          |           95 |           100 |             100 | 100 |
| Logout         |           95 |           100 |             100 | 100 |
| Signup         |           95 |           100 |             100 | 100 |

## Browser Testing
- The Website was tested on Google Chrome, Firefox, Safari browsers with no issues noted.
    
## Device Testing
- The website was viewed on a variety of devices such as Desktop, Laptop, iPhone 8, iPhoneXR and iPad to ensure responsiveness on various screen sizes in both portrait and landscape mode. The website performed as intended. The responsive design was also checked using Chrome developer tools across multiple devices with structural integrity holding for the various sizes.

## Manual Testing

### Site Navigation
| Element               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| NavBar                |            |                                                                    |           |
| Site Name (logo area) | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Browse Recipes Link   | Click      | Open Browse Recipes Page                                           | Pass      |
| Add Recipe Link       | Click      | Open Add Recipe Form                                               | Pass      |
| Add Recipe Link       | Display    | Only visible if user in session                                    | Pass      |
| My Meal Plan Link     | Click      | Open My Meal Plan page                                             | Pass      |
| My Meal Plan Link     | Display    | Only visible if user in session                                    | Pass      |
| My Account Dropdown   | Click      | Open My Account dropdown                                           | Pass      |
| My Account Dropdown   | Display    | Text changes to username with profile icon when user is in session | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| My Recipes Link       | Click      | Open My Recipes page                                               | Pass      |
| My Recipes Link       | Display    | Only visible if user in session                                    | Pass      |
| My Bookmarks Link     | Click      | Open My Bookmarks page                                             | Pass      |
| My Bookmarks Link     | Display    | Only visible if user in session                                    | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user in session                                    | Pass      |
| All Nav Links         | Hover      | lighten text                                                        | Pass      
|                       |            |                                                                    |           |
| Mobile View           |            |                                                                    |           |
| Hamburger Menu        | Responsive | Display when screen size reduces to medium size                       | Pass      |
| My Account Dropdown   | Responsive | Contents move into hamburger menu when screen size reduces to medium           | Pass      |
| Site Name (logo area) | Click      | Redirect to home                                                   | Pass      |
| Home Link             | Click      | Redirect to home                                                   | Pass      |
| Browse Recipes Link   | Click      | Open Browse Recipes Page                                           | Pass      |
| Sign Up Link          | Click      | Open Sign up page                                                  | Pass      |
| Sign Up Link          | Display    | Not visible if user in session                                     | Pass      |
| Log In Link           | Click      | Open Login page                                                    | Pass      |
| Log In Link           | Display    | Not visible if user in session                                     | Pass      |
| Add Recipe Link       | Click      | Open Add Recipe Form                                               | Pass      |
| Add Recipe Link       | Display    | Only visible if user in session                                    | Pass      |
| My Meal Plan Link     | Click      | Open My Meal Plan page                                             | Pass      |
| My Recipes Link       | Click      | Open My Recipes page                                               | Pass      |
| My Recipes Link       | Display    | Only visible if user in session                                    | Pass      |
| My Bookmarks Link     | Click      | Open My Bookmarks page                                             | Pass      |
| My Bookmarks Link     | Display    | Only visible if user in session                                    | Pass      |
| Logout Link           | Click      | Open logout confirm page                                           | Pass      |
| Logout Link           | Display    | Only visible if user in session                                    | Pass      |
|                       |            |                                                                    |           |
| Footer                |            |                                                                    |           |
| All links             | Click      | Open in new tab and to correct location                            | Pass      |

### Home Page
| Element               | Action  | Expected Result                 | Pass/Fail |
|-----------------------|---------|---------------------------------|-----------|
| Hero 'Sign Up' Button | Click   | Open Sign up page               | Pass      |
| Hero 'Sign Up' Button | Display | Not visible if user in session  | Pass      |
| Hero 'Create" Button  | Click   | Open Add Recipe page            | Pass      |
| Hero 'Create" Button  | Display | Only visible if user in session | Pass      |

### Browse Recipes Page
| Element     | Action                  | Expected Result                                                                         | Pass/Fail |
|-------------|-------------------------|-----------------------------------------------------------------------------------------|-----------|
| Recipe Card | Display correct content | Display correct image, recipe title and cooktime                                        | Pass      |
| Recipe Card | Click                   | Clicking anywhere inside the recipe card takes you to the correct recipe's detail page. | Pass      |
| Recipe Card | Pagination              | Site will paginate 8 recipe cards to a page                                             | Pass      |
| Recipe Card | Order                   | Recipes are sorted by newest to oldest                                                  | Pass      |
| Recipe Card | Hover                   | Add gold border                                                                         | Pass      |
### Recipe Detail Page

| Element                        | Action              | Expected Result                                                                                                         | Pass/Fail |
|--------------------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Recipe Content                 | Display             | Display correct recipe image, title, author, prep time, cook time, description, ingredients and method                  | Pass      |
| Add to Meal Plan button        | Click               | Meal Plan modal pops up                                                                                                 | Pass      |
| Add to Meal Plan button        | Display             | Button only visible if user in session                                                                                  | Pass      |
| Bookmark button (Outline)      | Click               | Clicking the outlined bookmark changes it to a solid bookmark                                                           | Pass      |
| Bookmark button (Outline)      | Click               | Recipe is added to the user's bookmarks page                                                                            | Pass      |
| Bookmark button (Outline)      | Click               | Success message appears informing the user that the recipe has been added to their bookmarks                            | Pass      |
| Bookmark button (Outline)      | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Bookmark button (Solid)        | Click               | Clicking the solid bookmark changes it back to an outlined bookmark                                                     | Pass      |
| Bookmark button (Solid)        | Click               | Recipe is removed from the user's bookmarks page                                                                        | Pass      |
| Bookmark button (Solid)        | Click               | Success message appears informing the user that the recipe has been removed from bookmarks                              | Pass      |
| Bookmark button (Solid)        | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Bookmark button                | Display             | Button only visible if user in session                                                                                  | Pass      |
| Update recipe button           | Click               | Opens Update Recipe Form                                                                                                | Pass      |
| Update recipe button           | Display             | Button only visible if user is the author                                                                               | Pass      |
| Delete recipe button           | Click               | Opens Delete Recipe confirmation page                                                                                   | Pass      |
| Delete recipe button           | Display             | Button only visible if user is the author                                                                               | Pass      |
| User Comments                  | Display             | Displays correct name date time and comment body                                                                        | Pass      |
| User Comments                  | Display             | Comments are ordered oldest to newest                                                                                   | Pass      |
| Update comment button          | Display             | Button only visible if user is the comment author                                                                       | Pass      |
| Update comment button          | Click               | Opens Update Comment Form                                                                                               | Pass      |
| Update comment form            | Leave empty         | On submit: form won't submit                                                                                            | Pass      |
| Update comment form            | Leave empty         | Error message displays                                                                                                  | Pass      |
| Update comment submit button   | Click               | Form submit - page updates and comment displays in comments section with correct content                                | Pass      |
| Update comment submit button   | Click               | Success message appears informing the user that the comment has been updated                                            | Pass      |
| Update comment submit button   | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Update comment form            | Access              | If a user tries to edit another user's comment (by changing the url) they receive a 403 error.                          | Pass      |
| Update comment form            | Access              | If a user tries to edit a comment (by changing the url) without being signed in they are redirected to the login page   | Pass      |
| Delete comment button          | Display             | Button only visible if user is the comment author                                                                       | Pass      |
| Delete comment button          | Click               | Opens delete comment confirmation page                                                                                  | Pass      |
| Confirm delete button          | Click               | Comment is removed from comment section                                                                                 | Pass      |
| Confirm delete button          | Click               | Success message appears informing the user that the comment has been deleted                                            | Pass      |
| Confirm delete button          | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Confirm delete button          | Click               | Redirect user back to recipe page                                                                                       | Pass      |
| Cancel delete button           | Click               | Redirect user back to recipe page                                                                                       | Pass      |
| Delete comment                 | Access              | If a user tries to delete another user's comment (by changing the url) they receive a custom 403 error.                 | Pass      |
| Delete comment                 | Access              | If a user tries to delete a comment (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Add comment Form               | Display             | Form only visible if user in session                                                                                    | Pass      |
| Add comment Form submit button | Leave empty               | On submit: form won't submit                                                                                            | Pass      |
| Add comment Form submit button | Leave empty               | Error message displays                                                                                                  | Pass      |
| Add comment Form submit button | Filled in               | Form submit - page updates and comment displays in comments section with correct content                                | Pass      |
| Add comment Form submit button | Click               | Success message appears informing the user that the comment has been added                                              | Pass      |
| Add comment Form submit button | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
|                                |                     |                                                                                                                         |           |
| Meal plan model                |                     |                                                                                                                         |           |
| Modal cancel button            | Click               | Close modal                                                                                                             | Pass      |
| Days drop down menu            | Click               | Display list of the days of the week                                                                                    | Pass      |
| Days drop down menu            | Click               | Default day is Monday                                                                                                   | Pass      |
| Add to Meal Plan submit button | Click               | Form Submit                                                                                                             | Pass      |
| Add to Meal Plan submit button | Click               | Correct recipe is added to the user's Meal Plan page for the correct day                                                | Pass      |
| Add to Meal Plan submit button | Click               | Success message appears telling the user that the recipe has been added to their meal plan                              | Pass      |
| Add to Meal Plan submit button | Click               | Success message fades after 3 seconds                                                                                   | Pass      |
| Add to Meal Plan submit button | Click               | If meal plan item already exists for that day, the success message tells the user that meal plan has been updated       | Pass      |
| Add to Meal Plan submit button | Click               | Modal closes                                                                                                            | Pass      |
| Meal Plan modal                | Click outside modal | Close modal                                                                                                             | Pass      |
### Add Recipe Page
| Element                       | Action                | Expected Result                                                                                                     | Pass/Fail |
|-------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------|-----------|
| Add Recipe                    | Access                | If a user tries to add a recipe (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Form Text Input (if required) | Leave blank           | On Submit: Warning appears, form won't submit                                                                       | Pass      |
| Form Text Input (if required) | Just input whitespace | On Submit: Form won't submit                                                                                        | Pass      |
| Recipe Title                  | Duplicate Entry       | On Submit: Warning appears, form won't submit                                                                       | Pass      |
| Form image select button      | Click                 | Open device storage                                                                                                 | Pass      |
| Form image select button      | Display               | Chosen image name displayed once selected                                                                           | Pass      |
| Form image select button      | Display               | Default image is used if no image is selected                                                                       | Pass      |
| Cancel button                 | Click                 | Redirect to Browse Recipes page                                                                                     | Pass      |
| Add Recipe button(form valid) | Click                 | Form submit                                                                                                         | Pass      |
| Add Recipe button(form valid) | Click                 | Redirect to Recipe detail page for new recipe with all information displaying correctly                             | Pass      |
| Add Recipe button(form valid) | Click                 | Success message appears informing the user that the recipe has been created                                         | Pass      |
| Add Recipe button(form valid) | Click                 | Success message fades after 3 seconds                                                                               | Pass      |
### Update Recipe Page
| Element            | Action  | Expected Result                                                                                                         | Pass/Fail |
|--------------------|---------|-------------------------------------------------------------------------------------------------------------------------|-----------|
| Update Recipe      | Access  | If a user tries to edit another user's recipe (by changing the url) they receive a custom 403 error. (forbidden access) | Pass      |
| Update Recipe      | Access  | If a user tries to edit a recipe (by changing the url) without being signed in they are redirected to the login page    | Pass      |
| Update Recipe Form | Display | Form has all the fields filled out with the original content                                                            | Pass      |
| Update Button      | Click   | Updated recipe is saved                                                                                                 | Pass      |
| Update Button      | Click   | Success message appears telling the user that the recipe has been successfully updated                                  | Pass      |
| Update Button      | Click   | Success message fades after 3 seconds                                                                                   | Pass      |
| Update Button      | Click   | User is redirected back to the current recipe page                                                                      | Pass      |
| Cancel Button      | Click   | User is redirected back to the current recipe page                                                                      | Pass      |
### Confirm Delete Recipe Page
| Element       | Action | Expected Result                                                                                                        | Pass/Fail |
|---------------|--------|------------------------------------------------------------------------------------------------------------------------|-----------|
| Delete recipe | Access | If a user tries to delete another user's recipe (by changing the url) they receive a custom 403 error.                 | Pass      |
| Delete recipe | Access | If a user tries to delete a recipe (by changing the url) without being signed in they are redirected to the login page | Pass      |
| Delete Button | Click  | Recipe is deleted and removed from user recipes page                                                                   | Pass      |
| Delete Button | Click  | Success message appears telling the user that the recipe has been successfully deleted                                 | Pass      |
| Delete Button | Click  | User is redirected back to the My recipes page                                                                         | Pass      |
| Cancel Button | Click  | Redirect to current recipe page                                                                                        | Pass      |

### My Recipes Page
| Element         | Action               | Expected Result                                                                                                  | Pass/Fail |
|-----------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| My Recipes Page | Access               | If a user tries to access this page (by changing url) without being signed in they are redirected to the Login page | Pass      |
| My Recipes Page | Display              | Only displays the recipes that the user is the author for                                                        | Pass      |
| Recipe Card     | Show Status          | Show if recipe is draft                                                                             | Pass      |
| Recipe Card     | Card Content Display | Display correct image, recipe title and cooktime                                                                 | Pass      |
| Recipe Card     | Click                | Clicking anywhere inside the recipe card takes you to the correct recipe's detail page.                          | Pass      |
| Recipe Card     | Pagination           | Site will paginate 8 recipe cards to a page                                                                      | Pass      |
| Recipe Card     | Order                | Recipes are sorted by newest to oldest                                                                           | Pass      |
| Recipe Card     | Hover                | Display gold border                                                                                              | Pass      |
### My Bookmarks Page

| Element           | Action               | Expected Result                                                                                                  | Pass/Fail |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| My Bookmarks Page | Access               | If a user tries to access this page (by changing url) without being signed in they are redirected the Login page | Pass      |
| My Bookmarks Page | Display              | Only the recipes the user has book marked are shown                                                              | Pass      |
| Recipe Card       | Card Content Display | Display correct image, recipe title and cook time                                                                | Pass      |
| Recipe Card       | Click                | Clicking anywhere inside the recipe card takes you to the correct recipe's detail page.                          | Pass      |
| Recipe Card       | Pagination           | Site will paginate 8 recipe cards to a page                                                                      | Pass      |
| Recipe Card       | Order                | Recipes are sorted by newest to oldest                                                                           | Pass      |
| Recipe Card       | Hover                | Display gold border                                                                                              | Pass      |
### My Meal Plan Page
| Element           | Action               | Expected Result                                                                                                  | Pass/Fail |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------|-----------|
| My Meal Plan Page | Access               | If a user tries to access this page (by changing url) without being signed in they are redirected the Login page | Pass      |
| Meal Plan card    | Order                | Cards are ordered from Monday to Sunday                                                                          | Pass      |
| Meal Plan card    | Card Content Display | If populated: Display correct image, recipe title                                                                | Pass      |
| Meal Plan card    | Card Content Display | If unpopulated: display placeholder image and 'Add Recipe'                                                       | Pass      |
| Meal Plan card    | Click                | If populated: clicking anywhere inside the recipe card takes you to the detailed page for that recipe            | Pass      |
| Meal Plan card    | Click                | If unpopulated:  clicking anywhere inside the recipe card takes you to the browse recipes page                   | Pass      |
| Meal Plan card    | Hover                | Display gold border                                                                                              | Pass      |

### Django All Auth Pages
| Element                    | Action                                    | Expected Result                            | Pass/Fail |
|----------------------------|-------------------------------------------|--------------------------------------------|-----------|
| Sign Up                    |                                           |                                            |           |
| Log in link                | Click                                     | Redirect to login page                     | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert correct format                     | On submit: form submit                     | Pass      |
| Username field             | Insert duplicate username                 | On submit: form won't submit               | Pass      |
| Username field             | Insert duplicate username                 | Error message displays                     | Pass      |
| Email field                | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Email field                | Insert incorrect format                   | Error message displays                     | Pass      |
| Email field                | Insert correct format                     | On submit: form submit                     | Pass      |
| Email field                | Leave empty                               | On submit: form submit                     | Pass      |
| Email field                | Insert duplicate email                    | On submit: form won't submit               | Pass      |
| Email field                | Insert duplicate email                    | Error message displays                     | Pass      |
| Password field             | Insert incorrect format                   | On submit: form won't submit               | Pass      |
| Password field             | Insert incorrect format                   | Error message displays                     | Pass      |
| Password field             | Passwords don't match                     | On submit: form won't submit               | Pass      |
| Password field             | Passwords don't match                     | Error message displays                     | Pass      |
| Password field             | Insert correct format and passwords match | On submit: form submit                     | Pass      |
| Sign Up button(form valid) | Click                                     | Form submit                                | Pass      |
| Sign Up button(form valid) | Click                                     | Redirect to home page                      | Pass      |
| Sign Up button(form valid) | Click                                     | Success message confirming login appears   | Pass      |
| Sign Up button(form valid) | Click                                     | Success message fades after 3 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log in                     |                                           |                                            |           |
| Sign up link               | Click                                     | Redirect to sign up page                   | Pass      |
| Username field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Username field             | Leave empty                               | Error message displays                     | Pass      |
| Username field             | Insert wrong username                     | On submit: form won't submit               | Pass      |
| Username field             | Insert wrong username                     | Error message displays                     | Pass      |
| Password field             | Leave empty                               | On submit: form won't submit               | Pass      |
| Password field             | Leave empty                               | Error message displays                     | Pass      |
| Password field             | Insert wrong password                     | On submit: form won't submit               | Pass      |
| Password field             | Insert wrong password                     | Error message displays                     | Pass      |
| Login button(form valid)   | Click                                     | Form submit                                | Pass      |
| Login button(form valid)   | Click                                     | Redirect to home page                      | Pass      |
| Login button(form valid)   | Click                                     | Success message confirming login appears   | Pass      |
| Login button(form valid)   | Click                                     | Success message fades after 3 seconds      | Pass      |
|                            |                                           |                                            |           |
| Log Out Confirmation       |                                           |                                            |           |
| Logout button              | Click                                     | Redirect to homepage                       | Pass      |
| Logout button              | Click                                     | Success message confirming log out appears | Pass      |
| Logout button              | Click                                     | Success message fades after 3 seconds      | Pass      |

## Bugs 

### Fixed Bugs

- #### Overwrite Meal Plan Items
     - **Bug**: When I initially wrote the code to add a recipe to a meal plan item, if a meal plan item already existed for the current user for a particular day and then they added another recipe to that day, the meal plan item wouldn't update and the user's meal plan would still display the original meal plan item for that day.
     - **Fix**: in order to rectify this I queried the database to return all meal plan items for the current user and for the day selected. Through an if statement I could then check if a meal plan item already existed for the user for that day, and if it did then to overwrite it. 
This solved the problem whereby now if a user adds a meal plan item to a particular day, it just overwrites the previous meal plan item. 

- #### Required fields using Summernote extension submit with just whitespace entered
     - **Bug**: In the Add Recipe form, the Ingredients and Method fields both use the summernote extension. Both fields are required fields however the form still submitted when only whitespace was entered due to summernote rendering the html `<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>` on submit and therefore the form validation didn't pick up the empty field. 
     - **Fix**: My first attempt at the solution was to write a custom django `clean_<fieldname>() method` which would replace any `&nbsp` with blank, `strip()` whitespace and `strip_tags()`. The solution did prevent the form submitting with only whitespace however it wasn't a good solution due to fact that stripping the HTML tags meant the summernote editor didn't format valid inputs as expected. 
     - After posting the question on Slack Ian Meigh_5P proposed a working solution to create a custom validator for textfields and implement this in the Model. I have utilised Ian's custom validator in my code [here](eateasy/validators.py) and have credited him in my Readme. Thanks Ian!

- #### No Reverse Match Error
     - **Bug**: When I first implemented the Add Recipe form I kept getting a no reverse match error when trying to submit a new recipe due to the slug field not populating properly. 
     - **Fix**: After some research on stack overflow I learned about AutoSlugField which is a Django Model Field extension which will automatically create a unique slug and you can choose which field to populate the slug from. Utilising this extension I was able to create a unique slug populated from the recipe title.

- #### Cloudinary Images not Displaying
     - **Bug**: Cloudinary images not displaying after uploading. 
     - **Fix**: After searching the issue on slack I realised that I needed to include enctype="multipart/form-data in the opening form HTML tag and this solved the problem. 

- #### Footer not staying at bottom of screen
     - **Bug**: Footer not staying at the bottom of the screen when displaying on pages without fullscreen content and didn't want to use a sticky footer. 
     - **Fix**: Was able to utilise the calc() CSS function and make the page content 100% of the viewport height less the height of the footer and this solved the problem. 

### Unfixed bugs:
There are no known unfixed bugs. 