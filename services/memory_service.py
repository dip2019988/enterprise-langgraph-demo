from typing import List
from mem0 import Memory
from config.settings import settings
from utils.logger import logger
 
 
class Mem0Service:
    def __init__(self):
        try:
            if settings.MEM0_API_KEY:
                self.memory = Memory.from_config({"api_key": settings.MEM0_API_KEY})
            else:
                # Use in-memory vector store configuration to prevent /tmp/qdrant file locking errors
                mem0_config = {
                    "vector_store": {
                        "provider": "qdrant",
                        "config": {
                            "location": ":memory:",
                        }
                    }
                }
                self.memory = Memory.from_config(mem0_config)
            logger.info("[MEM0] Memory Service initialized successfully.")
        except Exception as e:
            logger.warning(f"[MEM0] Local storage notice ({str(e)}). Initializing fallback in-memory store.")
            try:
                self.memory = Memory()
            except Exception:
                self.memory = None
 
    def get_user_memories(self, user_id: str) -> List[str]:
        if not self.memory:
            return []
        try:
            results = self.memory.get_all(user_id=user_id)
            memories = []
            if isinstance(results, list):
                for item in results:
                    if isinstance(item, dict) and "memory" in item:
                        memories.append(item["memory"])
            elif isinstance(results, dict) and "results" in results:
                memories = [m.get("memory", "") for m in results.get("results", [])]
            return memories
        except Exception as e:
            logger.error(f"[MEM0] Failed to fetch memories: {str(e)}")
            return []
 
    def add_user_memory(self, user_id: str, interaction: str):
        if not self.memory:
            return
        try:
            self.memory.add(interaction, user_id=user_id)
        except Exception as e:
            logger.error(f"[MEM0] Failed to save memory: {str(e)}")
 
    def close(self):
        """Safely release client resources on shutdown."""
        try:
            if hasattr(self, "memory") and self.memory and hasattr(self.memory, "vector_store"):
                if hasattr(self.memory.vector_store, "client") and hasattr(self.memory.vector_store.client, "close"):
                    self.memory.vector_store.client.close()
        except Exception:
            pass
 
 
mem0_service = Mem0Service()