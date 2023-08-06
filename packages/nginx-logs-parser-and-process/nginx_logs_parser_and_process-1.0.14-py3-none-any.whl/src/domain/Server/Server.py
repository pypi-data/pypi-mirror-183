from pydantic import BaseModel
from src.domain.Tables.tables import Tables


class Server(BaseModel):
    name: str
    source_path: str
    host: str = None
    port: int = 22
    includes: str = ""
    data_filter: list = []
    tables: Tables = None
