#!/usr/bin/env python3
"""
Debug script to test repository analysis
"""

import tempfile
from arvo import RepositoryAnalyzer

def test_hello_world_analysis():
    """Test analysis of hello_world repository"""
    analyzer = RepositoryAnalyzer()
    
    # Download the repository
    repo_url = "https://github.com/Arvo-AI/hello_world.git"
    repo_path = analyzer.download_repository(repo_url)
    
    print(f"Repository downloaded to: {repo_path}")
    
    # Check directory structure
    import os
    for root, dirs, files in os.walk(repo_path):
        level = root.replace(repo_path, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")
    
    # Check if requirements.txt exists and read it
    req_path = os.path.join(repo_path, "hello_world-main", "app", "requirements.txt")
    if os.path.exists(req_path):
        print(f"\nFound requirements.txt at: {req_path}")
        with open(req_path, 'r') as f:
            content = f.read()
            print(f"Contents:\n{content}")
    
    # Test analysis
    analysis = analyzer.analyze_repository(repo_path)
    print(f"\nAnalysis result:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    test_hello_world_analysis()
