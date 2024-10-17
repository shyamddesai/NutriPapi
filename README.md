# NutriPapi

Introducing NutriPapi: Your Personalized Health Companion
![NutriPapi Logo](docs/NutriPapi_logo.png)

NutriPapi is an innovative health management platform designed to empower users in achieving their wellness goals effortlessly. With AI-powered meal recommendations, personalized health tracking, and secure data handling, NutriPapi serves as a comprehensive solution for anyone looking to improve their dietary habits and overall well-being.

## Key Features
- **Personalized Health Tracking**: Users can input health metrics (e.g., weight, height, activity level) and dietary preferences, enabling NutriPapi to provide custom caloric intake recommendations.
- **AI-Powered Recipe Recommendations**: Using scikit-learn, NLP, and clustering algorithms, NutriPapi’s recommendation engine learns from user likes/dislikes and suggests meals based on available ingredients.
- **Ingredient-Based Meal Planning**: Input ingredients on hand, and NutriPapi will create meal plans suited to dietary preferences and nutritional goals.
- **Progress Tracking and Reports**: Log daily meals, track calories, and receive weekly progress updates.
- **Security and Privacy**: NutriPapi prioritizes user data security with robust authentication and encryption protocols.

## Technical Overview
- **Frontend**: Built with Next.js for a responsive user interface.
- **Backend**: Powered by Django and SQLite, supporting secure data handling and efficient storage.
- **Machine Learning**: Utilizes scikit-learn for decision trees, k-means clustering, and NLP techniques (e.g., tokenization) to personalize meal suggestions.
- **Agile Development**: Managed using SCRUM methodology and GitHub Projects, featuring four-week sprints and task management by the SCRUM master.

---

## Installation and Setup
### Backend Setup
1. **Create and activate a virtual environment**:
   ```bash
   python -m venv nutripapi
   cd Backend
   .\nutripapi\Scripts\Activate  # On Windows

   # On MacOS/Linux:
   cd .nutripapi/bin && source activate
   ```
2. **Install dependencies**:
   ```bash
   pip install -r .\requirements.txt  # On Windows
   python3 -m pip install -r requirements.txt  # On MacOS/Linux
   ```
3. **Run the server**:
   ```bash
   python .\manage.py runserver
   ```

### React Frontend Setup
1. **Navigate to the React frontend**:
   ```bash
   cd reactfront
   ```
2. **Install dependencies and start the application**:
   ```bash
   npm install
   npm run start
   ```

### Database Migrations
1. **Apply migrations**:
   ```bash
   cd Backend
   python manage.py makemigrations
   python manage.py migrate
   ```

### Acceptance Tests
1. **Run acceptance tests**:
   ```bash
   cd Backend
   python manage.py test
   ```

### Cucumber Tests
1. **Run Cucumber tests**:
   ```bash
   cd Backend
   python .\manage.py behave .\features\US0XX.feature
   ```
  
---

## Agile Development
NutriPapi is developed using Agile methodologies, anchored in SCRUM for iterative development, continuous feedback, and adaptive planning. The process begins with a comprehensive product backlog in GitHub Projects, which guides feature development, user stories, and technical tasks.

Each four-week sprint starts with a collaborative selection of user stories from the backlog, outlining the features to be implemented. Throughout the sprint, developers use GitHub for version control and collaboration, creating branches, reviewing code, and merging updates according to best practices.

Our release pipeline integrates GitHub for source control, unit and acceptance tests, and project documentation, with GitHub Actions facilitating continuous integration. Team coordination involves weekly online meetings, daily scrums on Microsoft Teams, and key meetings at sprint milestones. Project documentation is maintained on GitHub Wiki, with updates shared via Microsoft Teams and WhatsApp. The scrum master ensures progress alignment by maintaining a weekly task list within GitHub for project tracking and issue resolution.

### SCRUM Masters
- Sprint A: Shyam Desai, shyam.desai@mail.mcgill.ca
- Sprint B: Shyam Desai, shyam.desai@mail.mcgill.ca

### Team Members
- Masa Kagami <br>
- Martin Eskaros <br>
- Shyam Desai <br>
- Victor Micha <br>
- Yuting Li <br>
- Simon Cao <br>
- Ahmed Nami <br>
- Simiao Rao <br>
- Jingyi Wang <br>
- Simo Benkirane <br>

### Done Checklist
- [ ] All story related tasks have been completed.
- [ ] All of a story’s code in integrated into the main source code (i.e. merged into the
master branch).
- [ ] All of a story’s code has been peer reviewed and accepted.
- [ ] All known bugs have been reviewed and documented. Any bugs which block
acceptance tests from passing have been corrected.
- [ ] Unit tests have been written and run and succeed as part of the build process.
- [ ] All previous automated unit tests still succeed.
- [ ] Code builds successfully.
- [ ] All story specific acceptance tests succeed.
- [ ] All story normal and alternate flow story tests are automated and run as part of the
build process.
- [ ] All previous automated story tests still succeed.
- [ ] Any story specific non functional acceptance criteria pass.

---

## Requirements
### User Requirements:
- The NutriPapi system shall allow the user to be able to create an account 
- The NutriPapi system shall allow the user to input their target weight, current weight, height, weekly physical activity
- The NutriPapi system shall allow the user to get a daily suggested caloric intake according to their target/current weight and for how long they want to gain or lose weight
- The NutriPapi system shall allow the user to input the ingredients that they have in the fridge
- The NutriPapi system shall allow the user to set their dietary preferences in the profile (such as vegetarian, vegan, lactose intolerant, no nuts, etc.) to filter out the ingredients from the suggested meals
- The NutriPapi system shall allow the user to set and update their personal information eg weight, height, gender, weight goals
- The NutriPapi system shall allow the user to access and log their meal history 
- The NutriPapi ​system shall allow users to delete the accounts they created.

### System Requirements:
- The NutriPapi system shall send the user daily notifications at 8 am, 12 pm, and 6 pm that their recipes are ready for the day and to prepare the ingredients.
- The NutriPapi system shall be able to filter out suggestions for the ingredients based on the dietary restrictions entered by the user
- The NutriPapi system shall have 4 meals dedicated to breakfast, lunch, dinner, and snacks.
- The NutriPapi system shall allow users to search for the ingredients by their name and get nutritional information about that ingredient.
- The NutriPapi system shall recommend different recipes for different meals on the same day and can only recommend the same meal after 2 weeks unless specified by the user.

### Non-Functional Requirements:
- The NutriPapi ​system should be responsive and compatible with all major operating systems and major browsers.
- The NutriPapi system shall implement secure authentication methods and encrypt sensitive user data
- The NutriPapi system shall be user-friendly, with an intuitive interface that is easy to navigate for a wide range of users, including those with limited technical skills.

### Optional Requirements:
- The NutriPapi system shall allow the user to generate a weekly progress report
- The NutriPapi system shall send the user reminders throughout the day to start preparing their meals and stay on a consistent schedule
- The NutriPapi system shall be able to display a quote of the day that relates to diet each calendar day.
- The NutriPapi system shall allow users to create a custom meal plan based on their dietary preferences and nutritional requirements.
- The NutriPapi system shall allow the users to “like'' and “dislike” the meals they enjoyed and get recommended that same meal on another occasion on a higher frequency.

---

### User Stories
- As a user, I want to create an account on the NutriPapi system so that I can get access to its functionalities
- As a user, I want to input my current weight, target weight, height, weekly physical activity levels, and dietary requirements so that the system can provide me with tailored suggestions on achieving my health goals.
- As a user, I want to receive a daily suggested caloric intake based on my target/current weight and my timeline for gaining or losing weight so that I can make informed dietary choices.
- As a user, I want to be able to input the ingredients I have in my fridge so that the NutriPapi system can recommend different recipes and I can enjoy diverse and healthy meals.
- As a user who may have lost or gained weight, I want to update my weight in the NutriPapi system so that it can adjust my daily caloric intake recommendations accordingly.
- As a user, I want to log my daily meals so that I can track my progress towards my health goals over time.
- As a user, I want to receive timely reminders for meal preparation so that I can prepare my meals on time and maintain my health routines.
- As a user, I want to receive timely reminders for meal preparation so that I can prepare my meals on time and maintain my health routines.
- As a health-conscious user, I want to search for ingredients by name and receive detailed nutritional information about them so that I can make informed choices about the ingredients I use in my meals.
- As a user who enjoys culinary diversity, I want the NutriPapi system to recommend a variety of recipes for different meals each day and ensure that the same meal is not repeated within a two-week period unless I specifically request it.
- As a user who no longer wishes to use the NutriPapi system, I want to be able to delete my account so that my personal data is removed from the system.
- As a user who uses multiple devices, I want the NutriPapi system to be responsive and compatible on all my devices so that I can access my meal plans and health tracking.
- As a user concerned about my personal data, I want the NutriPapi system to implement secure authentication methods and encrypt sensitive user data to ensure my privacy and security.

---

## UML Class Diagram and Entity Relationship Diagram
![UML Class and Entity Relationship Diagram](docs/UML_ER.png)
