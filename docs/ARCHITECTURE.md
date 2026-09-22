# IRIS — Current Architecture

## 1. Architecture Overview

IRIS is structured as a modular desktop application designed around separate components for the user interface, core processing, agents, tools, memory, model management, and security.

The existing implementation is currently being audited to verify the exact interaction between these components.

---

## 2. Verified Application Flow

The currently verified desktop interaction follows this flow:

```text
User
  |
  v
IRIS Desktop Interface
  |
  v
Orchestrator
  |
  v
Processing Pipeline
  |
  v
Response
  |
  v
IRIS Desktop Interface
```

The desktop interface creates an `Orchestrator` instance and passes the user's input to its `process()` method.

---

## 3. Desktop Layer

The desktop interface is implemented using PySide6.

The current interface is responsible for:

* Displaying the IRIS application window.
* Displaying the conversation.
* Accepting user input.
* Sending user requests to the orchestrator.
* Displaying the returned response.

The desktop interface does not directly implement the memory or model-processing logic.

---

## 4. Core Layer

The repository contains a dedicated `core` layer for central IRIS processing.

The current repository structure includes:

```text
core/
├── agent_router.py
├── file_command_parser.py
├── intent_engine.py
├── memory_command_parser.py
└── orchestrator.py
```

The detailed behavior and interaction of these components are being verified during the codebase audit.

---

## 5. Agent Layer

The repository contains specialized agents for different categories of tasks.

Current agent modules include:

```text
agents/
├── application_agent.py
├── calender_agent.py
├── file_agent.py
├── memory_agent.py
├── notification_agent.py
├── system_agent.py
└── task_agent.py
```

The exact responsibilities, execution flow, and integration of each agent will be documented after source-level review.

---

## 6. Tool Layer

The repository contains a dedicated tools layer:

```text
tools/
├── application_tools.py
├── file_tools.py
├── system_tools.py
└── tool_registry.py
```

This separation allows agent logic and executable operations to remain separate.

The detailed tool-registration and execution mechanisms are still under review.

---

## 7. Memory and Context Layer

The current ContextEngine connects short-term and long-term memory:

```text
ContextEngine
    |
    +-- ShortTermMemory
    |
    +-- LongTermMemory
```

The ContextEngine currently handles:

* Recent conversation
* Long-term memory retrieval
* Basic automatic memory extraction
* Context-size management

---

## 8. Current Memory Processing

The current implementation uses rule-based memory extraction.

Supported patterns include information such as:

* User name
* User project
* Current project being worked on
* User preferences

The current memory-selection mechanism uses keyword-based matching to identify potentially relevant stored memories.

This provides a basic foundation for future semantic memory retrieval.

---

## 9. Context Construction

The current ContextEngine builds a context containing:

```text
Current User Input
        +
Recent Conversation
        +
Relevant Long-Term Memories
        |
        v
Context Size Control
        |
        v
Final Context
```

The current implementation limits:

* Number of recent messages.
* Number of retrieved memories.
* Maximum length of individual text content.

Oversized text is truncated to remain within configured limits.

---

## 10. Model Layer

The repository contains a dedicated model-management component:

```text
models/
└── model_manager.py
```

The exact model initialization, inference, and configuration behavior is being reviewed as part of the codebase audit.

---

## 11. Security Layer

The repository contains:

```text
security/
└── permissions.py
```

This component is intended to provide permission-related functionality for IRIS operations.

Its current implementation and integration will be documented after source-level review.

---

## 12. Current High-Level Architecture

The currently identified architecture can be represented as:

```text
                    ┌─────────────────┐
                    │   IRIS Desktop  │
                    │       UI        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Orchestrator   │
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
          Intent Engine   Agent Router  Context
                │            │            │
                │            ▼            │
                │          Agents         │
                │            │            │
                │            ▼            │
                │          Tools          │
                │                         │
                └────────────┬────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Model Manager  │
                    └─────────────────┘
```

This diagram represents the current architectural structure identified from the repository and reviewed components. The exact execution relationships will be refined as the remaining source files are audited.

---

## 13. Architectural Development Direction

The development direction is to maintain clear separation between:

```text
Presentation
      |
Application / Orchestration
      |
Agent Intelligence
      |
Tools / Actions
      |
Memory / Context
      |
Model Layer
```

Future architectural changes will be based on findings from the ongoing source-code audit rather than replacing the existing implementation without evaluation.
