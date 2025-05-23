import requests

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "llama3.2:1b"

def test_ollama():
    url = f"{OLLAMA_URL}/api/generate"
    payload = {
        "model": MODEL_NAME,
        "prompt": "Say hello",
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Ollama API response:", response.json().get("response"))
    except Exception as e:
        print("Error connecting to Ollama:", e)

if __name__ == "__main__":
    test_ollama()
