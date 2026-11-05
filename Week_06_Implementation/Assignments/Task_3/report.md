# Task 3 report

The script [`embed_chunks.py`](./embed_chunks.py) converts the chunks from
Task 2 into deterministic 256-dimensional hashed TF-IDF vectors. It embeds
both source code and file paths, making code elements searchable. L2
normalization allows cosine similarity to be calculated with a dot product.

The vectors and chunk metadata are stored in `chunk_embeddings.json`. JSON was
chosen because it is easily readable and portable.
