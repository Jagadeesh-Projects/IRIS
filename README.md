

````markdown
# IRIS: Context-Aware Agentic Personal Intelligence System (CAPIS)

<p align="center">

### 🧠 A Local-First, Context-Aware Agentic AI Assistant for Intelligent Personal Computing

</p>

## 📌 Overview

**IRIS (Context-Aware Agentic Personal Intelligence System)** is a **local-first, desktop-based Agentic AI platform** designed to function as an intelligent personal computing companion.

Traditional AI assistants are primarily reactive: users provide a prompt, receive a response, and often need to repeat context when continuing a task. IRIS aims to address this limitation by combining:

- **Persistent Memory**
- **Context-Aware Reasoning**
- **Multi-Agent Collaboration**
- **Desktop and System Interaction**
- **Intelligent File Operations**
- **Local AI Model Execution**
- **Permission-Aware Task Execution**

The system uses a centralized **Orchestrator** to understand user requests, identify the appropriate intent, route the request to a specialized agent, execute the required operation, and generate a natural-language response.

IRIS is designed around a **local-first architecture**, allowing user context and memory to remain on the user's device by default.

---

## 🎯 Problem Statement

Modern AI assistants can provide powerful natural-language responses, but personal computing workflows often require more than conversation.

Users may need to:

- Repeatedly provide the same personal context.
- Search for files manually.
- Switch between applications.
- Perform repetitive desktop operations.
- Restore previous workflows.
- Retrieve information from previous interactions.
- Manage different tasks using different applications.

These limitations motivate the development of an intelligent desktop assistant capable of maintaining context and coordinating different capabilities.

The central problem addressed by IRIS is:

> **How can a local-first Agentic AI system combine persistent personalized memory, contextual reasoning, multi-agent collaboration, and desktop interaction to provide more intelligent and continuous personal computing assistance?**

---

# 💡 Proposed Approach

IRIS follows a modular multi-agent architecture.

Instead of implementing every capability inside a single large program, the system separates responsibilities into specialized components.

The general workflow is:

```text
                    ┌─────────────────────────┐
                    │       User Input        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Orchestrator      │
                    │   Central Coordinator   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Intent Engine      │
                    │ Understand User Request │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Agent Router       │
                    │ Select Specialized Agent│
                    └────────────┬────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
       ┌────────────┐     ┌────────────┐     ┌────────────┐
       │System Agent│     │ File Agent │     │Memory Agent│
       └──────┬─────┘     └──────┬─────┘     └──────┬─────┘
              │                  │                  │
              ▼                  ▼                  ▼
       System Tools        File Tools         Memory Store
              │                  │                  │
              └──────────────────┼──────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Context Engine    │
                    │ Memory + Conversation   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Local LLM Model     │
                    │      Qwen3 4B Instruct  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      User Response      │
                    └─────────────────────────┘
````

---

# 🏗️ System Architecture

IRIS consists of several major architectural layers.

## 1. User Interface Layer

The desktop interface provides the primary interaction point between the user and IRIS.

The user can communicate with the assistant using natural language.

```text
User
  │
  ▼
Desktop Interface
  │
  ▼
Orchestrator
```

---

## 2. Orchestration Layer

The **Orchestrator** acts as the central coordination component.

Its responsibilities include:

1. Receiving user input.
2. Maintaining conversation context.
3. Detecting user intent.
4. Routing requests to appropriate agents.
5. Executing agent operations.
6. Formatting results.
7. Generating natural-language responses.
8. Updating conversational memory.

```text
User Request
     │
     ▼
Orchestrator
     │
     ├── Intent Detection
     │
     ├── Context Retrieval
     │
     ├── Agent Routing
     │
     ├── Agent Execution
     │
     └── Response Generation
```

---

# 🧠 Context-Aware Intelligence

One of the main concepts behind IRIS is **context-aware interaction**.

The system maintains two forms of memory:

### Short-Term Memory

Short-term memory maintains recent conversational interactions.

It can contain:

* Recent user messages
* Recent assistant responses
* Current conversation context

```text
User: My name is Jagadeesh.

Assistant: Nice to meet you, Jagadeesh.

User: What is my name?

IRIS → Retrieves recent/contextual information
```

### Long-Term Memory

Long-term memory stores information that can remain useful across conversations.

Examples include:

```text
User Name
User Preferences
Projects
Other Persistent Context
```

The current persistent memory layer uses a local database.

```text
                Context Engine
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
   Short-Term Memory       Long-Term Memory
          │                       │
          ▼                       ▼
   Recent Conversation       Persistent Data
                                  │
                                  ▼
                              SQLite DB
```

---

# 🔄 Context Processing

When a user sends a request, IRIS can construct a contextual representation containing:

```text
Current User Input
       +
Recent Conversation
       +
Relevant Long-Term Memories
       +
Agent Result
       ↓
Context-Aware Response
```

This allows the system to move beyond isolated question-answer interactions.

---

# 🤖 Multi-Agent Architecture

IRIS uses specialized agents instead of placing every operation inside a single component.

The repository contains agents for different categories of tasks.

## Current / Core Agents

### 🖥️ System Agent

Responsible for system-related operations such as retrieving system information.

Example:

```text
User:
How much RAM am I using?

        ↓

Intent Engine
        ↓
SYSTEM_MONITORING
        ↓
System Agent
        ↓
System Tools
        ↓
System Information
        ↓
Natural Language Response
```

---

### 📁 File Agent

Responsible for file-related operations.

Example requests:

```text
Find files in my project
Search for a Python file
Find a particular document
```

The File Agent works with the file tools and returns structured file information to the orchestration layer.

---

### 🧠 Memory Agent

The Memory Agent is responsible for memory-related operations.

Its intended responsibilities include:

* Storing user information.
* Retrieving remembered information.
* Processing memory-related commands.
* Interacting with the memory subsystem.

---

## Additional Agents

The architecture also contains specialized components for:

* Application interaction
* Calendar management
* Notifications
* Task management

These components form part of the modular architecture and can be expanded as development progresses.

---

# 🧭 Intent Engine

The **Intent Engine** determines what the user is trying to accomplish.

For example:

```text
User Input
    │
    ▼
Intent Engine
    │
    ├── GENERAL_QUERY
    │
    ├── SYSTEM_MONITORING
    │
    ├── FILE_OPERATION
    │
    ├── MEMORY_OPERATION
    │
    ├── APPLICATION_OPERATION
    │
    └── TASK_OPERATION
```

Intent detection allows IRIS to determine which specialized capability should handle a request.

---

# 🔀 Agent Router

After identifying an intent, the **Agent Router** selects the corresponding agent.

```text
Intent
  │
  ▼
Agent Router
  │
  ├── SYSTEM_MONITORING → System Agent
  │
  ├── FILE_OPERATION → File Agent
  │
  ├── MEMORY_OPERATION → Memory Agent
  │
  ├── APPLICATION_OPERATION → Application Agent
  │
  └── TASK_OPERATION → Task Agent
```

This separation makes the system modular and easier to extend.

---

# 🧰 Tool Layer

IRIS separates high-level agent reasoning from low-level system operations.

The tool layer contains utilities for:

### File Operations

```text
tools/file_tools.py
```

### System Operations

```text
tools/system_tools.py
```

### Application Operations

```text
tools/application_tools.py
```

### Tool Registry

```text
tools/tool_registry.py
```

The Tool Registry provides a centralized mechanism for exposing available tools to the system.

---

# 🧩 Memory Architecture

IRIS includes a dedicated memory subsystem.

```text
memory/
│
├── database.py
├── short_term.py
└── long_term.py
```

### Short-Term Memory

Maintains recent conversation messages.

### Long-Term Memory

Provides persistent storage and retrieval.

The long-term memory layer uses a local database and supports operations such as:

```text
remember(memory_type, key, value)

recall(memory_type, key)

all_memories()
```

Example:

```text
remember(
    "user",
    "name",
    "Jagadeesh"
)
```

Later:

```text
recall(
    "user",
    "name"
)
```

returns the stored value.

---

# 🧠 Local AI Model

IRIS uses a locally hosted Large Language Model through **Ollama**.

Current development model:

```text
Qwen3 4B Instruct
```

The local model is responsible for natural-language response generation and contextual interpretation.

The local-first approach helps reduce dependence on external AI APIs for the core conversational workflow.

---

# 🔒 Privacy and Local-First Design

Privacy is an important design consideration of IRIS.

The architecture is designed around keeping personal context and memory on the user's machine by default.

### Core principle

> **User context should remain local unless the user explicitly chooses otherwise.**

The system uses:

* Local LLM execution
* Local persistent memory
* Local SQLite storage
* Permission-aware system operations

This project is intended as a research and engineering prototype and should not be considered a security-certified system.

---

# 🛡️ Permission and Safety Layer

IRIS contains a dedicated security component:

```text
security/permissions.py
```

The purpose of this layer is to support permission-aware execution of potentially sensitive operations.

The broader architectural principle is:

```text
User Request
     │
     ▼
Intent Detection
     │
     ▼
Agent
     │
     ▼
Permission Check
     │
     ▼
Tool Execution
```

This is particularly important for future desktop automation capabilities.

---

# 🗂️ Project Structure

The current repository is organized into modular components:

```text
IRIS/
│
├── agents/
│   ├── application_agent.py
│   ├── calender_agent.py
│   ├── file_agent.py
│   ├── memory_agent.py
│   ├── notification_agent.py
│   ├── system_agent.py
│   └── task_agent.py
│
├── config/
│   └── settings.py
│
├── core/
│   ├── agent_router.py
│   ├── file_command_parser.py
│   ├── intent_engine.py
│   ├── memory_command_parser.py
│   └── orchestrator.py
│
├── data/
│   ├── iris.db
│   └── logs/
│       └── iris.log
│
├── memory/
│   ├── database.py
│   ├── long_term.py
│   └── short_term.py
│
├── models/
│   └── model_manager.py
│
├── security/
│   └── permissions.py
│
├── tools/
│   ├── application_tools.py
│   ├── file_tools.py
│   ├── system_tools.py
│   └── tool_registry.py
│
├── ui/
│   └── desktop.py
│
├── utils/
│   └── logger.py
│
├── requirements.txt
├── main.py
└── README.md
```

> `.venv/`, cache directories, local databases, logs, and other machine-specific files should not be committed to the GitHub repository unless intentionally required.

---

# ⚙️ Technology Stack

## Programming

* Python
* Object-Oriented Programming
* Modular Software Architecture

## Artificial Intelligence

* Large Language Models
* Agentic AI
* Context-Aware Reasoning
* Natural Language Processing
* Local LLM Inference

## Local AI Runtime

* Ollama
* Qwen3 4B Instruct

## Memory

* SQLite
* Short-Term Memory
* Long-Term Memory

## System Architecture

* Multi-Agent Architecture
* Intent Detection
* Agent Routing
* Tool-Based Execution
* Context Management

## Development

* Git
* GitHub
* Python Virtual Environment
* VS Code

---

# 💻 Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd IRIS
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🦙 Ollama Setup

IRIS currently uses Ollama for local LLM execution.

Install Ollama and verify the installation:

```bash
ollama --version
```

Then download/run the required model:

```bash
ollama run qwen3:4b-instruct
```

Once the model is available locally, IRIS can communicate with the local Ollama runtime.

---

# ▶️ Running IRIS

Activate the virtual environment first.

```powershell
.venv\Scripts\activate
```

Then start the application:

```bash
python main.py
```

The desktop interface should start and allow interaction with IRIS.

---

# 💬 Example Interactions

## System Monitoring

```text
User:
How much RAM am I using?

IRIS:
[System information retrieved and presented to the user]
```

---

## File Search

```text
User:
Find files in my IRIS project.

IRIS:
[Relevant file information is returned]
```

---

## Memory

```text
User:
My name is Jagadeesh.

IRIS:
I'll remember that.

User:
What is my name?

IRIS:
Your name is Jagadeesh.
```

---

## General Question

```text
User:
Explain what an operating system is.

IRIS:
[Context-aware response generated using the local LLM]
```

---

# 🧪 Current Implementation Status

| Component                   | Status                    |
| --------------------------- | ------------------------- |
| Desktop Interface           | 🟢 Implemented            |
| Ollama Integration          | 🟢 Implemented            |
| Qwen3 Local Model           | 🟢 Implemented            |
| Model Manager               | 🟢 Implemented            |
| Intent Engine               | 🟢 Implemented            |
| Agent Router                | 🟢 Implemented            |
| Orchestrator                | 🟢 Implemented            |
| System Agent                | 🟢 Implemented            |
| File Agent                  | 🟢 Implemented            |
| System Tools                | 🟢 Implemented            |
| File Tools                  | 🟢 Implemented            |
| Tool Registry               | 🟢 Implemented            |
| Short-Term Memory           | 🟢 Implemented            |
| Long-Term Memory            | 🟢 Implemented            |
| SQLite Memory Storage       | 🟢 Implemented            |
| Context Engine              | 🟢 Implemented / Evolving |
| Memory Agent                | 🟡 Under Development      |
| Application Agent           | 🟡 Under Development      |
| Calendar Agent              | 🟡 Under Development      |
| Notification Agent          | 🟡 Under Development      |
| Task Agent                  | 🟡 Under Development      |
| Advanced Desktop Automation | 🔵 Planned                |
| Advanced Semantic Memory    | 🔵 Planned                |

### Status Legend

```text
🟢 Implemented
🟡 Under Development
🔵 Planned
```

---

# 📈 Engineering Considerations

During development, IRIS encountered an important context-management challenge.

Large file-search results can exceed the context window of a local language model.

For example:

```text
File Search
    │
    ▼
Thousands of Results
    │
    ▼
Very Large Prompt
    │
    ▼
Context Window Overflow
```

The architecture therefore incorporates result limiting and structured context handling.

The intended approach is:

```text
Large Tool Output
       │
       ▼
Filter / Limit
       │
       ▼
Structured Result
       │
       ▼
LLM
       │
       ▼
Natural Language Response
```

This reduces unnecessary context consumption and improves reliability.

---

# 🔬 Research Focus

The research and engineering focus of IRIS includes:

## 1. Context-Aware AI

Investigating how persistent context can improve interactions between users and desktop AI assistants.

---

## 2. Persistent Personalized Memory

Exploring how short-term and long-term memory can allow an AI assistant to retain useful user information across interactions.

---

## 3. Multi-Agent Collaboration

Investigating how specialized agents can divide responsibilities and coordinate through a central orchestration layer.

---

## 4. Intelligent Desktop Assistance

Exploring how natural-language requests can be connected to desktop, file, application, and system operations.

---

## 5. Local-First AI

Investigating the use of local AI models and local storage to reduce unnecessary dependence on external services.

---

## 6. Adaptive AI Computing

The broader project architecture considers adapting AI capabilities according to the computational resources available on the host system.

---

# 📊 Evaluation Metrics

The project can be evaluated using the following metrics:

### Task Completion Success Rate

Measures how successfully IRIS completes user requests.

```text
Successful Tasks
---------------- × 100
Total Tasks
```

### Memory Retrieval Accuracy

Measures whether the correct stored information is retrieved for relevant queries.

### Response Time

Measures the time required from user input to generated response.

### Resource Utilization

Measures system resource usage during execution.

Potential measurements include:

* CPU utilization
* RAM usage
* Model resource requirements

### User Satisfaction

Can be evaluated through structured user feedback and usability studies.

---

# 🧪 Evaluation Framework

A possible evaluation workflow is:

```text
              Test Dataset / User Tasks
                         │
                         ▼
                 ┌───────────────┐
                 │     IRIS      │
                 └───────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      Task Result    Memory Result   Response Time
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                 Evaluation Report
```

---

# 🔐 Scope and Limitations

## Included

* Local AI assistant
* Context-aware interaction
* Persistent memory
* Multi-agent architecture
* Intent detection
* Agent routing
* File operations
* System monitoring
* Local LLM inference
* SQLite-based memory
* Permission-aware architecture

## Not Yet Fully Included

* Fully autonomous desktop control
* Complete application automation
* Production-grade security
* Large-scale distributed deployment
* Human-level general intelligence
* Guaranteed correctness of AI-generated responses

IRIS is a research-oriented prototype and is being developed incrementally.

---

# 🚀 Future Work

Potential future extensions include:

* Advanced semantic memory retrieval
* Vector-based memory search
* Improved context ranking
* LLM-based memory extraction
* More sophisticated task planning
* Application automation
* Calendar integration
* Notification management
* Workflow restoration
* Proactive assistance
* Improved permission management
* Adaptive model selection
* Resource-aware model configuration
* Improved desktop automation
* Comprehensive evaluation framework
* Multi-modal interaction
* Voice-based interaction

---

# 🧭 Development Roadmap

```text
Phase 1
│
├── Project Architecture
├── Local LLM Integration
├── Intent Engine
└── Agent Router
        │
        ▼
Phase 2
│
├── System Agent
├── File Agent
├── Tool Layer
└── Orchestrator
        │
        ▼
Phase 3
│
├── Short-Term Memory
├── Long-Term Memory
├── SQLite Storage
└── Context Engine
        │
        ▼
Phase 4
│
├── Memory Agent
├── Task Agent
├── Application Agent
├── Calendar Agent
└── Notification Agent
        │
        ▼
Phase 5
│
├── Advanced Context Retrieval
├── Intelligent Planning
├── Desktop Automation
└── Workflow Restoration
        │
        ▼
Phase 6
│
├── Evaluation
├── Optimization
├── Security Improvements
└── Research Analysis
```

---

# 📁 Important Files

| File                            | Purpose                          |
| ------------------------------- | -------------------------------- |
| `main.py`                       | Application entry point          |
| `core/orchestrator.py`          | Central request coordinator      |
| `core/intent_engine.py`         | User intent detection            |
| `core/agent_router.py`          | Agent selection and routing      |
| `core/file_command_parser.py`   | File command interpretation      |
| `core/memory_command_parser.py` | Memory command interpretation    |
| `memory/database.py`            | Persistent database operations   |
| `memory/short_term.py`          | Short-term conversational memory |
| `memory/long_term.py`           | Long-term memory management      |
| `models/model_manager.py`       | Local AI model management        |
| `agents/system_agent.py`        | System-related operations        |
| `agents/file_agent.py`          | File-related operations          |
| `agents/memory_agent.py`        | Memory-related operations        |
| `tools/system_tools.py`         | System-level tools               |
| `tools/file_tools.py`           | File-level tools                 |
| `tools/application_tools.py`    | Application-level tools          |
| `tools/tool_registry.py`        | Tool registration                |
| `security/permissions.py`       | Permission and safety layer      |
| `ui/desktop.py`                 | Desktop interface                |
| `utils/logger.py`               | Application logging              |
| `data/iris.db`                  | Local persistent memory database |
| `data/logs/iris.log`            | Application logs                 |

---

# 📝 Example Architecture Flow

A typical request travels through IRIS as follows:

```text
                    User
                     │
                     ▼
              Desktop Interface
                     │
                     ▼
                Orchestrator
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
   Context Engine         Intent Engine
          │                     │
          │                     ▼
          │                Agent Router
          │                     │
          │          ┌──────────┼──────────┐
          │          │          │          │
          │          ▼          ▼          ▼
          │       System      File      Memory
          │       Agent       Agent      Agent
          │          │          │          │
          │          ▼          ▼          ▼
          │       Tools       Tools      Memory
          │          │          │          │
          └──────────┴──────────┴──────────┘
                     │
                     ▼
              Structured Result
                     │
                     ▼
                Local LLM
                     │
                     ▼
               Final Response
```

---

# 🌱 Design Principles

IRIS is developed around the following principles:

### Modular

Each major capability is separated into an independent component.

### Context-Aware

The system considers recent interactions and relevant persistent information.

### Local-First

Local processing and storage are preferred for personal context.

### Extensible

New agents and tools can be added without redesigning the entire system.

### Permission-Aware

Potentially sensitive operations should be controlled through explicit permission mechanisms.

### Research-Oriented

The system is developed as a research and engineering project rather than as a claim of creating a completely autonomous general-purpose AI.

---

# 📚 Key Research References

The project is motivated by research and existing systems in areas including AI assistants, Agentic AI, AI operating systems, memory architectures, semantic file systems, and reasoning-and-acting agents.

Key references associated with the project include:

1. **Microsoft Copilot**
2. **Google Gemini**
3. **Microsoft 365 Copilot**
4. Mei et al. (2024), **"AIOS: LLM Agent Operating System"**
5. Xiong et al. (2023), **"LLM as OS, Agents as Apps: Envisioning AIOS, Agents and the AIOS-Agent Ecosystem"**
6. Li et al. (2024), **"From Commands to Prompts: LLM-based Semantic File System for AIOS"**
7. Chen et al. (2024), **"Turn Every Application into an Agent: Towards Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents"**
8. Kang et al. (2025), **"Memory OS of AI Agent"**
9. Wang et al. (2025), **"MemOS: A Memory Operating System for Large Language Model Applications"**
10. Park et al. (2023), **"Generative Agents: Interactive Simulacra of Human Behavior"**
11. Shinn et al. (2023), **"Reflexion: Language Agents with Verbal Reinforcement Learning"**
12. Yao et al. (2023), **"ReAct: Synergizing Reasoning and Acting with Language Models"**
13. Qin et al. (2023), **"Tool Learning with Foundation Models"**
14. OpenAI (2025), **"ChatGPT Agent"**
15. Perplexity AI (2025), **"Perplexity Assistant / Personal AI Assistant"**

---

# 🎓 Research Contribution

The project does **not** claim to invent:

* Large Language Models
* Agentic AI
* Persistent memory
* AI assistants
* Multi-agent systems
* Desktop automation

Instead, the research and engineering contribution focuses on investigating the **integration of these concepts into a local-first personal computing assistant**.

The project particularly focuses on the combination of:

```text
Persistent Memory
        +
Contextual Reasoning
        +
Multi-Agent Architecture
        +
Tool-Based Execution
        +
Desktop Interaction
        +
Local AI
        ↓
IRIS
```

The resulting system provides a platform for studying context-aware and personalized Agentic AI for desktop computing.

---

# 👥 Project Team

| S. No. | Team Member                     | Roll Number |
| ------ | ------------------------------- | ----------- |
| 1      | **T. Jagadeesh**                | 23BQ1A61E1  |
| 2      | **V. Raj Gopala Krishnamurthy** | 23BQ1A61E5  |
| 3      | **U. Amrutha Varshini**         | 23BQ1A61E3  |
| 4      | **Sk. Anirudh**                 | 23BQ1A61C6  |

---

# 👨‍🏫 Project Guide

**Mr. Ch. Vijayananda Ratnam**

---

# 📌 Project Objective

The central objective of IRIS is to develop and investigate a:

> **Context-Aware Agentic Personal Intelligence System capable of maintaining persistent user context, coordinating specialized agents, interacting with desktop resources, and generating personalized responses using a local-first AI architecture.**

