# ArvoAI 

**NLP-powered CLI autodeployment system**

ArvoAI is an intelligent command-line interface that automatically deploys applications based on natural language descriptions and repository links. Simply describe your deployment needs, and ArvoAI will handle the entire process from analysis to deployment!

## 🎯 Features

- **Natural Language Processing**: Parse deployment requirements from plain English
- **Repository Analysis**: Automatically detect application type, framework, and dependencies
- **Multi-Cloud Support**: AWS and Google Cloud Platform (GCP) integration
- **Infrastructure Automation**: Terraform-based infrastructure provisioning
- **Code Adaptation**: Automatic updates for cloud deployment (localhost → public IP)
- **Multi-Framework Support**: Flask, Django, FastAPI, Express, React, Vue, Spring, Laravel
- **Comprehensive Logging**: Detailed deployment logs and process tracking

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Terraform CLI
- AWS CLI or GCP SDK (for cloud deployments)
- Cloud provider credentials

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd arvoAI
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up cloud credentials:

```bash
# For AWS
aws configure

# For GCP
gcloud auth application-default login
```

4. Run ArvoAI:

```bash
python arvo.py
```

## 📖 Usage

### Basic Deployment

Start the interactive chat and describe your deployment:

```
============================================================
🚀 Welcome to ArvoAI v1.0.0
============================================================
I'm here to automatically deploy your applications!

What I can do:
• Analyze your repository and detect application type
• Determine the best deployment strategy
• Provision cloud infrastructure with Terraform
• Deploy your application automatically
• Update your code for cloud deployment

Just describe your deployment needs and provide a repository!
Type 'exit' or 'bye' to quit the session.
============================================================

You: Deploy this flask application on AWS: https://github.com/Arvo-AI/hello_world.git
```

### Example Commands

**Flask App on AWS:**

```
Deploy this flask application on AWS: https://github.com/Arvo-AI/hello_world.git
```

**Django App on GCP:**

```
Deploy this django application on GCP: https://github.com/Arvo-AI/hello_world.git
```

**React App on AWS:**

```
Deploy this react application on AWS: https://github.com/Arvo-AI/hello_world.git
```

### Supported Input Formats

- **GitHub URLs**: `https://github.com/user/repo`
- **Zip files**: `/path/to/repository.zip`
- **Natural language**: "Deploy this [framework] application on [provider]"

## 🏗️ Architecture

### Core Components

1. **RepositoryAnalyzer**: Downloads and analyzes code repositories
2. **InfrastructureDecisionEngine**: Determines optimal deployment strategy
3. **TerraformManager**: Provisions cloud infrastructure
4. **CodeModifier**: Updates code for cloud deployment
5. **ArvoAI**: Main orchestration class

### Supported Frameworks

| Language | Frameworks                   | Default Port |
| -------- | ---------------------------- | ------------ |
| Python   | Flask, Django, FastAPI       | 5000/8000    |
| Node.js  | Express, React, Vue, Next.js | 3000         |
| Java     | Spring, Maven, Gradle        | 8080         |
| PHP      | Laravel, Symfony             | 8000         |

### Deployment Strategies

- **Simple VM**: Single virtual machine deployment
- **Containerized**: Docker-based deployment
- **Serverless**: Function-based deployment (planned)

## 🔧 Configuration

### Cloud Provider Settings

Edit `config.yaml` to customize deployment settings:

```yaml
aws:
  default_region: "us-east-1"
  instance_types:
    small: "t2.micro"
    medium: "t2.small"

gcp:
  default_region: "us-central1"
  machine_types:
    small: "e2-micro"
    medium: "e2-small"
```

### Environment Variables

```bash
# AWS Configuration
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=us-east-1

# GCP Configuration
export GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
```

## 🧪 Testing

Run the test suite to verify functionality:

```bash
python test_deployment.py
```

This will test:

- Repository analysis
- Infrastructure decision making
- Deployment orchestration

## 📊 Deployment Process

### Step-by-Step Workflow

1. **Input Parsing**: Extract repository URL and requirements from natural language
2. **Repository Analysis**: Download and analyze code structure
3. **Strategy Determination**: Choose optimal deployment approach
4. **Infrastructure Provisioning**: Create Terraform configuration and deploy
5. **Code Modification**: Update localhost references to public IP
6. **Application Deployment**: Install dependencies and start application
7. **Result Delivery**: Return public URL and deployment details

### Example Output

```
🎉 Deployment successful!

📊 Analysis: flask application
🌐 Public IP: 52.23.45.67
🔗 Application URL: http://52.23.45.67:5000
📝 Modified 3 files
📋 Instance ID: i-1234567890abcdef0

Your application is now live! 🚀
```

## 🔍 Troubleshooting

### Common Issues

**Terraform not found:**

```bash
# Install Terraform
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update && sudo apt-get install terraform
```

**AWS credentials not configured:**

```bash
aws configure
# Enter your Access Key ID, Secret Access Key, and region
```

**GCP authentication failed:**

```bash
gcloud auth application-default login
```

### Logs

Check deployment logs:

```bash
tail -f arvo_deployment.log
```

## 🚀 Advanced Features

### Custom Terraform Templates

Create custom deployment templates in `terraform_templates/`:

```
terraform_templates/
├── simple_vm/
├── docker_vm/
└── lambda/
```

### Multi-Region Deployment

Specify regions in your request:

```
Deploy this flask app on AWS us-west-2: https://github.com/user/repo
```

### Environment-Specific Configuration

Use environment variables for different deployment environments:

```bash
export ARVO_ENVIRONMENT=production
export ARVO_INSTANCE_TYPE=t2.medium
```

## 📈 Roadmap

### Phase 1 (Current) ✅

- [x] Interactive CLI interface
- [x] Repository analysis
- [x] Basic Terraform provisioning
- [x] Multi-cloud support
- [x] Code modification

### Phase 2 (Next)

- [ ] Advanced NLP with OpenAI integration
- [ ] Kubernetes deployment support
- [ ] Database provisioning
- [ ] Load balancer configuration
- [ ] Auto-scaling groups

### Phase 3 (Future)

- [ ] CI/CD pipeline integration
- [ ] Blue-green deployments
- [ ] Monitoring and alerting
- [ ] Cost optimization
- [ ] Multi-region deployments

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python test_deployment.py

# Format code
black arvo.py

# Lint code
flake8 arvo.py
```

## 📄 License

[Add your license here]

## 🆘 Support

- **Issues**: Open an issue on GitHub
- **Documentation**: Check the README and inline code comments
- **Logs**: Review `arvo_deployment.log` for detailed error information

---

**Note**: This is a production-ready autodeployment system. The current version provides full automation from natural language input to deployed application. Future versions will include advanced NLP capabilities and additional deployment strategies.
