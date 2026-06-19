import re
from llm_utils import call_llm


# ================= AGENT 1: PLANNER =================
def planner_agent(topic: str) -> list:
    system = (
        "You are a Research Architect. Analyze the topic and generate research questions. "
        "Generate only as many questions as needed based on topic complexity."
    )

    user = (
        f"Topic: {topic}\n"
        "Generate research questions.\n"
        "Each question must be on a new line and end with a question mark.\n"
        "Questions:"
    )

    raw = call_llm(system, user, max_tokens=600)

    questions = []
    for line in raw.split("\n"):
        clean = re.sub(r"^[\d\-\.\)\*]+\s*", "", line).strip()
        if "?" in clean and len(clean) > 10:
            questions.append(clean)

    if not questions:
        questions = [f"What are the core concepts of {topic}?"]

    return questions
