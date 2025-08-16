# Research Paper Summarizer & Citation Finder

A learning exercise built with the **OpenAI Agents SDK** that demonstrates how to orchestrate multiple AI agents to:
1. Search for research papers on a given topic.
2. Summarize key findings from each paper.
3. Format the results in APA-style citations.

> ⚠️ This is a demo project — the paper search function is mocked for now. You can easily extend it to use the [Semantic Scholar API](https://api.semanticscholar.org/), [arXiv API](https://arxiv.org/help/api), or other scholarly data sources.

---

## Features

- **Multi-agent orchestration**:
  - **Search Agent**: Finds relevant papers (mocked for now).
  - **Summarizer Agent**: Creates concise summaries.
  - **Citation Agent**: Formats citations in APA style.
- **Extensible**:
  - Replace mock search with real APIs.
  - Add PDF parsing for deeper summaries.
  - Store results in a database.
- **OpenAI Agents SDK** for agent management, handoffs, and tool execution.

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/research-agents-demo.git
cd research-agents-demo


### 2. Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate


### 3. Install dependencies
```bash
pip install openai-agents requests


### 4. Set your OpenAI API key
```bash
export OPENAI_API_KEY="your-key-here"


## Usage
Run script
```bash
python main.py


you will be prompted to enter research project
```yaml
Enter research topic: AI in healthcare

example output
```java
=== FINAL OUTPUT ===

Summary:
1. "AI in healthcare - Advances in 2024" explores the latest applications...
2. "Challenges of AI in healthcare in developing nations" critically reviews...

Citations:
Dr. Alice Smith, Prof. John Doe (2024). AI in healthcare - Advances in 2024.
Jane Roe, Michael Chan (2023). Challenges of AI in healthcare in developing nations.


## Project Structure
```bash
.
├── main.py        # Main script with agents, tools, and orchestration
├── README.md      # Project documentation
└── requirements.txt (optional)



