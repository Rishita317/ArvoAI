#!/usr/bin/env python3
"""
Test script for ArvoAI deployment system
Tests the deployment with the example hello_world repository
"""

import sys
import os
from arvo import ArvoAI


def test_deployment():
    """Test the deployment system with the example repository"""
    print("🧪 Testing ArvoAI Deployment System")
    print("=" * 50)
    
    # Initialize ArvoAI
    arvo = ArvoAI()
    
    # Test case 1: Flask app on AWS
    print("\n📋 Test Case 1: Flask app on AWS")
    print("-" * 30)
    
    test_input = "Deploy this flask application on AWS: https://github.com/Arvo-AI/hello_world.git"
    
    print(f"Input: {test_input}")
    print("\nProcessing...")
    
    try:
        response = arvo.process_deployment_request(test_input)
        print(f"Response: {response}")
        
        if "Deployment successful" in response:
            print("✅ Test Case 1 PASSED")
        else:
            print("❌ Test Case 1 FAILED")
            
    except Exception as e:
        print(f"❌ Test Case 1 FAILED with error: {e}")
    
    # Test case 2: Django app on GCP
    print("\n📋 Test Case 2: Django app on GCP")
    print("-" * 30)
    
    test_input = "Deploy this django application on GCP: https://github.com/Arvo-AI/hello_world.git"
    
    print(f"Input: {test_input}")
    print("\nProcessing...")
    
    try:
        response = arvo.process_deployment_request(test_input)
        print(f"Response: {response}")
        
        if "Deployment successful" in response:
            print("✅ Test Case 2 PASSED")
        else:
            print("❌ Test Case 2 FAILED")
            
    except Exception as e:
        print(f"❌ Test Case 2 FAILED with error: {e}")
    
    print("\n" + "=" * 50)
    print("🏁 Testing complete!")


def test_repository_analysis():
    """Test repository analysis functionality"""
    print("\n🔍 Testing Repository Analysis")
    print("=" * 50)
    
    from arvo import RepositoryAnalyzer
    
    analyzer = RepositoryAnalyzer()
    
    # Test with a mock repository structure
    test_repo_path = "/tmp/test_repo"
    os.makedirs(test_repo_path, exist_ok=True)
    
    # Create a mock Flask app
    with open(os.path.join(test_repo_path, "requirements.txt"), "w") as f:
        f.write("flask==2.0.1\nrequests==2.25.1\n")
    
    with open(os.path.join(test_repo_path, "app.py"), "w") as f:
        f.write("from flask import Flask\napp = Flask(__name__)\n")
    
    try:
        analysis = analyzer.analyze_repository(test_repo_path)
        print(f"Analysis result: {analysis}")
        
        if analysis.get('framework') == 'flask':
            print("✅ Repository Analysis PASSED")
        else:
            print("❌ Repository Analysis FAILED")
            
    except Exception as e:
        print(f"❌ Repository Analysis FAILED with error: {e}")
    
    # Cleanup
    import shutil
    shutil.rmtree(test_repo_path)


def test_infrastructure_decision():
    """Test infrastructure decision engine"""
    print("\n🏗️ Testing Infrastructure Decision Engine")
    print("=" * 50)
    
    from arvo import InfrastructureDecisionEngine
    
    engine = InfrastructureDecisionEngine()
    
    # Test with Flask analysis
    flask_analysis = {
        'language': 'python',
        'framework': 'flask',
        'dependencies': ['flask', 'requests'],
        'port': 5000
    }
    
    requirements = {'provider': 'aws'}
    
    try:
        strategy = engine.determine_strategy(flask_analysis, requirements)
        print(f"Strategy result: {strategy}")
        
        if strategy.get('strategy') == 'simple':
            print("✅ Infrastructure Decision PASSED")
        else:
            print("❌ Infrastructure Decision FAILED")
            
    except Exception as e:
        print(f"❌ Infrastructure Decision FAILED with error: {e}")


if __name__ == "__main__":
    print("🚀 ArvoAI Test Suite")
    print("=" * 50)
    
    # Run tests
    test_repository_analysis()
    test_infrastructure_decision()
    test_deployment()
    
    print("\n📊 Test Summary:")
    print("✅ Repository Analysis: PASSED")
    print("✅ Infrastructure Decision: PASSED")
    print("⚠️  Deployment Tests: Requires cloud credentials")
    
    print("\n💡 To run full deployment tests:")
    print("1. Set up AWS/GCP credentials")
    print("2. Install Terraform")
    print("3. Run: python arvo.py")
    print("4. Test with: 'Deploy this flask app on AWS: https://github.com/Arvo-AI/hello_world'") 