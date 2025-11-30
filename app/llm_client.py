# app/llm_client.py
import os
from typing import Optional

# make sure google-genai is installed in your venv:
# pip install google-genai

try:
    from google import genai
except Exception as e:
    raise ImportError("google-genai package not found. Run: pip install google-genai") from e

class LLMClient:
    def __init__(self, model_name: str = "gemini-2.5-flash"):  # pick the model you want
        self.model = model_name
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError("Set GEMINI_API_KEY (or GOOGLE_API_KEY) environment variable with your key.")
        # create client (explicit api_key is OK for server-side)
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str, max_tokens: Optional[int] = None) -> str:
        """
        Generate text. We avoid passing unknown kwargs to SDK; use 'contents' as the docs show.
        Returns the model text as a string.
        """
        # The SDK expects `contents` (a single string or list). We won't pass unknown token args.
        response = self.client.models.generate_content(
            model=self.model,
            contents=str(prompt)
            # If your SDK version supports token limit, consult docs and pass the correct kwarg.
        )
        # The response object differs by sdk version; try to get the text.
        # response.text() or response.output[0].content[0].text depending on version.
        try:
            # Common helper in newer SDKs:
            return response.text
        except Exception:
            # Fallback: stringify the object
            return str(response)
