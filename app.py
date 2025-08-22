import streamlit as st  # Import Streamlit library for building web apps
import os  # Import OS library for file operations

# --- Page Configuration ---
st.set_page_config(  # Set Streamlit page configuration
    page_title="Shah Nawaz Hussain | Cloud DevOps Portfolio",  # Set browser tab title
    layout="wide",  # Use wide layout for the page
    page_icon="💻"  # Set page icon
)

# --- Sidebar Navigation ---
# Display profile image safely (updated to teams(2).jpg)
profile_image_path = "profile.png"  # Path to profile image
try:
    st.sidebar.image(profile_image_path, width=120)  # Show profile image in sidebar
except FileNotFoundError:
    st.sidebar.warning(f"Profile image '{profile_image_path}' not found.")  # Warn if image not found

# Navigation menu
menu = [  # List of navigation options
    "About Me",
    "Experience",
    "Projects",
    "Skills & Certifications",
    "Education",
    "Achievements",
    "Contact"
]
choice = st.sidebar.radio("Navigation", menu)  # Sidebar radio button for navigation

# --- Helper Functions ---
def show_about():  # Function to show About Me section
    st.title("👨‍💻 Shah Nawaz Hussain")  # Display title
    st.subheader("Cloud Automation & DevOps Engineer | AWS | Terraform | CI/CD")  # Display subheader
    st.markdown("""  # Display markdown content
Cloud Automation and DevOps Engineer with **3.11 years of experience** in AWS infrastructure, Terraform (IaC),
and CI/CD implementation.

- Proven track record of reducing deployment times by **30%** and optimizing AWS resource costs.
- Certified **AWS Solutions Architect** and **Terraform Associate**.
- Hands-on expertise in **Lambda automation, Prometheus-Grafana monitoring**, and building secure architecture aligned with the AWS Well-Architected Framework.
""")

def show_experience():  # Function to show Experience section
    st.header("💼 Work Experience")  # Display header
    st.subheader("Accenture Solutions Pvt. Ltd. | Cloud DevOps Engineer")  # Display subheader
    st.write("📍 Bengaluru | Dec 2021 - Present")  # Display location and duration
    st.markdown("""  # Display markdown content
- Reduced deployment time by **30%** by developing and optimizing CI/CD pipelines using AWS CodeCommit, CodeBuild, CodeDeploy, and CodePipeline.
- Created & managed **200+ IAM users, groups, policies, roles** via Terraform (IaC).
- Automated IAM compliance for **100+ AWS accounts** via Lambda, reducing non-compliance by **60%**.
- Ensured **99.9% uptime** using Blue/Green, Canary, and Rolling deployment strategies.
- Monitored EC2 and databases using **Grafana, Prometheus, CloudWatch, CloudTrail**, reducing MTTR by **40%**.
- Implemented **AWS Well-Architected Framework** across multiple environments.
- Configured **NACL rules** across 10+ VPC subnets using Terraform.
""")

def show_projects():  # Function to show Projects section
    st.header("🚀 Projects")  # Display header
    with st.expander("1. AWS Architecture for 3-Tier Web Hosting", expanded=True):  # Expandable project section
        st.markdown("""  # Display markdown content
- Designed a **scalable 3-Tier architecture** (frontend, backend, DB) on AWS.
- Automated with **Terraform**.
- Used **NAT Gateway, Auto Scaling Groups, and ALB** for high availability.
- Integrated **CloudWatch alarms** for proactive monitoring.
""")
    with st.expander("2. Automated Cost Optimization System", expanded=True):  # Expandable project section
        st.markdown("""  # Display markdown content
- Built an **AWS Lambda-based monitoring solution** integrated with CloudWatch.
- Identified underutilized EC2/RDS instances and automated shutdown schedules.
- Saved **$1,200 monthly** by enforcing autoscaling and off-peak shutdowns.
""")

def show_skills():  # Function to show Skills & Certifications section
    st.header("🛠️ Skills & Certifications")  # Display header
    col1, col2 = st.columns(2)  # Create two columns
    with col1:
        st.markdown("**Certifications**")  # Display certifications header
        st.markdown("""  # Display markdown content
- AWS Certified Cloud Practitioner
- AWS Certified Solutions Architect – Associate
- HashiCorp Certified: Terraform Associate (003)
""")
    with col2:
        st.markdown("**Skills**")  # Display skills header
        st.markdown("""  # Display markdown content
- **Cloud Platforms**: AWS
- **CI/CD Tools**: CodePipeline, Jenkins
- **IaC**: Terraform, CloudFormation
- **Containers**: Docker, Kubernetes, EKS
- **Monitoring**: Prometheus, Grafana, CloudWatch, CloudTrail
- **Configuration Mgmt**: Ansible, Rundeck
- **Scripting**: Python, Bash
- **Databases**: MySQL, RDS
- **Others**: Git, Bitbucket, JIRA, ServiceNow
""")

def show_education():  # Function to show Education section
    st.header("🎓 Education")  # Display header
    st.markdown("""  # Display markdown content
**Dayananda Sagar College of Engineering (2017 - 2021)**
- Bachelor of Engineering (Mechanical Engineering)
""")

def show_achievements():  # Function to show Achievements section
    st.header("🏆 Achievements")  # Display header
    st.markdown("""  # Display markdown content
- **CDP Award** – For best practices in client data protection during project implementation.
- Recognized by senior leadership for **automating IAM compliance workflows** impacting 100+ accounts.
""")

def show_contact():  # Function to show Contact section
    st.header("📬 Contact Me")  # Display header
    st.write("📧 Email: shahilhussain41@gmail.com")  # Display email
    st.write("📱 Phone: +91 9101144633")  # Display phone
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/shah-nawaz-hussain-185b391b2/)")  # LinkedIn link
    st.markdown("[💻 GitHub](https://github.com/shahilhussain41)")  # GitHub link

    resume_path = "Shah_Nawaz_Hussain_Resume.pdf"  # Path to resume PDF
    try:
        with open(resume_path, "rb") as pdf_file:  # Open resume file in binary mode
            st.download_button("📄 Download Resume", pdf_file, resume_path)  # Download button for resume
    except FileNotFoundError:
        st.warning("Resume file not found.")  # Warn if resume not found

# --- Main Content ---
pages = {  # Dictionary mapping menu choices to functions
    "About Me": show_about,
    "Experience": show_experience,
    "Projects": show_projects,
    "Skills & Certifications": show_skills,
    "Education": show_education,
    "Achievements": show_achievements,
    "Contact": show_contact
}
pages.get(choice, show_about)()  # Call the selected page function, default to show_about
