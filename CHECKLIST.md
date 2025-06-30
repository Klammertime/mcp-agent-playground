# ✅ Multi-Agent Canvas Starter - Updated Checklist

**Project**: [`open-multi-agent-canvas`](https://github.com/CopilotKit/open-multi-agent-canvas)

A sophisticated multi-agent system built with **CopilotKit**, **LangGraph**, and **MCP (Model Context Protocol)** that provides specialized AI agents with contextual visual interfaces.

---

## 🔧 Initial Setup

- [ ] **Clone the repository**
      `bash
  git clone https://github.com/CopilotKit/open-multi-agent-canvas.git
  cd open-multi-agent-canvas
  `

- [ ] **Setup Frontend**
      `bash
  cd frontend
  npm install  # or pnpm install
  npm run dev  # Starts on http://localhost:3000
  `

- [ ] **Setup Backend Agent** (Optional - for MCP functionality)
      `bash
      cd agent
      pip install -e . # or poetry install
  # Configure environment variables in .env
  `

---

## 🧠 Understanding the Architecture

### 🏗️ **Core Concept**: Multi-Agent System

This is **NOT** a traditional node-graph canvas. Instead, it's a **contextual multi-agent interface** where:

- **Left Panel**: Chat interface for user interaction
- **Right Panel**: Dynamic canvas that changes based on active agent
- **Agents**: Specialized AI agents with unique capabilities and UIs

### 🤖 **The Three Agent Types**

| Agent              | Purpose                                          | UI Component                     | Backend                  |
| ------------------ | ------------------------------------------------ | -------------------------------- | ------------------------ |
| **Travel Agent**   | Trip planning, itineraries, location-based tasks | Interactive map interface        | CopilotKit routing       |
| **Research Agent** | Research papers, information gathering, analysis | Research logs + markdown reports | CopilotKit routing       |
| **MCP Agent**      | Extensible tool integration, custom workflows    | Tool execution interface         | Python + LangGraph + MCP |

---

## 🗂️ **Key Files & Folders**

### Frontend Structure

```
frontend/src/
├── app/(canvas-pages)/page.tsx     # Main entry point
├── components/
│   ├── canvas.tsx                  # Main canvas orchestrator
│   ├── chat-window.tsx            # CopilotKit chat interface
│   ├── agents/                    # Agent-specific components
│   │   ├── travel.tsx            # Map-based travel interface
│   │   ├── researcher.tsx        # Research reports + logs
│   │   └── mcp-agent.tsx         # MCP tool execution
│   ├── map.tsx                   # Leaflet map component
│   └── mcp-config-modal.tsx      # MCP server configuration
├── lib/
│   ├── available-agents.ts       # Agent type definitions
│   └── mcp-config-types.ts       # MCP configuration types
└── hooks/
    └── use-local-storage.tsx     # Local storage hook
```

### Backend Structure

```
agent/
├── mcp-agent/
│   └── agent.py                  # Main LangGraph agent
├── math_server.py               # Example MCP server
├── pyproject.toml              # Python dependencies
└── langgraph.json              # LangGraph configuration
```

---

## 💬 **Testing the System**

### Basic Agent Interactions

Try these commands in the chat:

- [ ] **Travel Agent**: `"Plan a 3-day trip to Tokyo"`
- [ ] **Research Agent**: `"Research the latest developments in AI"`
- [ ] **MCP Agent**: `"Calculate the square root of 144"` (uses math server)

### Expected Behaviors

- [ ] **Agent Status**: Top-right indicator shows which agent is active
- [ ] **Context Switching**: Canvas UI changes based on agent type
- [ ] **Real-time Updates**: Progress logs appear during agent execution
- [ ] **Results Display**: Each agent shows results in its specialized format

---

## 🔍 **How It Actually Works**

### 1. **Chat Input** → `ChatWindow` (CopilotKit)

- User types command
- CopilotKit analyzes intent and routes to appropriate agent

### 2. **Agent Selection** → `useCoAgent` Hook

- System determines which agent should handle the request
- Agent state management begins

### 3. **Agent Execution** → Backend Processing

- **Travel/Research**: CopilotKit handles routing and processing
- **MCP Agent**: Python backend with LangGraph + MCP tools

### 4. **UI Updates** → `useCoAgentStateRender`

- Real-time status updates
- Agent-specific UI components render
- Progress logs and results display

### 5. **Results** → Contextual Display

- **Travel**: Interactive map with locations
- **Research**: Formatted markdown reports with resources
- **MCP**: Tool execution results and logs

---

## 🛠️ **Customization Tasks**

### Beginner Tasks

- [ ] **Modify agent instructions** in `chat-window.tsx`
- [ ] **Customize UI colors/styling** in agent components
- [ ] **Add new MCP server** in `math_server.py` style
- [ ] **Configure MCP servers** via the UI modal

### Intermediate Tasks

- [ ] **Create new agent type** following the existing pattern
- [ ] **Add new map layers** to travel agent
- [ ] **Extend research agent** with new data sources
- [ ] **Build custom MCP tools** for specific workflows

### Advanced Tasks

- [ ] **Implement agent-to-agent communication**
- [ ] **Add persistent state management**
- [ ] **Create multi-step workflows**
- [ ] **Build custom LangGraph nodes**

---

## ⚙️ **MCP (Model Context Protocol) Deep Dive**

### What is MCP?

- **Standardized protocol** for AI agents to connect to external tools
- **Dynamic configuration** - add/remove tools without code changes
- **Server-based architecture** - tools run as separate processes

### Current MCP Setup

- [ ] **Math Server**: Basic calculator functionality
- [ ] **Configuration UI**: Add/edit MCP servers via modal
- [ ] **Local Storage**: Configurations persist in browser
- [ ] **Dynamic Loading**: Agents load tools based on configuration

### Adding New MCP Servers

1. **Create server script** (like `math_server.py`)
2. **Add to configuration** via UI or directly in code
3. **Test integration** through MCP agent

---

## 🚀 **Production Readiness**

### Environment Setup

- [ ] **Configure OpenAI API key** for LLM functionality
- [ ] **Set up environment variables** in both frontend and backend
- [ ] **Configure CORS** for production deployment
- [ ] **Set up proper error handling** and logging

### Deployment Considerations

- [ ] **Frontend**: Deploy to Vercel/Netlify
- [ ] **Backend**: Deploy Python agent to cloud service
- [ ] **MCP Servers**: Ensure proper server management
- [ ] **Database**: Add persistent storage if needed

---

## 🧹 **What to Ignore Initially**

- **Complex LangGraph workflows** - Start with basic agent interactions
- **Advanced MCP configurations** - Use the math server example first
- **Performance optimizations** - Focus on understanding the flow
- **Production deployment** - Get local development working first

---

## 🎯 **Learning Path**

1. **Week 1**: Understand the multi-agent concept and basic interactions
2. **Week 2**: Dive into one agent type (recommend starting with MCP)
3. **Week 3**: Customize and extend existing functionality
4. **Week 4**: Build your own agent or MCP server

---

## 📚 **Key Technologies to Learn**

- **CopilotKit**: Agent orchestration and chat interface
- **LangGraph**: Python agent workflows and state management
- **MCP**: Tool integration protocol
- **React + TypeScript**: Frontend development
- **Tailwind CSS**: Styling and responsive design

---

**Ready to build your multi-agent system?** Start with the basic setup and work through the testing scenarios! 🚀
