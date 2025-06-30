<div align="center">

# MCP Agent Playground 🧪

_My experimental lab for building AI agents with MCP, CopilotKit, and LangGraph_

![CopilotKit-Banner](https://github.com/user-attachments/assets/8167c845-0381-45d9-ad1c-83f995d48290)

</div>

![multi-agent-canvas](https://github.com/user-attachments/assets/5953a5a6-5686-4722-9477-5279b67b3dba)

## 🎯 What This Is

This is my personal playground for learning and experimenting with multi-agent AI systems. Based on [CopilotKit's Open Multi-Agent Canvas](https://github.com/CopilotKit/open-multi-agent-canvas), I'm extending it with custom agents, MCP servers, and advanced workflows.

**Core Technologies:**

- 🤖 **CopilotKit** - Agent orchestration and chat interface
- 🧠 **LangGraph** - Python agent workflows and state management
- 🔧 **MCP (Model Context Protocol)** - Extensible tool integration
- ⚛️ **Next.js + TypeScript** - Modern React frontend
- 🎨 **Tailwind CSS** - Beautiful, responsive UI

## 🚀 My Learning Journey

I've created comprehensive guides for mastering this project:

- 📋 **[CHECKLIST.md](./CHECKLIST.md)** - Updated project overview and setup guide
- 📚 **[LEARNING_TASKS.md](./LEARNING_TASKS.md)** - 4-week structured learning path
- ⚡ **[INTENSIVE_LEARNING.md](./INTENSIVE_LEARNING.md)** - 3-5 day intensive mode for focused learning

## 🤖 The Three Agent Types

| Agent                 | Purpose                             | UI Component                     | What I'm Building                                     |
| --------------------- | ----------------------------------- | -------------------------------- | ----------------------------------------------------- |
| **🗺️ Travel Agent**   | Trip planning, location-based tasks | Interactive map interface        | Custom travel experiences, local recommendations      |
| **📊 Research Agent** | Information gathering, analysis     | Research logs + markdown reports | Specialized research domains, custom data sources     |
| **🔧 MCP Agent**      | Extensible tool integration         | Tool execution interface         | Weather servers, productivity tools, API integrations |

## 🛠️ My Custom Additions

### Planned Custom Agents

- [ ] **Weather Agent** - Real-time weather data with maps
- [ ] **Finance Agent** - Stock tracking and budget analysis
- [ ] **Code Assistant Agent** - GitHub integration and code review
- [ ] **Productivity Agent** - Calendar, tasks, and note management

### Custom MCP Servers

- [ ] **Weather Server** - OpenWeatherMap integration
- [ ] **GitHub Server** - Repository management and code analysis
- [ ] **Calendar Server** - Google Calendar integration
- [ ] **Finance Server** - Stock and crypto data

## 🚀 Quick Start

### Prerequisites

- [pnpm](https://pnpm.io/installation) or npm
- Node.js 18+
- Python 3.10+ (for MCP agent backend)

### 1. Frontend Setup

```bash
cd frontend
cp example.env .env
# Add your CopilotKit API key to .env:
# NEXT_PUBLIC_CPK_PUBLIC_API_KEY=your_key_here
pnpm install
pnpm run dev
```

Visit [http://localhost:3000](http://localhost:3000) 🎉

### 2. MCP Agent Backend (Optional)

```bash
cd agent
cp example.env .env
# Add your OpenAI API key to .env:
# OPENAI_API_KEY=your_key_here
poetry install
poetry run langgraph dev --host localhost --port 8123 --no-browser
```

### 3. Test the Agents

Try these commands in the chat:

```
Travel: "Plan a 5-day trip to Japan with cultural activities"
Research: "Research the latest developments in quantum computing"
MCP: "Calculate the square root of 256"
```

## 🔧 MCP Configuration

The MCP Agent supports two types of servers:

**Standard IO Servers** (Local Python scripts):

```json
{
  "math": {
    "command": "python",
    "args": ["path/to/math_server.py"],
    "transport": "stdio"
  }
}
```

**SSE Servers** (Remote endpoints):

```json
{
  "external": {
    "url": "https://mcp.composio.dev",
    "transport": "sse"
  }
}
```

Configure servers via the "MCP Servers" button in the top-right corner.

## 📚 Learning Resources

### Essential Reading

- [CopilotKit Documentation](https://docs.copilotkit.ai/coagents)
- [LangGraph Platform Docs](https://langchain-ai.github.io/langgraph/cloud/)
- [Model Context Protocol (MCP) Docs](https://github.com/langchain-ai/langgraph/tree/main/examples/mcp)

### Original Agents (Reference)

- [CoAgents Travel Agent](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-travel/agent)
- [CoAgents AI Researcher](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-ai-researcher/agent)

## 🎯 Current Progress

### ✅ Completed

- [x] Set up development environment
- [x] Tested all three base agents
- [x] Created comprehensive learning documentation
- [x] Analyzed codebase architecture

### 🚧 In Progress

- [ ] Building custom Weather MCP server
- [ ] Creating Weather Agent UI component
- [ ] Implementing agent state persistence

### 📋 Next Steps

- [ ] Deploy to production
- [ ] Add authentication system
- [ ] Create demo videos
- [ ] Write technical blog posts

## 🤝 Contributing

This is my personal learning project, but feel free to:

- ⭐ Star the repo if you find it helpful
- 🐛 Report issues or suggest improvements
- 💡 Share ideas for new agents or MCP servers
- 📖 Use my learning guides for your own journey

## 📄 License & Attribution

**Original Project:** [CopilotKit's Open Multi-Agent Canvas](https://github.com/CopilotKit/open-multi-agent-canvas)  
**License:** MIT (see [LICENSE](./LICENSE))  
**My Additions:** Also MIT licensed

---

**🎉 Ready to build your own multi-agent system?** Start with the [Quick Start](#-quick-start) and follow my [learning guides](./CHECKLIST.md)!
