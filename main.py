from enum import Enum

class Vectors(Enum):
    PINECONE:str = "pinecone"
    MILVUSE:str = "milvus"
    CHROM:str = "chroma"



inst = Vectors.CHROM

print(inst.value)
print(inst.name)