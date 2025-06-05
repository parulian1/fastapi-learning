from openai import OpenAI

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import logging

from app.utils.openai_helpers import chat_helper


router = APIRouter(tags=["ai"], prefix="/ai")
logger = logging.getLogger(__name__)

class AiQuestion(BaseModel):
    question: str


@router.post("/")
async def answer_question(question: AiQuestion):
    logger.debug(f"/ai - received input: {question.question}")
    msg = {"role": "user", "content": question.question}
    try:
        result = await chat_helper(msg)
        logger.debug(f"/ai - returning result: {result}")
        return JSONResponse(content=result)
    except Exception as e:
        logger.error(f"/ai - Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))