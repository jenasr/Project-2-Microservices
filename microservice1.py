from pydantic import BaseModel

class Guess(BaseModel):
    id: int
    guess: str
