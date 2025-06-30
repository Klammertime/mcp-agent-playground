#!/usr/bin/env python3
"""
Check script for MCP servers

This script checks the status of all MCP servers.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_server_status():
    """Check if MCP servers are running"""
    
    server_files = ["math_server.py", "weather_server.py"]
    running_servers = []
    
    for server_file in server_files:
        try:
            # Find processes containing the server filename
            result = subprocess.run([
                "pgrep", "-f", server_file
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                pids = result.stdout.strip().split('\n')
                for pid in pids:
                    if pid:  # Make sure PID is not empty
                        running_servers.append((server_file, pid))
            
        except FileNotFoundError:
            # pgrep not available, try ps instead
            try:
                result = subprocess.run([
                    "ps", "aux"
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    lines = result.stdout.split('\n')
                    for line in lines:
                        if server_file in line and 'python' in line:
                            parts = line.split()
                            if len(parts) > 1:
                                running_servers.append((server_file, parts[1]))
            except:
                pass
    
    return running_servers

def check_log_files():
    """Check for log files and their recent content"""
    
    log_files = ["math_server.log", "weather_server.log"]
    log_info = []
    
    for log_file in log_files:
        if os.path.exists(log_file):
            try:
                # Get file size
                size = os.path.getsize(log_file)
                
                # Get last few lines
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    last_lines = lines[-3:] if len(lines) >= 3 else lines
                
                log_info.append((log_file, size, last_lines))
            except:
                log_info.append((log_file, 0, []))
    
    return log_info

def main():
    print("📋 MCP Server Status Check")
    print("=" * 35)
    
    # Check running processes
    running_servers = check_server_status()
    
    if running_servers:
        print("🟢 Running Servers:")
        for server_file, pid in running_servers:
            server_name = server_file.replace('.py', '').replace('_', ' ').title()
            print(f"  • {server_name} (PID: {pid})")
    else:
        print("🔴 No MCP servers are currently running")
    
    print()
    
    # Check log files
    log_info = check_log_files()
    
    if log_info:
        print("📝 Log Files:")
        for log_file, size, last_lines in log_info:
            print(f"  • {log_file} ({size} bytes)")
            if last_lines:
                print("    Recent entries:")
                for line in last_lines:
                    print(f"      {line.strip()}")
            else:
                print("    (empty or unreadable)")
            print()
    else:
        print("📝 No log files found")
    
    # Check if servers should be running
    expected_servers = ["math_server.py", "weather_server.py"]
    missing_servers = []
    
    for expected in expected_servers:
        if not any(server == expected for server, _ in running_servers):
            missing_servers.append(expected)
    
    if missing_servers:
        print("⚠️  Expected but not running:")
        for server in missing_servers:
            print(f"  • {server}")
        print()
        print("💡 To start all servers:")
        print("  poetry run python start_servers.py")
    else:
        print("✅ All expected servers are running!")
    
    print("\n🔧 Management Commands:")
    print("  Start all:  poetry run python start_servers.py")
    print("  Stop all:   poetry run python stop_servers.py")
    print("  Check:      poetry run python check_servers.py")

if __name__ == "__main__":
    main() 