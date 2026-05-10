from app.utils.text_chunker import chunk_text


def test_chunk_text_without_overlap():
    text = "one two three four five six"

    chunks = chunk_text(text, chunk_size=2, overlap=0)

    assert chunks == [
        "one two",
        "three four",
        "five six",
    ]


def test_chunk_text_with_overlap():
    text = "one two three four five"

    chunks = chunk_text(text, chunk_size=3, overlap=1)

    assert chunks == [
        "one two three",
        "three four five",
        "five",
    ]
