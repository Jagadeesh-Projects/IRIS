# IRIS — Development Roadmap

## 1. Purpose

This roadmap defines the planned development stages for IRIS.

The project will be developed incrementally. Existing components will first be understood and evaluated before major architectural changes are introduced.

---

# Phase 1 — Existing Foundation

**Status:** 🟡 In Progress / Under Audit

The initial repository provides the foundation for the IRIS desktop application.

### Areas

* Desktop user interface
* Core processing layer
* Orchestration
* Intent processing
* Agent routing
* Specialized agents
* Tools
* Memory
* Model management
* Security

### Current Objective

Understand and document the existing implementation before extending it.

---

# Phase 2 — Codebase and Architecture Stabilization

**Status:** 🔵 Planned

### Objectives

* Complete source-code audit.
* Define clear component responsibilities.
* Identify unnecessary coupling.
* Improve error handling.
* Establish consistent interfaces.
* Improve configuration management.
* Establish structured logging.
* Introduce automated tests.

### Expected Outcome

A stable and clearly understood foundation for further IRIS development.

---

# Phase 3 — Memory and Context

**Status:** 🔵 Planned

### Objectives

Improve IRIS's ability to store, retrieve, and use relevant information.

### Planned Areas

* Improved memory extraction
* Structured memory representation
* Semantic memory retrieval
* Relevance-based memory selection
* Improved context construction
* Context compression
* Context-size optimization
* Memory retrieval evaluation

### Current Limitation

The existing implementation primarily uses rule-based memory extraction and keyword-based memory selection.

---

# Phase 4 — Agent Intelligence

**Status:** 🔵 Planned

### Objectives

Improve IRIS's ability to understand requests, plan actions, and execute multi-step tasks.

### Planned Areas

* Improved intent understanding
* Agent selection
* Structured task planning
* Multi-step task execution
* Tool selection
* Agent coordination
* Failure handling
* Task state management

---

# Phase 5 — Tool and Desktop Capabilities

**Status:** 🔵 Planned

Expand IRIS's ability to interact with the user's computing environment in a controlled manner.

### Planned Areas

* File operations
* Application interaction
* System operations
* Task management
* Calendar functionality
* Notifications
* Controlled desktop automation

All operations should remain subject to appropriate permission and safety controls.

---

# Phase 6 — Context Awareness

**Status:** 🔵 Planned

Expand IRIS's understanding beyond the immediate conversation.

### Potential Context Sources

* Current user task
* User goal
* Recent actions
* Open applications
* Relevant files
* System state
* Time and date
* Active workflow

### Objective

Provide the model with relevant context while avoiding unnecessary information and excessive context size.

---

# Phase 7 — Voice Interaction

**Status:** 🔵 Planned

Explore natural voice-based interaction with IRIS.

### Potential Capabilities

* Speech-to-text
* Text-to-speech
* Voice commands
* Conversational voice interaction
* Interruption handling

---

# Phase 8 — Reliability and Evaluation

**Status:** 🔵 Planned

Establish measurable evaluation criteria for the IRIS system.

### Potential Metrics

* Task completion rate
* Tool-selection accuracy
* Memory retrieval accuracy
* Context relevance
* Response latency
* Failure recovery
* Reliability
* Resource usage

### Objective

Move from feature-based development toward measurable system evaluation.

---

# Phase 9 — Integration and Final Release

**Status:** 🔵 Planned

Integrate validated components into the final IRIS system.

### Final Activities

* Unit testing
* Integration testing
* End-to-end testing
* Performance evaluation
* Reliability testing
* Documentation
* Demonstration scenarios
* Experimental evaluation
* Final project report
* Final release
