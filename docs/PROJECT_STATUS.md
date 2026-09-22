# IRIS — Project Status

**Project:** IRIS — Context-Aware Agentic Personal Intelligence System

**Development Stage:** Foundation / Codebase Audit

**Status:** Active Development

---

## 1. Project Overview

IRIS is a context-aware agentic personal intelligence system designed to provide an intelligent desktop-based personal assistant.

The current repository contains a modular foundation consisting of a desktop interface, core processing components, agents, tools, memory components, model integration, and security components.

The existing implementation is currently being reviewed and documented before further development and architectural changes are introduced.

---

## 2. Verified Components

The following components have been reviewed during the initial codebase audit.

### Application Entry Point

`main.py` initializes the PySide6 application, creates the main IRIS window, displays it, and starts the Qt event loop.

### Desktop Interface

`ui/desktop.py` currently provides:

* IRIS desktop window
* Conversation display
* User input field
* Send button
* Enter-key message submission

The desktop interface passes user input to the core orchestrator and displays the returned response.

### Context Engine

The current ContextEngine provides:

* Short-term conversation memory
* Long-term memory integration
* Basic automatic memory extraction
* Long-term memory retrieval
* Recent conversation selection
* Context-size limiting

The current memory extraction mechanism is rule-based, while memory selection currently uses keyword-based matching.

---

## 3. Initial Limitations Identified

The initial audit has identified the following areas for further development:

* Rule-based memory extraction
* Keyword-based memory retrieval
* Limited semantic understanding of stored memories
* Basic context selection
* Fixed context-size limits
* Text truncation for oversized context
* Synchronous orchestrator execution from the desktop UI
* Limited error handling in the current UI interaction path

The complete orchestration, agent, model, tool, security, and storage implementations are still being audited.

---

## 4. Development Approach

The existing implementation will be treated as the starting point for further development.

The development process will follow these stages:

1. Audit the existing implementation.
2. Document the current architecture.
3. Identify strengths and limitations.
4. Preserve useful existing components.
5. Improve weak or tightly coupled components.
6. Add new capabilities incrementally.
7. Test individual components.
8. Test integrated workflows.
9. Evaluate the completed system using measurable criteria.
10. Document the final architecture and results.

---

## 5. Current Phase

### Codebase Audit

Current activities include:

* Reviewing source files.
* Understanding component responsibilities.
* Mapping dependencies.
* Identifying architectural limitations.
* Documenting the current system.
* Establishing the development roadmap.

---

## 6. Immediate Next Steps

The next components to be reviewed are:

1. Core orchestrator
2. Model manager
3. Intent engine
4. Agent router
5. Command parsers
6. Agents
7. Tools
8. Memory storage
9. Security and permissions
10. Supporting utilities

After the audit is complete, an updated architecture and implementation plan will be established.
