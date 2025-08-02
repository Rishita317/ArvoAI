#!/usr/bin/env python3
"""
ArvoAI Demo Script
Demonstrates the autodeployment system with a mock repository
"""

import os
import tempfile
import shutil
import json
from arvo import ArvoAI, RepositoryAnalyzer, InfrastructureDecisionEngine


def download_real_repository():
    """Download the real hello_world repository for demonstration"""
    from arvo import RepositoryAnalyzer
    
    analyzer = RepositoryAnalyzer()
    repo_url = "https://github.com/Arvo-AI/hello_world.git"
    
    try:
        repo_path = analyzer.download_repository(repo_url)
        print(f"✅ Successfully downloaded repository to: {repo_path}")
        return repo_path
    except Exception as e:
        print(f"❌ Failed to download repository: {e}")
        # Fallback to mock repository
        return create_mock_repository()


def create_mock_repository():
    """Create a mock Flask repository for demonstration (fallback)"""
    temp_dir = tempfile.mkdtemp()
    
    # Create requirements.txt
    with open(os.path.join(temp_dir, 'requirements.txt'), 'w') as f:
        f.write("""flask==2.3.3
requests==2.31.0
python-dotenv==1.0.0
""")
    
    # Create app.py
    with open(os.path.join(temp_dir, 'app.py'), 'w') as f:
        f.write("""from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from ArvoAI!',
        'status': 'success',
        'framework': 'Flask'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
""")
    
    # Create README.md
    with open(os.path.join(temp_dir, 'README.md'), 'w') as f:
        f.write("""# Hello World Flask App

A simple Flask application for ArvoAI demonstration.

## Features
- Health check endpoint
- JSON API responses
- Environment variable configuration

## Local Development
```bash
pip install -r requirements.txt
python app.py
```
""")
    
    # Create .env file
    with open(os.path.join(temp_dir, '.env'), 'w') as f:
        f.write("""PORT=5000
FLASK_ENV=production
""")
    
    return temp_dir


def demo_repository_analysis():
    """Demonstrate repository analysis"""
    print("🔍 Demo: Repository Analysis")
    print("=" * 40)
    
    # Download real repository
    repo_path = download_real_repository()
    
    try:
        # Analyze repository
        analyzer = RepositoryAnalyzer()
        
        # Debug: List repository contents
        print(f"📁 Repository contents:")
        for root, dirs, files in os.walk(repo_path):
            level = root.replace(repo_path, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
        
        analysis = analyzer.analyze_repository(repo_path)
        
        print(f"📊 Analysis Results:")
        print(f"   Language: {analysis['language']}")
        print(f"   Framework: {analysis['framework']}")
        print(f"   Port: {analysis['port']}")
        print(f"   Dependencies: {len(analysis['dependencies'])} packages")
        print(f"   Start Commands: {analysis['start_commands']}")
        
        print("✅ Repository analysis completed successfully!")
        
    except Exception as e:
        print(f"❌ Repository analysis failed: {e}")
    
    finally:
        # Cleanup
        shutil.rmtree(repo_path)


def demo_infrastructure_decision():
    """Demonstrate infrastructure decision making"""
    print("\n🏗️ Demo: Infrastructure Decision Engine")
    print("=" * 40)
    
    # Create sample analysis
    flask_analysis = {
        'language': 'python',
        'framework': 'flask',
        'dependencies': ['flask', 'requests', 'python-dotenv'],
        'port': 5000,
        'start_commands': ['python app.py', 'flask run']
    }
    
    requirements = {
        'provider': 'aws',
        'region': 'us-east-1'
    }
    
    try:
        # Determine strategy
        engine = InfrastructureDecisionEngine()
        strategy = engine.determine_strategy(flask_analysis, requirements)
        
        print(f"📊 Strategy Results:")
        print(f"   Strategy: {strategy['strategy']}")
        print(f"   Template: {strategy['template']}")
        print(f"   Description: {strategy['description']}")
        
        print("✅ Infrastructure decision completed successfully!")
        
    except Exception as e:
        print(f"❌ Infrastructure decision failed: {e}")


def demo_terraform_generation():
    """Demonstrate Terraform configuration generation"""
    print("\n⚙️ Demo: Terraform Configuration Generation")
    print("=" * 40)
    
    from arvo import TerraformManager
    
    # Create sample data
    analysis = {
        'language': 'python',
        'framework': 'flask',
        'port': 5000,
        'start_commands': ['python app.py']
    }
    
    requirements = {
        'provider': 'aws',
        'region': 'us-east-1'
    }
    
    try:
        # Generate Terraform config
        terraform_manager = TerraformManager()
        terraform_dir = terraform_manager.create_terraform_config(
            'simple_vm', analysis, requirements
        )
        
        # Check if files were created
        files = os.listdir(terraform_dir)
        print(f"📁 Generated Terraform files: {files}")
        
        # Show main.tf content (first few lines)
        main_tf_path = os.path.join(terraform_dir, 'main.tf')
        if os.path.exists(main_tf_path):
            with open(main_tf_path, 'r') as f:
                content = f.read()
                print(f"📄 Main.tf preview (first 200 chars):")
                print(content[:200] + "...")
        
        print("✅ Terraform configuration generated successfully!")
        
    except Exception as e:
        print(f"❌ Terraform generation failed: {e}")


def demo_code_modification():
    """Demonstrate code modification for cloud deployment"""
    print("\n🔧 Demo: Code Modification for Cloud Deployment")
    print("=" * 40)
    
    from arvo import CodeModifier
    
    # Create mock repository with localhost references
    temp_dir = tempfile.mkdtemp()
    
    # Create a file with localhost references
    with open(os.path.join(temp_dir, 'config.py'), 'w') as f:
        f.write("""# Configuration file
DATABASE_URL = "http://localhost:5432"
API_ENDPOINT = "http://localhost:8000/api"
REDIS_URL = "redis://localhost:6379"
""")
    
    try:
        # Modify code for cloud deployment
        modifier = CodeModifier()
        public_ip = "52.23.45.67"  # Mock public IP
        
        modified_files = modifier.modify_code_for_deployment(
            temp_dir, public_ip, {'framework': 'flask'}
        )
        
        print(f"📝 Modified {len(modified_files)} files")
        
        # Show the modified content
        with open(os.path.join(temp_dir, 'config.py'), 'r') as f:
            content = f.read()
            print(f"📄 Modified config.py:")
            print(content)
        
        print("✅ Code modification completed successfully!")
        
    except Exception as e:
        print(f"❌ Code modification failed: {e}")
    
    finally:
        # Cleanup
        shutil.rmtree(temp_dir)


def demo_full_workflow():
    """Demonstrate the full deployment workflow"""
    print("\n🚀 Demo: Full Deployment Workflow")
    print("=" * 40)
    
    # Download real repository
    repo_path = download_real_repository()
    
    try:
        # Initialize ArvoAI
        arvo = ArvoAI()
        
        # Simulate the deployment process
        print("1️⃣ Analyzing repository...")
        analysis = arvo.analyzer.analyze_repository(repo_path)
        print(f"   ✅ Detected: {analysis['framework']} application")
        
        print("2️⃣ Determining deployment strategy...")
        requirements = {'provider': 'aws'}
        strategy = arvo.decision_engine.determine_strategy(analysis, requirements)
        print(f"   ✅ Strategy: {strategy['strategy']}")
        
        print("3️⃣ Generating Terraform configuration...")
        terraform_dir = arvo.terraform_manager.create_terraform_config(
            strategy['template'], analysis, requirements
        )
        print(f"   ✅ Configuration created in: {terraform_dir}")
        
        print("4️⃣ Simulating infrastructure deployment...")
        print("   ⏳ (This would normally deploy to AWS/GCP)")
        print("   ✅ Mock deployment successful!")
        
        print("5️⃣ Modifying code for cloud deployment...")
        public_ip = "52.23.45.67"  # Mock IP
        modified_files = arvo.code_modifier.modify_code_for_deployment(
            repo_path, public_ip, analysis
        )
        print(f"   ✅ Modified {len(modified_files)} files")
        
        print("\n🎉 Full workflow completed successfully!")
        print(f"📊 Application URL: http://{public_ip}:{analysis['port']}")
        
    except Exception as e:
        print(f"❌ Full workflow failed: {e}")
    
    finally:
        # Cleanup
        shutil.rmtree(repo_path)


def main():
    """Run all demos"""
    print("🚀 ArvoAI Autodeployment System Demo")
    print("=" * 50)
    print("This demo shows the core functionality of ArvoAI")
    print("without requiring cloud credentials or actual deployment.")
    print()
    
    # Run individual demos
    demo_repository_analysis()
    demo_infrastructure_decision()
    demo_terraform_generation()
    demo_code_modification()
    demo_full_workflow()
    
    print("\n" + "=" * 50)
    print("🏁 Demo completed!")
    print("\n💡 To run with actual deployment:")
    print("1. Set up cloud credentials")
    print("2. Install Terraform")
    print("3. Run: python arvo.py")
    print("4. Try: 'Deploy this flask app on AWS: https://github.com/user/repo'")


if __name__ == "__main__":
    main() 