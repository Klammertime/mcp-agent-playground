<div align="center">

# MCP Agent Playground 🧪

_My experimental lab for building AI agents with MCP, CopilotKit, and LangGraph_

![CopilotKit-Banner](https://github.com/user-attachments/assets/8167c845-0381-45d9-ad1c-83f995d48290)

</div>

![multi-agent-canvas](https://github.com/user-attachments/assets/5953a5a6-5686-4722-9477-5279b67b3dba)

# 🚨 Multi-Agent Canvas: An Honest Developer Review

> **TL;DR**: This demo is more complex than it appears. Read the "Gotchas" section before diving in.

## What This Actually Is

This is a **multi-agent system demo** that showcases three different agent paradigms in one interface:

- **Travel Agent**: CopilotKit cloud-based (works immediately)
- **Research Agent**: CopilotKit cloud-based (works immediately)
- **MCP Agent**: Local LangGraph server + MCP protocol (requires setup)

**The Problem**: It's marketed as a simple starter, but it's actually a complex hybrid system that mixes cloud and local infrastructure in confusing ways.

## 🔥 Major Gotchas for New Developers

### 1. **"It's Just a Demo" is Misleading**

- **What you expect**: Simple example to understand multi-agent concepts
- **What you get**: Production-complexity setup with multiple servers, protocols, and failure points
- **Reality**: This is closer to a reference architecture than a learning demo

### 2. **Invisible Connection Patterns**

```
User Input → CopilotKit Router → {
  Travel/Research: Direct to cloud API ✅
  MCP: Local LangGraph → MCP Servers 🚨
}
```

**The confusing part**: Some agents work immediately, others require a full local backend. This isn't obvious from the UI.

### 3. **Agent Selection is Opaque**

Agent routing happens via AI interpretation of these instructions:

```typescript
"Always use the MCP Agent if you need to use the MCP Servers.
You are a multi-agent chat system with specialized agents:
- MCP Agent: For general or multipurpose tasks use the mcp-agent
- Travel Agent: Expert in planning trips, itineraries and travel recommendations
- Research Agent: You are a helpful research assistant..."
```

**The problem**: No explicit routing logic, just natural language that may or may not work consistently.

### 4. **Silent Failures Everywhere**

- MCP agent appears to work but silently fails if LangGraph server isn't running
- No clear error messages when agents don't activate
- Frontend shows no difference between "agent choosing not to respond" vs "agent can't respond"

### 5. **Directory Hell**

```bash
# These work from root:
cd frontend && npm run dev ✅

# These DON'T work from root:
poetry run langgraph dev  ❌ (needs agent/ directory)
poetry run python weather_server.py  ❌ (needs agent/ directory)

# But the README doesn't make this clear
```

## 🛠️ What You Actually Need to Run Everything

### Minimal Setup (Travel + Research Only)

```bash
cd frontend
cp example.env .env
# Add: NEXT_PUBLIC_COPILOT_CLOUD_API_KEY=your_key
npm install && npm run dev
```

**Result**: 2/3 agents work, good for basic testing

### Full Setup (All Agents)

```bash
# 1. Frontend
cd frontend
cp example.env .env && echo "NEXT_PUBLIC_COPILOT_CLOUD_API_KEY=your_key" >> .env
npm install && npm run dev

# 2. Agent backend (different terminal)
cd agent
cp example.env .env && echo -e "OPENAI_API_KEY=your_key\nLANGSMITH_API_KEY=optional" >> .env
poetry install
poetry run langgraph dev --host localhost --port 8123

# 3. Optional: Custom MCP servers (if you built any)
# cd agent && poetry run python weather_server.py &
```

## 🎯 Who This Demo is Actually For

### ❌ **NOT Good For**:

- **First-time multi-agent learners** - Too complex, too many moving parts
- **Quick prototyping** - Setup overhead is significant
- **Understanding agent concepts** - Architecture is unnecessarily hybrid

### ✅ **Good For**:

- **Evaluating CopilotKit + LangGraph integration**
- **Understanding MCP protocol implementation**
- **Reference for production multi-agent architecture**
- **Learning about hybrid cloud/local agent systems**

## 🔍 Better Alternatives for Learning

If you want to learn multi-agent concepts without this complexity:

1. **Pure CopilotKit**: Build single-agent apps first
2. **Pure LangGraph**: Start with local-only multi-agent systems
3. **CrewAI**: Simpler multi-agent framework
4. **AutoGen**: Microsoft's multi-agent framework

## 🚨 Common Developer Traps

### "Why isn't my math calculation working?"

- **Trap**: Assuming it should work because there's a math server
- **Reality**: Need LangGraph server running + proper MCP configuration
- **Debug**: Check `lsof -i :8123` and look for agent status in UI

### "The agents seem random"

- **Trap**: Expecting deterministic routing
- **Reality**: AI-based routing via natural language instructions
- **Solution**: Be very explicit in your prompts

### "Everything was working, now it's broken"

- **Trap**: Assuming stateless behavior
- **Reality**: Local servers can crash, connections can drop
- **Debug**: Check all server processes, restart everything

## 📊 Development Experience Rating

| Aspect                   | Rating | Notes                                       |
| ------------------------ | ------ | ------------------------------------------- |
| **Initial Setup**        | 3/10   | Multiple unclear steps, easy to get stuck   |
| **Documentation**        | 4/10   | Exists but misses critical gotchas          |
| **Debugging**            | 2/10   | Silent failures, no error visibility        |
| **Learning Value**       | 6/10   | Good concepts, poor execution for beginners |
| **Production Readiness** | 7/10   | Actually decent architecture, just complex  |

## 🎖️ Our Improvements

We added some debugging tools to make this less painful:

1. **Real-time agent status panel** - See which agents are actually running
2. **Development notes** - `DEVELOPMENT_NOTES.md` with setup sequence
3. **Honest documentation** - This README

## 🤔 Should You Use This?

**Use it if**: You need to evaluate CopilotKit + LangGraph integration for production, or you're specifically learning MCP protocol.

**Skip it if**: You're new to multi-agent systems, want to prototype quickly, or just want to understand the concepts.

**Alternative**: Start with a single-agent CopilotKit app, then gradually add complexity.

---

## 🏆 The Original Vision vs Reality

**What it could be**: Simple, educational multi-agent playground  
**What it is**: Complex reference implementation with hybrid architecture  
**What it should be**: Either simplified for learning OR fully documented for production use

This demo sits in an uncomfortable middle ground. We hope this README helps you decide if it's right for your learning goals.

---

**Original Project**: [CopilotKit/open-multi-agent-canvas](https://github.com/CopilotKit/open-multi-agent-canvas)  
**Honest Review**: Added by developers who spent way too much time figuring this out

## �� What This Is

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
