#!/usr/bin/env python3
"""
Stop script for MCP servers

This script stops all running MCP servers cleanly.
"""

import subprocess
import sys
import signal
import os

def find_and_kill_servers():
    """Find and kill MCP server processes"""
    
    # Find processes running our servers
    server_files = ["math_server.py", "weather_server.py"]
    killed_count = 0
    
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
                        try:
                            pid_int = int(pid)
                            print(f"🛑 Stopping {server_file} (PID: {pid_int})")
                            os.kill(pid_int, signal.SIGTERM)
                            killed_count += 1
                        except (ValueError, ProcessLookupError):
                            pass
            else:
                print(f"✅ {server_file} not running")
                
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
                                try:
                                    pid = int(parts[1])
                                    print(f"🛑 Stopping {server_file} (PID: {pid})")
                                    os.kill(pid, signal.SIGTERM)
                                    killed_count += 1
                                except (ValueError, ProcessLookupError):
                                    pass
            except:
                pass
    
    return killed_count

def main():
    print("🛑 Stopping MCP Servers")
    print("=" * 30)
    
    killed_count = find_and_kill_servers()
    
    if killed_count > 0:
        print(f"\n✅ Stopped {killed_count} server process(es)")
        print("\n🧹 Cleaning up log files...")
        
        # Optionally clean up log files
        log_files = ["math_server.log", "weather_server.log"]
        for log_file in log_files:
            if os.path.exists(log_file):
                print(f"  📄 {log_file} (keeping for reference)")
    else:
        print("\n✅ No MCP servers were running")
    
    print("\n🏁 Done!")

if __name__ == "__main__":
    main() 