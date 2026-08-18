#!/bin/bash

echo "============================================================"
echo "🛡️  NOVA Framework Web Server"
echo "============================================================"
echo "Starting server on http://localhost:8080"
echo "Open your browser and go to: http://localhost:8080"
echo "============================================================"
echo ""
echo "Features:"
echo "• Scan prompts for security threats"
echo "• Detect jailbreaks, injections, malware requests"
echo "• Real-time threat analysis"
echo "• Beautiful web interface"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd /tmp/nova-framework
source venv/bin/activate
python web_server.py
