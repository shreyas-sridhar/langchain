from typing import Any, Iterator

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessageChunk
from langchain_core.outputs import ChatGenerationChunk, ChatResult
from langchain_core.tracers._streaming import _V2StreamingCallbackHandler


class GeminiLikeModel(BaseChatModel):
    """Streams usage as per-chunk deltas, like langchain-google-genai / -vertexai."""

    @property
    def _llm_type(self) -> str:
        return "gemini-like"

    def _generate(self, *args: Any, **kwargs: Any) -> ChatResult:
        raise NotImplementedError

    def _stream(self, *args: Any, **kwargs: Any) -> Iterator[ChatGenerationChunk]:
        yield ChatGenerationChunk(message=AIMessageChunk(content="Hello", usage_metadata={
            "input_tokens": 100, "output_tokens": 40, "total_tokens": 140,
            "input_token_details": {"cache_read": 80},
            "output_token_details": {"reasoning": 30},
        }))
        yield ChatGenerationChunk(message=AIMessageChunk(content=" world", usage_metadata={
            "input_tokens": 0, "output_tokens": 20, "total_tokens": 20,
            "input_token_details": {"cache_read": 0},
            "output_token_details": {"reasoning": 0},
        }))


class V2Handler(BaseCallbackHandler, _V2StreamingCallbackHandler):
    """Any handler that opts into protocol streaming."""


model = GeminiLikeModel()
print("v1:", model.invoke("hi", stream=True).usage_metadata)
print("v2:", model.invoke("hi", config={"callbacks": [V2Handler()]}).usage_metadata)

stream = model.stream_events("hi", version="v3")
for _ in stream:
    pass
print("v3:", stream.output.usage_metadata)
