# 🚀 Development Notes - Multi-Agent Canvas

## 🏗️ Architecture Overview

This project has a **dual-connection architecture**:

### Frontend → Agents Connection

- **Travel & Research Agents**: Direct connection via CopilotKit Cloud API

  - No local backend required
  - Works immediately when frontend starts
  - Uses `NEXT_PUBLIC_COPILOT_CLOUD_API_KEY`

- **MCP Agent**: Local connection via LangGraph server
  - Requires LangGraph server on `localhost:8123`
  - LangGraph connects to local MCP servers
  - Only works when LangGraph server is running

## 🔄 Complete Startup Sequence

### 1. Frontend (Always Required)

```bash
cd frontend
npm run dev  # localhost:3000d
```

### 2. MCP Servers (For MCP Agent functionality)

```bash
cd agent
# Start weather server in background
nohup poetry run python weather_server.py > weather_server.log 2>&1 &
# Math server is already configured to start automatically
```

### 3. LangGraph Server (For MCP Agent functionality)

```bash
cd agent  # IMPORTANT: Must be in agent/ directory
poetry run langgraph dev --host localhost --port 8123
```

## 🧪 Testing Each Component

### Travel Agent ✈️

```
"Plan a 3-day trip to Tokyo"
```

- Should show map interface
- Works without any backend

### Research Agent 📚

```
"Research the latest developments in AI"
```

- Should show research logs and reports
- Works without any backend

### MCP Agent 🔧

```
"Calculate the square root of 144"
"What's the weather in Tokyo?"
```

- Requires LangGraph server running
- Uses local MCP servers (math, weather)

## 🐛 Common Issues & Solutions

### "Poetry could not find pyproject.toml"

- **Cause**: Running poetry from wrong directory
- **Solution**: Always run poetry commands from `agent/` directory

### "MCP Agent not responding"

- **Cause**: LangGraph server not running
- **Solution**: Start LangGraph server from `agent/` directory

### "Weather server not working"

- **Cause**: Server not in MCP configuration
- **Solution**: Check `DEFAULT_MCP_CONFIG` in `agent/mcp-agent/agent.py`

### "Server out of date" warning

- **Cause**: LangGraph CLI version mismatch
- **Solution**: Warning is cosmetic, server works fine

## 📂 Key Files

### Frontend

- `frontend/src/providers/Providers.tsx` - CopilotKit configuration
- `frontend/src/components/coagents-provider.tsx` - Agent state management
- `frontend/src/components/canvas.tsx` - Main UI orchestrator

### Backend

- `agent/mcp-agent/agent.py` - LangGraph workflow + MCP config
- `agent/langgraph.json` - LangGraph server configuration
- `agent/weather_server.py` - Custom weather MCP server

## 🔍 Connection Flow

```
User Input → ChatWindow (CopilotKit) → Agent Router → {
  Travel/Research: CopilotKit Cloud API
  MCP: Local LangGraph → MCP Servers → Tools
}
```

## 📝 Development Tips

1. **Always start frontend first** - provides immediate feedback
2. **LangGraph server must stay running** - use `nohup` for background
3. **Check processes**: `lsof -i :8123` and `ps aux | grep weather`
4. **Debug MCP**: Check logs in `agent/*.log` files
5. **Frontend hot-reload works** - backend changes need restart
