"""
Base memory implementation
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class Memory(BaseModel):
    """Base class for memory management"""
    
    store: Any
    config: Optional[Dict[str, Any]] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        self._validate_store()
        
    def _validate_store(self) -> None:
        """Validate the memory store"""
        if not hasattr(self.store, 'get') or not hasattr(self.store, 'set'):
            raise ValueError("Memory store must implement get and set methods")
            
    async def get(self, key: str) -> Any:
        """Get a value from memory"""
        return await self.store.get(key)
        
    async def set(self, key: str, value: Any) -> None:
        """Set a value in memory"""
        await self.store.set(key, value)
        
    async def update(self, data: Dict[str, Any]) -> None:
        """Update multiple values in memory"""
        for key, value in data.items():
            await self.set(key, value)
            
    async def delete(self, key: str) -> None:
        """Delete a value from memory"""
        await self.store.delete(key)
        
    async def clear(self) -> None:
        """Clear all values from memory"""
        await self.store.clear()
        
    def get_config(self) -> Dict[str, Any]:
        """Get the memory configuration"""
        return self.config.copy() if self.config else {}
        
    def set_config(self, config: Dict[str, Any]) -> None:
        """Set the memory configuration"""
        self.config = config.copy() 