def web_search(query, top_k=3):
    return [f"https://example.com?q={query}&r={i}" for i in range(top_k)]
