from dataclasses import dataclass

@dataclass
class Error:
    err: str
    msg: str
    l: int
    c: int
    
    def __repr__(self) -> str:
        return f"Error at line {self.l}, column {self.c}\n{self.err}: {self.msg}"