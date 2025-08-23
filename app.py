import streamlit as st  # Import the Streamlit library for building web apps

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Portfolio - Shahnawaz",  # Set the browser tab title
    page_icon=":cloud:",                 # Set the tab icon (emoji)
    layout="wide"                        # Use wide layout for the page
)

# --- HERO SECTION ---
col1, col2, col3 = st.columns([1,2,1])  # Create three columns for layout (center column is wider)
with col2:  # Use the middle column for the hero section
    # Display profile image as a round picture using HTML/CSS
    st.markdown(
        """
        <div style="display:flex; justify-content:center;">
            <img src="https://raw.githubusercontent.com/shahilhussain41/portfolio/main/profile.png" style="width:180px; height:180px; border-radius:50%; object-fit:cover; border:2px solid #eee;" alt="Profile">
        </div>
        """,
        unsafe_allow_html=True  # Allow HTML for custom styling
    )
    st.markdown("<h2 style='text-align:center;'>Shahnawaz Hussain</h2>", unsafe_allow_html=True)  # Display name centered
    st.markdown("<h4 style='text-align:center; color:gray;'>Cloud Automation & DevOps Engineer | AWS | Terraform | CI/CD</h4>", unsafe_allow_html=True)  # Display title centered

# --- MENU (TABS LIKE VIJAYRAM) ---
menu = st.tabs([
    "👤 About Me", "💼 Work Experience", "📂 Projects", "🛠 Skills & Certifications",
    "🎓 Education", "🏆 Achievements", "📑 Resume", "📞 Contact"
])  # Create tabs for navigation

# --- ABOUT ME ---
with menu[0]:  # First tab: About Me
    st.subheader("👋 About Me")  # Section header
    st.write("""
    Cloud Automation and DevOps Engineer with **3.11 years of experience** in AWS infrastructure, Terraform (IaC), 
    and CI/CD implementation. Proven track record of reducing deployment times by **30%** and optimizing AWS costs.  
    Certified **AWS Solutions Architect** and **Terraform Associate**, skilled in Lambda automation, monitoring via Prometheus-Grafana, 
    and building secure cloud architectures aligned with the AWS Well-Architected Framework.
    """)  # Short bio

# --- WORK EXPERIENCE ---
with menu[1]:  # Second tab: Work Experience
    st.subheader("💼 Work Experience")  # Section header
    st.markdown("**Accenture Solutions Pvt. Ltd. | Cloud DevOps Engineer**  \n📍 Bengaluru | Dec 2021 – Present")  # Job title and location
    st.markdown("""
    - 🚀 Reduced deployment time by **30%** by developing CI/CD pipelines using AWS CodeCommit, CodeBuild, CodeDeploy & CodePipeline.  
    - 🔑 Managed **200+ IAM users, groups, policies & roles** with Terraform (IaC).  
    - ⚡ Automated IAM compliance for **100+ AWS accounts** via Lambda, cutting non-compliance by **60%**.  
    - 🌍 Ensured **99.9% uptime** using Blue/Green, Canary, and Rolling deployment strategies.  
    - 📊 Monitored EC2 & databases with Grafana, Prometheus, CloudWatch, and CloudTrail, reducing MTTR by **40%**.  
    - 🛡 Applied **AWS Well-Architected Framework** across 5+ environments.  
    - 🔒 Configured **NACL rules** across 10+ VPC subnets via Terraform.  
    """)  # List of achievements and responsibilities

# --- PROJECTS ---
with menu[2]:  # Third tab: Projects
    st.subheader("📂 Projects")  # Section header
    st.markdown("**AWS Architecture for 3-Tier Web Hosting**")  # Project title
    st.markdown("""
    - Designed scalable architecture with frontend, backend, and DB microservices on AWS.  
    - Automated provisioning with Terraform scripts.  
    - Implemented **NAT Gateway, ASG, ALB** for HA.  
    - Integrated **CloudWatch alarms** for EC2/CPU monitoring.  
    """)  # Project details
    st.markdown("**Automated Cost Optimization System**")  # Second project title
    st.markdown("""
    - Built AWS Lambda + CloudWatch monitoring solution to detect underutilized resources.  
    - Automated shutdowns for EC2/RDS in off-peak hours.  
    - Saved **$1,200/month** with autoscaling & optimization.  
    """)  # Project details

# --- SKILLS & CERTIFICATIONS ---
with menu[3]:  # Fourth tab: Skills & Certifications
    col1, col2 = st.columns(2)  # Split into two columns
    with col1:  # Left column: Certifications
        st.subheader("📜 Certifications")  # Section header
        st.markdown("""
        - ☁️ AWS Certified Cloud Practitioner  
        - 🏗 AWS Certified Solutions Architect – Associate  
        - ⚙️ HashiCorp Certified: Terraform Associate (003)  
        """)  # List of certifications
    with col2:  # Right column: Skills
        st.subheader("🧩 Skills")  # Section header
        st.markdown("""
        - **Cloud Platforms**: AWS  
        - **IaC**: Terraform, CloudFormation  
        - **CI/CD Tools**: AWS CodePipeline, Jenkins  
        - **Containers**: Docker, Kubernetes, EKS  
        - **Monitoring/Logging**: Prometheus, Grafana, CloudWatch, CloudTrail, Splunk, AppDynamics  
        - **Scripting**: Python, Bash  
        - **Config Mgmt**: Ansible, Rundeck  
        - **Version Control**: Git, CodeCommit, Bitbucket  
        - **Databases**: MySQL, RDS  
        - **Others**: JIRA, Confluence, ServiceNow, Agile  
        """)  # List of skills

# --- EDUCATION ---
with menu[4]:  # Fifth tab: Education
    st.subheader("🎓 Education")  # Section header
    st.write("""
    **Dayananda Sagar College of Engineering (2017 – 2021)**  
    🎓 Bachelor of Engineering – Mechanical Engineering  
    Coursework: Cloud Computing, Automation, Software Engineering  
    """)  # Education details

# --- ACHIEVEMENTS ---
with menu[5]:  # Sixth tab: Achievements
    st.subheader("🏆 Achievements")  # Section header
    st.write("""
    - 🏅 **CDP Award** – Best practices in client data protection.  
    - ⚡ Recognized for automating IAM compliance workflows across **100+ AWS accounts**.  
    - ☁️ Migrated legacy systems to AWS, improving scalability and reliability.  
    """)  # List of achievements

# --- RESUME ---
with menu[6]:  # Seventh tab: Resume
    st.subheader("📑 Resume")  # Section header
    resume_path = "Shah_Nawaz_Hussain_Resume.pdf"  # Path to resume file
    with open(resume_path, "rb") as f:
        resume_bytes = f.read()
    st.download_button(
        label="👉 Download My Resume",
        data=resume_bytes,
        file_name="Shah_Nawaz_Hussain_Resume.pdf",
        mime="application/pdf"
    )


# --- CONTACT ---
with menu[7]:  # Eighth tab: Contact
    st.subheader("📞 Contact Me")  # Section header
    st.markdown("📧 [Email](mailto:shahilhussain41@gmail.com)")  # Email link
    st.markdown("📱 [Call](tel:+919101144633)")  # Phone link
    st.markdown("💼 [LinkedIn](https://www.linkedin.com/in/shah-nawaz-hussain-185b391b2/)")  # LinkedIn link
    st.markdown("💻 [GitHub](https://github.com/shahilhussain41)")  # GitHub link

# --- FOOTER ---
st.markdown(
    """
    <hr style="border:1px solid #555;">  <!-- Horizontal line for separation -->
    <p style="text-align:center; color:gray;">
    © 2025 Shahnawaz Hussain | Built with Streamlit ☁️
    </p>
    """, unsafe_allow_html=True  # Allow HTML for custom footer styling
)
