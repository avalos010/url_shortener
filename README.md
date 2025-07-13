# 🔗 Simple URL Shortener (FastAPI + SQLite)

A simple and minimal URL shortener built with [FastAPI](https://fastapi.tiangolo.com/) and [SQLite](https://www.sqlite.org/index.html).

## ✨ Features

- Shorten long URLs into compact, shareable links
- Store shortened URLs in a local SQLite database
- Retrieve the original URL using the shortened link

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

#### On Linux/macOS

```bash
source .venv/bin/activate
```

#### On Windows

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

## 📡 API Endpoints

### POST `/shorten`

Shortens a long URL.

**Request Body:**

```json
{
  "original_url": "https://www.example.com"
}
```

**Response:**

```json
{
  "shortened_url": "https://your-url-shortener.com/abc123"
}
```

---

### GET `/redirect/{shortened_url}`

Retrieves the original URL from a shortened one.

**Example Request:**

```
GET https://your-url-shortener.com/abc123
```

**Response:**

```json
{
  "original_url": "https://www.example.com"
}
```

## 🗃️ Database

- The application uses a SQLite database for storage.
- The database file is named `urls.db` and is located in the project root directory.

## 🪪 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome!

If you'd like to contribute:

1. Fork the repository
2. Create a feature or fix branch
3. Submit a pull request

## 🙏 Acknowledgments

- Built using [FastAPI](https://fastapi.tiangolo.com/)
- Project structure inspired by the official FastAPI documentation
