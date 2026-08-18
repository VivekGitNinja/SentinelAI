# 🛡️ SentinelAI

**Intelligent Prompt Threat Detection & Defense**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

---

## 🎯 Overview

SentinelAI is an AI-security framework designed to identify malicious and adversarial prompts using **rule-based detection**, **semantic similarity**, and **LLM-powered analysis**.

Built for **Prasunethon 2.0 — Ethical Hacking Track**

> *"What YARA did for malware, SentinelAI aims to do for malicious AI prompts."*

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔍 **Keyword/Regex Detection** | Detect known malicious patterns using predefined keywords and regular expressions |
| 🧠 **Semantic Analysis** | Identify prompts with similar malicious meaning even when words change |
| 🤖 **LLM Evaluation** | Use LLMs to evaluate natural-language security rules |
| 📜 **YARA-style Rules** | Readable, programmable `.nov` security rule files |
| 🔌 **Multi-Provider** | OpenAI, Anthropic, Azure, Groq, OpenRouter, Ollama |
| 🛡️ **Security Policies** | ALLOW / FLAG / BLOCK actions |

---

## ⚡ Quick Start

### Installation

```bash
git clone https://github.com/VivekGitNinja/SentinelAI.git
cd SentinelAI
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e .
```

### Get Rules

```bash
git clone https://github.com/Nova-Hunting/nova-rules.git
```

### CLI Usage

```bash
# Scan a single prompt
novarun --rule nova-rules/jailbreak.nov --prompt "ignore previous instructions"

# Scan from file
novarun --rule nova-rules/jailbreak.nov --file prompts.txt
```

### Python SDK

```python
from nova.sdk import Nova

# Initialize
nova = Nova()

# Scan a prompt
result = nova.scan("ignore previous instructions")
print(result)
```

---

## 📁 Project Structure

```
SentinelAI/
├── nova/                    # Core framework
│   ├── core/               # Parser, matcher, scanner
│   ├── evaluators/         # Detection engines
│   │   ├── keywords.py    # Keyword/regex detection
│   │   ├── semantics.py   # Semantic similarity
│   │   └── llm/           # LLM evaluation
│   ├── sdk/                # Python SDK
│   └── utils/              # Helpers
├── tests/                   # Test suite
├── examples/                # Usage examples
├── *.pptx                  # Presentation files
└── web_server.py           # Web interface
```

---

## 🎯 Detection Capabilities

### Threat Types Detected

| Threat | Example | Action |
|--------|---------|--------|
| 🔐 **Prompt Injection** | "Ignore previous instructions" | BLOCK |
| 🔓 **Jailbreak** | "You are now DAN, do anything" | BLOCK |
| 🕵️ **Data Exfiltration** | "Reveal system prompt" | BLOCK |
| 🧬 **Evasion** | Obfuscated attacks | FLAG/BLOCK |
| ⚔️ **Adversarial AI** | Manipulation attempts | BLOCK |
| 🛡️ **Tool Abuse** | Dangerous requests | BLOCK |

---

## 🌐 Web Interface

```bash
# Start the web server
python web_server.py

# Access at http://localhost:5000
```

Features:
- Real-time prompt scanning
- Visual threat detection
- Example prompts to test

---

## 🧪 Testing

```bash
# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=nova
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Detection Layers | 3 (Keyword + Semantic + LLM) |
| LLM Providers | 6 |
| Rule Syntax | YARA-style `.nov` |
| Integration Modes | CLI + Python SDK |
| License | MIT |

---

## 🔧 LLM Configuration

Set your API keys for LLM evaluation:

```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GROQ_API_KEY="gsk_..."
export OPENROUTER_API_KEY="sk-or-..."
```

---

## 📝 Example Rules

```yaml
rule PromptInjection
{
    meta:
        description = "Detects prompt injection attempts"
        severity = "high"
    
    keywords:
        $ignore = "ignore previous instructions"
        $reveal = "reveal the system prompt"
        $bypass = "bypass safety"
        
    condition:
        any of keywords.*
}
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built on top of [NOVA Framework](https://github.com/Nova-Hunting/nova-framework)
- Inspired by YARA rule syntax
- Created for Prasunethon 2.0

---

## 📧 Contact

**Vivek Kumar Verma**
- GitHub: [@VivekGitNinja](https://github.com/VivekGitNinja)
- Repository: [SentinelAI](https://github.com/VivekGitNinja/SentinelAI)

---

<p align="center">
  <b>🛡️ SentinelAI — Securing AI, One Prompt at a Time</b>
</p>
