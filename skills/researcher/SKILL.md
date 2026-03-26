# Researcher Skill

Autonomous, Self-Propagating Research Architecture for Project Zero.

## Overview

This skill implements a sophisticated research architecture where Project Zero acts as the central orchestrator (Puppeteer), breaking down complex research tasks into executable scripts that are distributed across specialized agents.

## Architecture

```mermaid
graph TD
    User([User Query]) --> PM[<b>Project Zero</b><br/><i>(Central Orchestrator)</i>]
    
    subgraph "Control Plane (The Strings)"
        PM --> Plan[Task Decomposition & Planning]
        Plan --> Mem[(Global Shared Memory)]
        Mem --> Router{Task Router}
    end

    subgraph "Execution Layer (The Puppets)"
        Router --> S1[<b>Search Agent</b><br/><i>Scours Web & APIs</i>]
        Router --> S2[<b>Finance Agent</b><br/><i>Real-time Market Data</i>]
        Router --> S3[<b>Medical Agent</b><br/><i>PubMed & Clinical Trials</i>]
        Router --> Sn[<b>Specialist Agent</b><br/><i>Domain-specific Tools</i>]
    end

    subgraph "Synthesis & Feedback"
        S1 & S2 & S3 & Sn --> Verifier[Citation & Fact Verifier]
        Verifier --> Critic[Self-Correction Logic]
        Critic -- "Refine Search" --> Plan
        Critic --> Final[Final Report Synthesis]
    end

    Final --> User
```

## Control Plane (The Strings)

The core efficiency comes from a powerful supervisory agent (the Puppeteer) that does not search for data itself but instead breaks down complex research tasks into smaller, executable "scripts".

### Task Decomposition & Planning

1. **Query Decomposition**: Translate natural language into specific "drags" or trajectories of intent, much like a generator uses points to define motion.
2. **Task Breakdown**: Decompose complex research into atomic, executable sub-tasks.
3. **Priority Assignment**: Rank tasks by importance, urgency, and dependency.

### Global Shared Memory

1. **Context Persistence**: Maintain research context across agent interactions.
2. **Source of Truth**: Ensure every part of the research report is derived from the same "source of truth," maintaining high data integrity.
3. **State Management**: Track progress, findings, and intermediate results.

### Task Router

1. **Agent Selection**: Route tasks to appropriate specialized agents based on domain.
2. **Load Balancing**: Distribute work across available agents.
3. **Policy Enforcement**: Ensure all research "nodes" follow strict configurations, preventing "configuration drift" or redundant searching.

## Execution Layer (The Puppets)

Specialized agents that actively traverse digital networks to identify and analyze information before it is requested.

### Search Agent

**Purpose**: Scours Web & APIs for general information.

**Capabilities**:
- Web search and scraping
- API integration
- Document retrieval
- Content extraction

### Finance Agent

**Purpose**: Real-time Market Data and financial analysis.

**Capabilities**:
- Stock market data
- Financial reports
- Economic indicators
- Company filings

### Medical Agent

**Purpose**: PubMed & Clinical Trials research.

**Capabilities**:
- PubMed searches
- Clinical trial databases
- Medical literature
- Drug interaction data

### Specialist Agent

**Purpose**: Domain-specific Tools for specialized research.

**Capabilities**:
- Custom domain expertise
- Specialized databases
- Technical documentation
- Industry-specific sources

## Synthesis & Feedback

### Citation & Fact Verifier

1. **Source Verification**: Validate all claims against primary sources.
2. **Citation Tracking**: Maintain proper attribution.
3. **Fact Checking**: Cross-reference facts across multiple sources.
4. **Confidence Scoring**: Assign reliability scores to findings.

### Self-Correction Logic

1. **Gap Detection**: Identify missing information or weak arguments.
2. **Refinement Loop**: Feed back to Control Plane for additional research.
3. **Quality Assurance**: Ensure output meets quality standards.
4. **Bias Detection**: Identify and mitigate potential biases.

### Final Report Synthesis

1. **Structure Assembly**: Organize findings into coherent structure.
2. **Executive Summary**: Create high-level overview.
3. **Detailed Analysis**: Provide in-depth analysis.
4. **Recommendations**: Offer actionable insights.

## Usage

When activated, this skill enables Project Zero to:

1. **Proactive Research**: Actively traverse networks before being asked.
2. **Context-Aware Searching**: Use facts about the user to conditionally apply research policies.
3. **Decentralized Collection**: Clone/adapt sub-routines into various digital ecosystems.
4. **Consistent Output**: Ensure all research is derived from the same source of truth.

## Activation

This skill is automatically activated when:
- User requests research tasks
- Complex multi-source analysis is needed
- Domain-specific expertise is required
- Comprehensive fact-checking is necessary

## Notes

- The Puppeteer (Project Zero) never searches directly - it orchestrates.
- Each agent operates autonomously within its domain.
- Feedback loops ensure continuous improvement.
- Global Shared Memory maintains consistency across all agents.
