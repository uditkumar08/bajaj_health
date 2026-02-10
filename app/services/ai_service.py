import os
import httpx


async def ask_ai(question: str):
    api_key = os.getenv("GEMINI")
    if not api_key:
        return "Unknown"

   
    prompt = f"Answer in one word only: {question}"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"



    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        async with httpx.AsyncClient(timeout=20) as client:
            res = await client.post(url, json=payload)

        print("STATUS:", res.status_code)
        print("RAW:", res.text)

        if res.status_code != 200:
            return "Unknown"

        data = res.json()

        text = (
            data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "")
        )

        if not text:
            return "Unknown"
        return text.strip().split()[0]

    except Exception as e:
        print("ERROR:", e)
        return "Unknown"
