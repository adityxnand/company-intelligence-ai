from ..models import Chunk, Document

def get_chunk_rows(chunk_pieces:list[str],vectors:list[list[float]], doc_id:int)->list[Chunk]:
    chunk_objs = []
    for piece, vector in zip(chunk_pieces, vectors):
        chunk = Chunk(chunk=piece,embedding=vector,document_id=doc_id)
        chunk_objs.append(chunk)
    return chunk_objs


