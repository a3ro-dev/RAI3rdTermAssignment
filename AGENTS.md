# AGENTS.md

## Overview
This document serves as the single source of truth for repository standards, team roles, and coding practices. AI agents and human contributors must adhere to these guidelines to ensure consistency and quality across the codebase.

## Core Directives
- **Performance First**: All code must prioritize extremely fast performance, optimizing for TTFB, LCP, INP, and general execution speed.
- **Responsiveness**: Any UI components must be fully responsive and tested across mobile, tablet, and desktop.
- **Security**: Apply the highest security standards to protect user data and platform integrity.
- **Modern Standards**: Favor modern, efficient syntax and patterns. Avoid legacy methods unless strictly necessary for compatibility.

## Engineering Standards
- **Clean Code**: Write maintainable, upgradeable, and readable code. Use descriptive names and clear structures.
- **Documentation**: All changes must be documented. No "AI slop"—keep documentation concise, accurate, and useful.
- **Tooling**:
    - For Javascript/Typescript: **Always Use `pnpm`**.
    - For Python: Use `venv` or `pnpm` (if using pnpm for python management).
- **Reasoning**: Always provide reasoning for architectural choices and significant changes.

## Design Choices & Principles
- **Aesthetics**: UI should feel premium, dynamic, and state-of-the-art.
- **Interaction**: Use hover effects, smooth transitions, and micro-animations to improve engagement.
- **Consistency**: Use predefined design tokens and consistent components.

## Safety & Practices
- **Validation**: Strict input validation on all user-facing interfaces.
- **Testing**: Maintain high test coverage for core logic (e.g., `gradeprogram`, `assignment3`).

## Device Compatibility
- **Cross-Platform**: Ensure functionality across Chromium-based browsers, Firefox, and Safari.
- **Mobile-First**: Designs should be optimized for mobile interactions first, then scaled up.

## Agent Profiles
- **Backend/Logic**: Handled by Antigravity (Gemini).
- **Design/UI**: Handled by Antigravity (Gemini).
- **Cloud/Infra**: Managed by Akshat Singh Kushwaha.
