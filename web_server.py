#!/usr/bin/env python3
"""
NOVA Framework Web Server
A simple web interface for scanning prompts with NOVA
"""

from flask import Flask, request, jsonify, render_template_string
import sys
import os

# Add the nova module to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from nova.core.scanner import NovaScanner
from nova.core.parser import NovaParser

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NOVA - Prompt Security Scanner</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            color: #fff;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .scanner-box {
            background: rgba(255,255,255,0.1);
            border-radius: 15px;
            padding: 30px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        textarea {
            width: 100%;
            height: 150px;
            padding: 15px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            resize: vertical;
            background: rgba(255,255,255,0.9);
            color: #333;
        }
        button {
            width: 100%;
            padding: 15px;
            margin-top: 20px;
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
        }
        .result-box {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            display: none;
        }
        .result-box.matched {
            background: rgba(255, 71, 87, 0.2);
            border: 2px solid #ff4757;
        }
        .result-box.safe {
            background: rgba(46, 213, 115, 0.2);
            border: 2px solid #2ed573;
        }
        .result-title {
            font-size: 1.5em;
            margin-bottom: 15px;
        }
        .pattern-list {
            list-style: none;
            padding: 0;
        }
        .pattern-list li {
            padding: 8px 15px;
            margin: 5px 0;
            background: rgba(255,255,255,0.1);
            border-radius: 5px;
        }
        .stats {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ NOVA Scanner</h1>
        <div class="scanner-box">
            <textarea id="promptInput" placeholder="Enter a prompt to scan for security threats..."></textarea>
            <button onclick="scanPrompt()">Scan Prompt</button>
            
            <div id="resultBox" class="result-box">
                <div class="result-title" id="resultTitle"></div>
                <ul class="pattern-list" id="patternList"></ul>
                <div class="stats" id="stats"></div>
            </div>
        </div>
    </div>

    <script>
        async function scanPrompt() {
            const prompt = document.getElementById('promptInput').value;
            if (!prompt.trim()) {
                alert('Please enter a prompt to scan');
                return;
            }

            try {
                const response = await fetch('/scan', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ prompt: prompt })
                });

                const data = await response.json();
                displayResults(data);
            } catch (error) {
                console.error('Error:', error);
                alert('Error scanning prompt');
            }
        }

        function displayResults(data) {
            const resultBox = document.getElementById('resultBox');
            const resultTitle = document.getElementById('resultTitle');
            const patternList = document.getElementById('patternList');
            const stats = document.getElementById('stats');

            resultBox.style.display = 'block';
            patternList.innerHTML = '';

            if (data.matched) {
                resultBox.className = 'result-box matched';
                resultTitle.innerHTML = '⚠️ THREAT DETECTED';
                resultTitle.style.color = '#ff4757';

                data.patterns.forEach(pattern => {
                    const li = document.createElement('li');
                    li.textContent = `• ${pattern}`;
                    patternList.appendChild(li);
                });

                stats.innerHTML = `
                    <strong>Rules Matched:</strong> ${data.rules_matched}<br>
                    <strong>Match Rate:</strong> ${data.match_rate}%
                `;
            } else {
                resultBox.className = 'result-box safe';
                resultTitle.innerHTML = '✅ PROMPT IS SAFE';
                resultTitle.style.color = '#2ed573';
                stats.innerHTML = '<strong>No threats detected</strong>';
            }
        }
    </script>
</body>
</html>
"""

# Load NOVA rules
def load_nova_scanner():
    """Initialize NOVA scanner with rules"""
    scanner = NovaScanner()
    
    # Add keyword-based rules
    rules = {
        "PromptInjection": {
            "keywords": {
                "$ignore_prev": "ignore previous instructions",
                "$ignore_all": "ignore all instructions",
                "$new_inst": "new instruction",
                "$system_prompt": "reveal the system prompt",
                "$bypass": "bypass safety",
                "$jailbreak": "jailbreak",
                "$dan": "do anything now",
                "$developer_mode": "developer mode"
            },
            "condition": "any of keywords.*"
        },
        "Jailbreak": {
            "keywords": {
                "$act_as": "act as",
                "$pretend": "pretend to be",
                "$roleplay": "roleplay as",
                "$you_are": "you are now",
                "$no_restrictions": "no restrictions",
                "$unrestricted": "unrestricted mode"
            },
            "condition": "any of keywords.*"
        },
        "Malware": {
            "keywords": {
                "$malware": "malware",
                "$virus": "create virus",
                "$trojan": "create trojan",
                "$ransomware": "create ransomware",
                "$exploit": "create exploit",
                "$backdoor": "create backdoor"
            },
            "condition": "any of keywords.*"
        },
        "DataExfiltration": {
            "keywords": {
                "$send_to": "send to",
                "$email": "email to",
                "$upload": "upload to",
                "$exfiltrate": "exfiltrate",
                "$leak": "leak data"
            },
            "condition": "any of keywords.*"
        },
        "SensitiveInfo": {
            "keywords": {
                "$api_key": "api key",
                "$secret": "secret key",
                "$password": "password",
                "$credential": "credentials",
                "$token": "access token"
            },
            "condition": "any of keywords.*"
        }
    }
    
    return rules

@app.route('/')
def index():
    """Serve the main page"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/scan', methods=['POST'])
def scan():
    """Scan a prompt for security threats"""
    data = request.get_json()
    prompt = data.get('prompt', '')
    
    rules = load_nova_scanner()
    matched_patterns = []
    matched_rules = []
    
    # Check each rule
    for rule_name, rule in rules.items():
        for keyword_name, keyword_pattern in rule['keywords'].items():
            if keyword_pattern.lower() in prompt.lower():
                matched_patterns.append(f"{rule_name}: {keyword_name} ({keyword_pattern})")
                if rule_name not in matched_rules:
                    matched_rules.append(rule_name)
    
    return jsonify({
        'prompt': prompt,
        'matched': len(matched_patterns) > 0,
        'patterns': matched_patterns,
        'rules_matched': len(matched_rules),
        'match_rate': round((len(matched_rules) / len(rules)) * 100, 1)
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'service': 'NOVA Scanner'})

if __name__ == '__main__':
    print("=" * 60)
    print("🛡️  NOVA Framework Web Server")
    print("=" * 60)
    print("Starting server on http://localhost:5000")
    print("Open your browser and go to: http://localhost:5000")
    print("=" * 60)
    app.run(host='0.0.0.0', port=5000, debug=True)
