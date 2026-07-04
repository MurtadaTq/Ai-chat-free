import requests

headers = {
    "Authorization": f"Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}


payload = {
    "model": "groq/compound",
    "messages": [
        {
            "role": "user",
            "content": "مرحبا"
        }
    ],
    "stream": False,
    "compound_custom":{"tools":{"enabled_tools":["web_search","code_interpreter","visit_website"]}}
}


response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
