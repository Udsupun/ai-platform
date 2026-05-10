def chunk_text(
    text: str,
    chunk_size: int = 200,
    overlap: int = 50
):
    words = text.split()

    chunks = []
    step = chunk_size - overlap

    # Split the text into chunks
    for i in range (
        0,
        len(words),
        step
    ):
        # Create a chunk of text
        chunk = words[i:i + chunk_size]
        chunks.append(" ".join(chunk))

    return chunks