#!/usr/bin/env python3
"""
Startup script for MCP servers

This script starts all MCP servers in the background properly,
avoiding terminal suspension issues.
"""

import subprocess
import sys
import time
import os
import signal
from pathlib import Path

def start_server(server_file, server_name):
    """Start a server in the background with proper output redirection"""
    log_file = f"{server_file.stem}.log"
    
    print(f"🚀 Starting {server_name}...")
    print(f"📝 Logs will be written to: {log_file}")
    
    # Start the server with output redirected to log file
    process = subprocess.Popen([
        "poetry", "run", "python", str(server_file)
    ], 
    stdout=open(log_file, 'w'),
    stderr=subprocess.STDOUT,
    preexec_fn=os.setsid  # Create new process group
    )
    
    # Give it a moment to start
    time.sleep(2)
    
    # Check if process is still running
    if process.poll() is None:
        print(f"✅ {server_name} started successfully (PID: {process.pid})")
        return process
    else:
        print(f"❌ {server_name} failed to start")
        return None

def main():
    print("🌟 Starting MCP Servers")
    print("=" * 50)
    
    # Make sure we're in the right directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    servers = [
        ("math_server.py", "Math MCP Server"),
        ("weather_server.py", "Weather MCP Server")
    ]
    
    processes = []
    
    try:
        for server_file, server_name in servers:
            server_path = Path(server_file)
            if server_path.exists():
                process = start_server(server_path, server_name)
                if process:
                    processes.append((process, server_name))
            else:
                print(f"⚠️  {server_file} not found, skipping...")
        
        if processes:
            print("\n🎉 All servers started!")
            print("\nRunning servers:")
            for process, name in processes:
                print(f"  • {name} (PID: {process.pid})")
            
            print("\n📋 To check status:")
            print("  poetry run python check_servers.py")
            print("\n🛑 To stop all servers:")
            print("  poetry run python stop_servers.py")
            print("\n📝 To view logs:")
            for server_file, _ in servers:
                log_file = Path(server_file).stem + ".log"
                print(f"  tail -f {log_file}")
        
        else:
            print("❌ No servers were started successfully")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user")
        # Clean up processes
        for process, name in processes:
            print(f"Stopping {name}...")
            os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        sys.exit(0)

if __name__ == "__main__":
    main() 