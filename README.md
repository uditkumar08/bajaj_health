# BFHL API

A simple FastAPI application that provides mathematical operations and AI-powered responses.

## 📋 What is This?

BFHL API is a web service built with FastAPI that helps you:
- Calculate Fibonacci sequences
- Check if numbers are prime
- Find the Least Common Multiple (LCM)
- Find the Highest Common Factor (HCF)
- Get AI-powered responses to your queries

## 🎯 Prerequisites

Before you start, make sure you have:
- **Python 3.8+** installed on your computer
- **pip** (Python package installer)
- Optional: An `.env` file with your email address

## 🚀 Getting Started

### Step 1: Install Dependencies

Open your terminal/command prompt and navigate to the project folder, then run:

```bash
pip install -r requirements.txt
```

This installs all the libraries needed to run the application.

### Step 2: Create Environment File (Optional)

Create a `.env` file in the root folder and add:

```
EMAIL=your-email@example.com
```

### Step 3: Start the Server

Run the application using:

```bash
uvicorn app.main:app --reload
```

Or use the provided script:

```bash
bash start.sh
```

You should see:
```
Uvicorn running on http://127.0.0.1:8000
```

## 📡 API Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

Check if the server is running.

**Response:**
```json
{
  "is_success": true,
  "official_email": "your-email@example.com"
}
```

### 2. Main BFHL Endpoint

**Endpoint:** `POST /bfhl`

Send a request with one of these operations:

#### Fibonacci Sequence
```json
{
  "fibonacci": 5
}
```
**Response:** Returns Fibonacci numbers up to the 5th position

#### Prime Numbers
```json
{
  "prime": 10
}
```
**Response:** Returns all prime numbers up to 10

#### Least Common Multiple (LCM)
```json
{
  "lcm": [4, 6]
}
```
**Response:** Returns the LCM of the given numbers

#### Highest Common Factor (HCF)
```json
{
  "hcf": [12, 8]
}
```
**Response:** Returns the HCF (GCD) of the given numbers

#### AI Response
```json
{
  "AI": "What is machine learning?"
}
```
**Response:** Gets an AI-powered answer to your question

## 📁 Project Structure

```
bfhl_fastapi/
├── app/
│   ├── main.py           # Main FastAPI application
│   ├── routes.py         # API endpoints
│   ├── utils.py          # Helper functions
│   └── services/
│       ├── math_service.py   # Math operations (fibonacci, prime, lcm, hcf)
│       └── ai_service.py     # AI-powered features
├── requirements.txt      # Project dependencies
├── start.sh             # Script to start the server
└── README.md            # This file
```

## 🛠️ Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **Python** - Programming language
- **Uvicorn** - ASGI web server

## 💡 Tips for Beginners

1. **JSON Format:** Always send requests in JSON format (as shown in examples)
2. **POST vs GET:** Use `GET` for health check, `POST` for operations
3. **Error Handling:** If something goes wrong, you'll get an error message
4. **Hot Reload:** The `--reload` flag restarts the server when you change code

## 🙋 Common Questions

**Q: Where do I test the API?**  
A: Use tools like Postman, Insomnia, or VS Code REST Client

**Q: How do I stop the server?**  
A: Press `Ctrl + C` in the terminal

**Q: Can I modify the code?**  
A: Yes! This is a learning project. Feel free to experiment and modify!

## 📝 License

Feel free to use and modify this project as needed.

---

**Happy Coding!** 🎉
