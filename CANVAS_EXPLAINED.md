# Understanding "Canvas" in CopilotKit

## What "Canvas" Means Here

In the `open-multi-agent-canvas` project, the term "canvas" might be misleading if you're coming from other technical contexts. Here, it's used metaphorically to describe the AI agent's workspace or display area, similar to how ChatGPT or Claude use a split-screen interface.

## What It's NOT

The "canvas" in this project is **not**:

- An HTML5 `<canvas>` element for drawing graphics
- A data visualization canvas (like D3.js)
- A node-based flow diagram workspace (like react-flow)

## What It IS

The interface is split into two main sections:

```
┌─────────────┬──────────────┐
│             │              │
│   Chat      │   Agent's    │
│  Window     │  Workspace   │
│             │  ("Canvas")  │
│             │              │
└─────────────┴──────────────┘
```

- **Left Panel**: Chat interface for user interaction
- **Right Panel**: The "canvas" - a dynamic workspace that changes based on which agent is active

## Agent-Specific Workspaces

Each agent gets its own specialized display in the right panel:

1. **Travel Agent**

   - Interactive map interface using Leaflet
   - Displays trip locations and routes

2. **Research Agent**

   - Formatted markdown reports
   - Research logs and progress updates

3. **MCP Agent**
   - Tool execution results
   - Command outputs and responses

## Technical Implementation

The split layout is implemented in `canvas.tsx` using a responsive grid:

```tsx
<div className="grid grid-cols-1 md:grid-cols-12">
  {/* Chat Window - 4 columns on desktop */}
  <div className="md:col-span-4">
    <ChatWindow />
  </div>

  {/* Agent Canvas - 8 columns on desktop */}
  <div className="md:col-span-8">{/* Dynamic agent content */}</div>
</div>
```

## Why This Matters

Understanding that "canvas" here means "workspace" or "display area" helps:

1. Set correct expectations about the project's capabilities
2. Understand the project's relationship to ChatGPT/Claude-style interfaces
3. Clarify that this is about displaying agent outputs, not creating interactive visualizations

The term follows CopilotKit's pattern of providing AI assistants with dedicated spaces to display their work, making it more like a document editor's preview pane than a technical canvas element.
