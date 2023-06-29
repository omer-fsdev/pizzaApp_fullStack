# Pizza App - Full-Stack Project

Pizza App is a full-stack web application built with Django and Django Template Language. It allows users to order pizzas online.

## Features

- User registration and authentication
- Browse available pizza options
- Customize pizza size and quantity
- Place, update or delete orders
- View order history

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/omer-fsdev/pizzaApp_fullStack.git
   ```

2. Navigate to the project directory:

   ```
   cd pizzaApp_fullStack
   ```

3. Create a virtual environment and activate it:

```

- python -m venv env

- source env/bin/activate # Linux/Mac
.\env\Scripts\activate # Windows

```

3. Install the required packages:

```

pip install -r requirements.txt

```

4. Add .env file to the base directory and add your secret key to .env:

   ```
   SECRET_KEY = your_secret_key
   ```

5. Run database migrations:

```

python manage.py migrate

```

5. Start the development server:

```

python manage.py runserver

```

6. Open your web browser and visit http://localhost:8000 to view the application.

## Usage

- Create an account or login.
- Browse the available pizza options, select quantity or size, and place order.

## License

This project is licensed under the MIT License.
