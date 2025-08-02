#!/usr/bin/env python3
"""
Simple test script to verify ArvoAI functionality
"""

from arvo import ArvoAI

def test_arvo():
    """Test ArvoAI basic functionality"""
    print("Testing ArvoAI...")
    
    # Initialize ArvoAI
    arvo = ArvoAI()
    print(f"✅ ArvoAI initialized successfully")
    print(f"✅ Logger available: {hasattr(arvo, 'logger')}")
    
    # Test deployment
    repo_url = "https://github.com/Arvo-AI/hello_world.git"
    requirements = {'provider': 'aws', 'region': 'us-east-1'}
    
    print(f"🚀 Starting deployment test...")
    result = arvo.deploy_application(repo_url, requirements)
    
    if result['success']:
        print(f"✅ Deployment successful!")
        print(f"   Framework: {result['analysis']['framework']}")
        print(f"   Language: {result['analysis']['language']}")
        print(f"   Dependencies: {result['analysis']['dependencies']}")
        print(f"   Start Commands: {result['analysis']['start_commands']}")
        print(f"   Public IP: {result['public_ip']}")
        print(f"   Application URL: {result['application_url']}")
    else:
        print(f"❌ Deployment failed: {result['error']}")

if __name__ == "__main__":
    test_arvo()
