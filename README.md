# Ai chat with web search + no limit 

Simple Python example for using the **Groq Chat Completions API**.

## Requirements

Install the required package:

```bash
pip install requests
```

---

## Getting Started

1. Create an account at **https://groq.com**.
2. Generate a new API Key.
3. Replace:

```python
Bearer YOUR_API_KEY
```

with your own API key.

---

## Features

The example demonstrates how to:

- Send a prompt to the Groq API.
- Receive the model response.
- Enable supported tools:
  - Web Search
  - Visit Website
  - Code Interpreter

---

## Using Another Model

If you want to use a different model:

1. Open **Playground**.
2. Select the desired model.
3. Copy its name.
4. Replace the value of the `model` field inside the payload.

> Some models support additional parameters such as reasoning. Check the model documentation before using them.

---

## API Limits

Current limits:

- **30 requests/minute**
- **14,400 requests/day**

Token limits are automatically refreshed every minute.

---

## Author

 by **Murtada tariq**
