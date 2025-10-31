from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from model import Prompt, RequestBody
from openai import OpenAI
from settings import settings

client = OpenAI(
    api_key=settings.GROQ_KEY,
    base_url=settings.GROQ_ENDPOINT,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

conversation_hist = []


@app.post("/chat", status_code=status.HTTP_200_OK)
async def chat(request: RequestBody):
    new_prompt: Prompt = Prompt(role="user", content=request.message)
    conversation_hist.append(new_prompt)
    try:
        response = client.chat.completions.create(
            model=settings.GROQ_DEPLOYMENT,
            # messages=[new_prompt.model_dump()]  # type: ignore
            messages=conversation_hist,
        )
        reply = response.choices[0].message.content
        conversation_hist.append(Prompt(role="assistant", content=reply))  # type: ignore
        return {"Answer": reply}
    except Exception as e:
        return {"Error": str(e)}


@app.delete("/clear-conv", status_code=status.HTTP_200_OK)
async def clear_convo():
    conversation_hist = []
