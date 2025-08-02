#!/usr/bin/env python3
"""
Debug script to check repository structure
"""

import os
import tempfile
import requests
import zipfile
from arvo import RepositoryAnalyzer


def debug_repository():
    """Debug the repository structure"""
    print("🔍 Debugging Repository Structure")
    print("=" * 40)
    
    # Download repository
    analyzer = RepositoryAnalyzer()
    repo_url = "https://github.com/Arvo-AI/hello_world.git"
    
    try:
        repo_path = analyzer.download_repository(repo_url)
        print(f"✅ Repository downloaded to: {repo_path}")
        
        # List all contents
        print(f"\n📁 Repository contents:")
        for root, dirs, files in os.walk(repo_path):
            level = root.replace(repo_path, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
        
        # Check for specific files
        print(f"\n🔍 Checking for key files:")
        key_files = [
            'requirements.txt',
            'app/requirements.txt',
            'app.py',
            'app/app.py',
            'package.json',
            'pom.xml'
        ]
        
        for file_path in key_files:
            full_path = os.path.join(repo_path, file_path)
            if os.path.exists(full_path):
                print(f"✅ Found: {file_path}")
                # Show first few lines
                try:
                    with open(full_path, 'r') as f:
                        content = f.read()
                        print(f"   Content preview: {content[:100]}...")
                except Exception as e:
                    print(f"   Error reading file: {e}")
            else:
                print(f"❌ Not found: {file_path}")
        
        # Try analysis
        print(f"\n🔍 Running analysis:")
        analysis = analyzer.analyze_repository(repo_path)
        print(f"Analysis result: {analysis}")
        
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    debug_repository() 