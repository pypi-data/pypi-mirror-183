from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class FulfillmentHelperResponse():
    message: str
    short_message: Optional[str] = None
    jump_to: Optional[str] = None
    options: Optional[List[str]] = None
    logout: Optional[bool] = False
    parameters: Optional[Dict] = None


