# IRIS — Development Log

This document records significant development, investigation, architectural, and implementation activities during the development of IRIS.

---

## 2026-09-22 — Initial Codebase Audit

### Objective

Begin a structured review of the existing IRIS implementation before introducing architectural or feature-level changes.

The objective of the audit is to understand the existing implementation, identify strengths and limitations, and establish a reliable foundation for future development.

---

## Files Reviewed

### `main.py`

The application entry point was reviewed.

The file is responsible for:

1. Creating the PySide6 application.
2. Creating the `IrisWindow`.
3. Displaying the application window.
4. Starting the Qt event loop.

No major architectural changes were identified for the entry point during the initial review.

---

### `ui/desktop.py`

The desktop interface was reviewed.

The current interface provides:

* IRIS application window
* Conversation display
* User input
* Send button
* Enter-key submission

The interface creates an `Orchestrator` instance and passes user input to its `process()` method.

### Initial Observation

The current implementation invokes the orchestrator synchronously from the UI event handler.

As IRIS develops more complex multi-step operations, background execution and asynchronous processing should be evaluated to prevent long-running operations from blocking the desktop interface.

---

### ContextEngine

The ContextEngine was reviewed as part of the initial memory and context audit.

The current implementation provides:

* Short-term conversation storage
* Long-term memory integration
* Automatic memory extraction
* Memory retrieval
* Recent conversation selection
* Context-size control

### Initial Observations

The current memory system uses rule-based extraction.

Examples include identifying information such as:

* User name
* User project
* Current project being worked on
* User preferences

Memory selection currently uses keyword-based matching.

The ContextEngine also applies fixed limits to recent messages, retrieved memories, and individual text content.

Oversized content is truncated to remain within the configured limits.

---

## Initial Technical Findings

The first stage of the audit identified the following areas for further investigation:

### Memory

* Memory extraction is currently rule-based.
* Memory retrieval is currently keyword-based.
* Semantic memory retrieval is not yet implemented in the reviewed ContextEngine.
* Memory extraction ordering should be tested for overlapping patterns.

### Context

* Context construction currently combines current input, recent conversation, and selected long-term memories.
* Context limits are primarily based on fixed counts and text length.
* Future versions may require relevance-based selection and context compression.

### Desktop Execution

* The current UI calls the orchestrator synchronously.
* Longer-running model or tool operations may block the GUI event loop.
* Background execution should be evaluated during future architectural work.

---

## Development Principle

The existing implementation will not be replaced without evaluation.

The development process will:

1. Understand the existing implementation.
2. Document verified behavior.
3. Identify limitations.
4. Preserve useful components.
5. Improve components where necessary.
6. Add new capabilities incrementally.
7. Test changes.
8. Measure system behavior.
9. Document significant changes.

---

## Next Audit Target

The next major component scheduled for review is:

```text
core/orchestrator.py
```

The orchestrator will be examined to determine how user requests flow through the core processing system and how the different IRIS components are coordinated.

---

## Future Log Entries

Future entries will document:

* Architecture changes
* Feature implementation
* Bug fixes
* Testing
* Performance improvements
* Memory improvements
* Agent development
* Tool integration
* Evaluation results
* Major design decisions
