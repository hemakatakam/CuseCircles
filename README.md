## Cuse Circles - A Django Application

Users can explore existing circles, join them, and create their own to learn and collaborate with others.

### Getting Started

**Prerequisites:**

* Python 3.x
* pipenv (Install with `pip install pipenv`)
* Git (Optional, for cloning the repository)

**Instructions:**

1. **Clone the Repository (if using GitHub):**
   ```bash
   git clone https://github.com/your_username/learning_circles.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd learning_circles
   ```

3. **Set Up the Virtual Environment:**
   ```bash
   pipenv shell
   ```

4. **Install Dependencies:**
   ```bash
   pipenv install
   ```

5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

This will start the Django development server at `http://127.0.0.1:8000/`. You can access the application in your web browser.


### Development Phases

This project was developed in a phased approach:

**Phase 1: Basic Functionality**

- Project named `learning_circles` with an app called `circles`
- Model named `Circle` to represent learning circles
- Views for displaying all circles (home page)
- Templates for displaying information on the home page

**Phase 2: User Authentication**

- Implemented user login and signup using Django's built-in functionalities
- Created views and templates for signup and login

**Phase 3: Circle Management**

- Implemented creating, joining, and leaving circles for logged-in users
- Forms for collecting user input when creating circles
- Updated templates to display functionalities for logged-in users

**Phase 4: Styling and Design**

- Integrated Bootstrap for navigation bar, responsiveness, and basic styling
- Created logo and favicon for the application
- Implemented additional styling using CSS

**Phase 5 (To Be Implemented)**

- User profiles with additional information like interests and memberships
- Search functionality on the home page to find circles by keywords

**Phase 6 (To Be Implemented)**

- Dedicated circle pages with detailed information and member lists
- Communication channels using Slack API integration

**Phase 7 (To Be Implemented)**

- Recommendation service suggesting circles based on user interests and existing subscriptions

