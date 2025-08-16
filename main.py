from agents import Agent, Runner, function_tool
import requests

# -------- TOOL 1: Search for Papers --------
# TODO: Enable function_tool once if you have OPENAIN credits. Currently we are calling it directly
# @function_tool  
def search_papers(topic: str):
    """
    searches semantic scholars for academic papers on topic.
    Returns list of dicts with 'title', 'abstract', 'authors', 'year'
    """

    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": topic,
        "limit": 5,
        "fields": "title,abstract,authors,year"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    papers = []
    for paper in data.get("data", []):
        papers.append({
            "title": paper.get("title"),
            "abstract": paper.get("abstract", "No abstract available."),
            "authors": [a.get("name") for a in paper.get("authors", [])],
            "year": paper.get("year", "n.d.")
        })
    return papers


# -------- TOOL 2: Format Citations --------
# TODO: Enable function_tool once if you have OPENAIN credits. Currently we are calling it directly
# @function_tool
def format_citations(papers: list):
    """
    format papers in APA style citations
    """
    citations = []

    for p in papers:
        authors = ", ".join(p["authors"])
        citations.append(f"{authors} ({p['year']}). {p['title']}.")
    return "\n".join(citations)


# -------- AGENTS --------
search_agents = Agent(
    name="Search Agent",
    instructions="You search for recent academic papers on a give topic",
    tools=[search_papers]
)

summarizer_agent = Agent(
    name="Summarizer Agent", 
    instructions="You take a list of papers and summarize them in 3-4 sentences each."
)

citation_agent = Agent(
    name="Citation Agent", 
    instructions="You take a list of papers and format them into APA style citations.",
    tools=[format_citations]
)

# -------- ORCHESTRATION AGENT --------
orchestrator = Agent(
    name="Research Orchestrator", 
    instructions=(
        "You coordinate research: 1) Ask Search Agent for papers, "
        "2) Ask Summarizer Agent for summaries, "
        "3) Ask Citation Agent for citations. "
        "Return both summaries and citations."
    ),
    handoffs=[search_agents, summarizer_agent, citation_agent]
)

# -------- RUN --------
if __name__ == "__main__":
    topic = input("Enter research topic: ")

    # TODO: ==== use this if you have OPENAI credits ===
    # result = Runner.run_sync(
    #     starting_agent=orchestrator,
    #     input=f"Find and summarize recent papers about {topic}. "
    # )
    # print("\n=== FINAL OUTPUT ==== \n")
    # print(result.final_output)
    # ===================================================

    # Here we are calling functions directly as workaround, without OPENAI credits
    papers = search_papers(topic)
    print("\n=== PAPERS FOUND ===")
    for i, p in enumerate(papers, 1):
        print(f"{i}. {p['title']} ({p['year']}) - {', '.join(p['authors'][:3])}")

    print("\n=== SUMMARIES ===")
    for p in papers:
        print(f"- {p['title']}: {p['abstract'][:200]}...")  # just trim for demo

    print("\n=== CITATIONS ===")
    print(format_citations(papers))

