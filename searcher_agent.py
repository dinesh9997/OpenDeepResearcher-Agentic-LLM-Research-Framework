import time
from llm_utils import tavily_search


# ================= AGENT 2: SEARCHER (INTERNAL) =================
def searcher_agent(questions: list) -> dict:
    context_data = []
    sources = set()

    for q in questions:
        results = tavily_search(q)
        for r in results:
            content = r.get("content", "")
            if content:
                context_data.append(content[:600])
            if r.get("url"):
                sources.add(r["url"])
        time.sleep(0.5)

    return {
        "context": list(set(context_data))[:15],
        "sources": list(sources)
    }
