from ..models import Chunk

def get_chunk_rows(chunk_pieces, doc_id:int)->Chunk:
    chunk_objs = []
    for piece in chunk_pieces:
        chunk = Chunk(chunk=piece, document_id=doc_id)
        chunk_objs.append(chunk)
    return chunk_objs
