# 🚀 Pipeline Paramedic Agent (Autonomous SRE)

An AI-native, self-healing CI/CD agent that automatically detects failed pipelines, performs root cause analysis, generates surgical patches, and redeploys the fix—**achieving zero-downtime automation.**

## 🛠 Why this exists?
Standard CI/CD pipelines fail and wait for human intervention. This agent transforms a static CI/CD gate into an **Automated Hospital** that heals itself.

## 🧠 The Waterfall Architecture
1. **Priority 1 (GitLab Duo Native):** Leverages the power of GitLab Duo's AI engine to understand the codebase.
2. **Priority 2 (Circuit Breaker):** If the primary AI gateway faces latency or outages, it triggers an instant failover to **Groq LPU (Llama-3.3-70B)**, ensuring sub-second inference.
3. **Phase 4 (Surgical Deployment):** Directly commits the fix back to the repository via API, triggering an automatic pipeline restart.

## 🏆 The Flex
* **Self-Healing:** Zero human intervention required.
* **Resilient:** 3-Tier AI Circuit Breaker pattern.
* **Native:** Deep integration with GitLab Duo APIs.