from typing import List
from enum import Enum
from pydantic import BaseModel, Field

class Sentiment(str, Enum):
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"

class TargetAudience(str, Enum):
    CHILDREN = "children"
    FAMILY = "family"
    TEENS = "teens"
    YOUNG_ADULTS = "young_adults"
    ADULTS = "adults"
    MATURE = "mature"

class Tone(str, Enum):
    DARK = "dark"
    LIGHTHEARTED = "lighthearted"
    SERIOUS = "serious"
    HUMOROUS = "humorous"
    SUSPENSEFUL = "suspenseful"
    ROMANTIC = "romantic"
    MELANCHOLIC = "melancholic"
    INSPIRATIONAL = "inspirational"
    SATIRICAL = "satirical"

class MovieEnrichment(BaseModel):
    """Structured enrichment for a single movie."""
    sentiment: Sentiment = Field(..., description="Emotional tone the overview evokes")
    target_audience: TargetAudience = Field(..., description="Most likely primary audience")
    tone: Tone = Field(..., description="Dominant tone of the film")
    themes: List[str] = Field(
        ...,
        description="2-4 thematic tags (lowercase short noun phrases, e.g. 'redemption')",
        min_length=2, max_length=4,
    )
    sub_genre: str = Field(..., description="Specific sub-genre, lowercase (e.g. 'neo-noir')")

# Schema used in the prompt-engineering demo below
class SentimentOnly(BaseModel):
    sentiment: Sentiment