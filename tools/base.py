"""
Base tool implementation
"""

from typing import Any, Callable, Dict, Optional
from pydantic import BaseModel

class Tool(BaseModel):
    """Base class for all tools"""
    
    name: str
    description: str
    func: Callable
    config: Optional[Dict[str, Any]] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self._validate_func()
        
    def _validate_func(self) -> None:
        """Validate the tool function"""
        if not callable(self.func):
            raise ValueError("Tool function must be callable")
            
    async def run(self, *args: Any, **kwargs: Any) -> Any:
        """Run the tool with the given arguments"""
        try:
            result = await self.func(*args, **kwargs)
            return result
        except Exception as e:
            raise RuntimeError(f"Error running tool {self.name}: {str(e)}")
            
    def get_config(self) -> Dict[str, Any]:
        """Get the tool configuration"""
        return self.config.copy() if self.config else {}
        
    def set_config(self, config: Dict[str, Any]) -> None:
        """Set the tool configuration"""
        self.config = config.copy()
        
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Make the tool callable"""
        return self.run(*args, **kwargs) 