from llm_utils import call_llm, tavily_search
from planner_agent import planner_agent
from searcher_agent import searcher_agent


# ================= AGENT 3: WRITER =================
def writer_agent(topic: str, questions: list, search_data: dict) -> str:
    facts_list = search_data.get("context", [])

    # -------- FORMAT PLANNER QUESTIONS --------
    formatted_questions = ""
    for i, q in enumerate(questions):
        formatted_questions += f"{i+1}. {q}\n"

    # -------- FORMAT SEARCH CONTEXT --------
    formatted_context = ""
    for i, fact in enumerate(facts_list):
        formatted_context += f"DATA POINT {i+1}: {fact}\n"

    if len(formatted_context) > 5500:
        formatted_context = formatted_context[:5500] + "..."

    system = (
        "You are a Senior AI Research Scientist and Technical Writer. "
        "Follow planner questions strictly while maintaining professional documentation quality."
    )

    # -------- USER PROMPT (YOUR ORIGINAL + EXTRA CONTEXT) --------
    user = (
        # -------- EXTRA (ADDED – DO NOT REMOVE) --------
        "MANDATORY ANALYTICAL CONTEXT:\n"
        "The Planner Agent has generated research questions.\n"
        "You MUST use them to guide and shape the technical analysis.\n"
        "All questions must be addressed implicitly or explicitly.\n\n"

        "PLANNER AGENT QUESTIONS:\n"
        f"{formatted_questions}\n"
        "----------------------------------------\n\n"

        # -------- ORIGINAL PROMPT (UNCHANGED) --------
        f"Generate a comprehensive technical documentation for the topic: '{topic}'.\n\n"
        f"STRUCTURE REQUIREMENTS:\n"
        f"1. TITLE: Professional and academic.\n"
        f"2. EXECUTIVE SUMMARY: A high-level overview (4-5 sentences).\n"
        f"3. TECHNICAL ANALYSIS: 7-9 detailed bullet points. Use bold text for key concepts. "
        f"Focus on the 'how' and 'why' based on the facts.\n"
        f"4. CHALLENGES & ETHICS: A specific section on implementation hurdles and ethical considerations.\n"
        f"5. STRATEGIC CONCLUSION: A forward-looking summary (6-9 sentences).\n\n"
        f"FACTS FROM WEB RESEARCH:\n"
        f"{formatted_context}\n\n"
        f"FORMATTING INSTRUCTIONS:\n"
        f"- Use H1 (#) for Title, H2 (##) for Sections.\n"
        f"- Use horizontal rules (---) to separate sections.\n"
        f"- Avoid empty filler phrases like 'In this report'.\n"
        f"- Ensure sentences are complete and professionally articulated.\n\n"
        f"FINAL REPORT:"
    )

    summary = call_llm(system, user, max_tokens=1500)

    if not summary or not summary.strip():
        return "❌ Report generation failed."

    return summary.replace("FINAL REPORT:", "").strip()


# ================= CLI MODE =================
def run_cli():
    print("### Local Agentic RAG System ###")

    while True:
        topic = input("You: ")
        if topic.lower() in ["exit", "quit"]:
            break

        questions = planner_agent(topic)
        data = searcher_agent(questions)
        report = writer_agent(topic, questions, data)

        print("\n" + "=" * 60)
        print(report)
        print("=" * 60)


if __name__ == "__main__":
    run_cli()
