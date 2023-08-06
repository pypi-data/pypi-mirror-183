from .model import Model


class Group(Model):
    """Represents a MangaDex Group."""
    __slots__ = (
        "id", "name", "desc", "website", "irc_server", "irc_channel", "discord", "email",
        "locked", "official", "verified", "leader", "members", "created_at", "updated_at", "client"
    )

    def __init__(self, provider):
        super().__init__(provider)
        
        self.id: str = ""


        self.provider = provider
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    def __repr__(self) -> str:
        return str(self)