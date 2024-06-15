**Medical Blog Management System**

**Overview**

-The Medical Blog Management System is a Django-based web application designed to manage user authentication, blog posts, and user-specific dashboards for doctors and patients. 
- The system includes functionalities for user registration (signup), login, blog post creation, and displaying blog posts.
- This README file provides an overview of the project structure, functionalities, and steps to run the project locally.

**Project Structure**
The project comprises several Django views that handle user interactions and display the appropriate templates. Here's a brief overview of each view and its purpose:

**Views**

**Login Page (login_page):**

- Handles user login based on the credentials provided.
- Differentiates between doctors (superusers) and patients (regular users) and redirects them to their respective home pages.
- Patient Signup Page (patient_signup_page):
- Allows patients to create an account.
- Checks for duplicate usernames and emails.


**Doctor Signup Page (doctor_signup_page):**

- Allows doctors to create an account (superuser).
- Checks for duplicate usernames and emails.


**Doctor Home Page (doctor_home_page):**

- Displays the home page for doctors.


**Patient Home Page (patient_home_page):**

- Displays the home page for patients.


**Blog Post Page (blog_post_page):**

- Allows users to create and upload blog posts.
- Users can select a category, add a summary, and decide if the post should be a draft.


**Display Blog Page (display_blog_page):**

- Displays all blog posts.


**Blog List Page (blog_list_page):**

- Displays a list of published blog posts.
- Shows all available categories.


**Templates**

The project uses HTML templates to render the web pages for various functionalities. Key templates include:

- login.html: Login page template.
- patient_signup.html: Patient signup page template.
- doctor_signup.html: Doctor signup page template.
- doctor_home.html: Doctor home page template.
- patient_home.html: Patient home page template.
- upload_blog.html: Blog post creation page template.
- view_blog.html: Blog display page template.
- blog_list.html: Blog list page template.


**Models**

**CustomUser:**

- Extended Django User model to include additional fields such as address, lane, city, state, pincode, and profile picture.


**BlogPost:**

- Model representing a blog post with fields for title, image, category, summary, content, and draft status.


**BlogCategory:**

- Model representing blog categories.


**Installation Setup**

**Prerequisites**

- Python 3.x or above
- Django
- Other dependencies listed in **requirements.txt**


**Steps to Run the Project**

- Clone the Repository:
    git clone <repository-url>
    cd <repository-directory>
      
- Create and Activate a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

- Install Dependencies:
    pip install -r requirements.txt

- Apply Migrations:
    python manage.py makemigrations
    python manage.py migrate
  
- Create a Superuser:
    python manage.py createsuperuser

- Run the Development Server:
    python manage.py runserver
  
- Access the Application:
    Open a web browser and go to http://127.0.0.1:8000.
