import logging
from typing import Dict, List

from config import client
from fastapi import HTTPException

logger = logging.getLogger(__name__)


async def chat_helper(msg: Dict, model: str="gpt-4.1", system_configuration: str = "You are a helpful  assistant.", message_history: List[Dict] = []):
    msgs = [{"role": "system",  "content": system_configuration}] + message_history + [msg]
    logger.debug(f"chat_helper - Sending messages: {msgs}")
    print(msg)
    try: 
        completion =  client.responses.create(
            model="gpt-4.1",
            input=msg["content"]
        )
        # completion = client.chat.completions.create(
        #     model=model,
        #     messages=msgs
        # )
        
        logger.debug(f"chat_helper - Received completion: {completion}")
        response_msg = {
            "role": "assistant",
            "content": completion.output_text,
            "refusal": None
        }
        return response_msg
    except Exception as e:
        logger.error(f"chat_helper- Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))