import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Shah Nawaz Hussain | Cloud DevOps Portfolio",
    layout="wide",
    page_icon="💻"
)

# --- Sidebar Navigation ---
# Display profile image safely
try:
    st.sidebar.image("profile.jpg", width=120)
except FileNotFoundError:
    st.sidebar.warning("Profile image not found.")

# Navigation menu
menu = [
    "About Me",
    "Experience",
    "Projects",
    "Skills & Certifications",
    "Education",
    "Achievements",
    "Contact"
]

choice = st.sidebar.radio("Navigation", menu)

# --- Helper Functions ---
def show_about():
    st.title("👨‍💻 Shah Nawaz Hussain")
    st.subheader("Cloud Automation & DevOps Engineer | AWS | Terraform | CI/CD")
    st.markdown("""
Cloud Automation and DevOps Engineer with **3.11 years of experience** in AWS infrastructure, Terraform (IaC),
and CI/CD implementation.

- Proven track record of reducing deployment times by **30%** and optimizing AWS resource costs.
- Certified **AWS Solutions Architect** and **Terraform Associate**.
- Hands-on expertise in **Lambda automation, Prometheus-Grafana monitoring**, and building secure architecture aligned with the AWS Well-Architected Framework.
""")

def show_experience():
    st.header("💼 Work Experience")
    st.subheader("Accenture Solutions Pvt. Ltd. | Cloud DevOps Engineer")
    st.write("📍 Bengaluru | Dec 2021 - Present")
    st.markdown("""
- Reduced deployment time by **30%** by developing and optimizing CI/CD pipelines using AWS CodeCommit, CodeBuild, CodeDeploy, and CodePipeline.
- Created & managed **200+ IAM users, groups, policies, roles** via Terraform (IaC).
- Automated IAM compliance for **100+ AWS accounts** via Lambda, reducing non-compliance by **60%**.
- Ensured **99.9% uptime** using Blue/Green, Canary, and Rolling deployment strategies.
- Monitored EC2 and databases using **Grafana, Prometheus, CloudWatch, CloudTrail**, reducing MTTR by **40%**.
- Implemented **AWS Well-Architected Framework** across multiple environments.
- Configured **NACL rules** across 10+ VPC subnets using Terraform.
""")

def show_projects():
    st.header("🚀 Projects")
    with st.expander("1. AWS Architecture for 3-Tier Web Hosting", expanded=True):
        st.markdown("""
- Designed a **scalable 3-Tier architecture** (frontend, backend, DB) on AWS.
- Automated with **Terraform**.
- Used **NAT Gateway, Auto Scaling Groups, and ALB** for high availability.
- Integrated **CloudWatch alarms** for proactive monitoring.
""")
    with st.expander("2. Automated Cost Optimization System", expanded=True):
        st.markdown("""
- Built an **AWS Lambda-based monitoring solution** integrated with CloudWatch.
- Identified underutilized EC2/RDS instances and automated shutdown schedules.
- Saved **$1,200 monthly** by enforcing autoscaling and off-peak shutdowns.
""")

def show_skills():
    st.header("🛠️ Skills & Certifications")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Certifications**")
        st.markdown("""
- AWS Certified Cloud Practitioner
- AWS Certified Solutions Architect – Associate
- HashiCorp Certified: Terraform Associate (003)
""")
    with col2:
        st.markdown("**Skills**")
        st.markdown("""
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

def show_education():
    st.header("🎓 Education")
    st.markdown("""
**Dayananda Sagar College of Engineering (2017 - 2021)**
- Bachelor of Engineering (Mechanical Engineering)
""")

def show_achievements():
    st.header("🏆 Achievements")
    st.markdown("""
- **CDP Award** – For best practices in client data protection during project implementation.
- Recognized by senior leadership for **automating IAM compliance workflows** impacting 100+ accounts.
""")

def show_contact():
    st.header("📬 Contact Me")
    st.write("📧 Email: shahilhussain41@gmail.com")
    st.write("📱 Phone: +91 9101144633")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/shah-nawaz-hussain-185b391b2/)")
    st.markdown("[💻 GitHub](https://github.com/shahilhussain41)")

    resume_path = "Shah_Nawaz_Hussain_Resume.pdf"
    try:
        with open(resume_path, "rb") as pdf_file:
            st.download_button("📄 Download Resume", pdf_file, resume_path)
    except FileNotFoundError:
        st.warning("Resume file not found.")

# --- Main Content ---
if choice == "About Me":
    show_about()
elif choice == "Experience":
    show_experience()
elif choice == "Projects":
    show_projects()
elif choice == "Skills & Certifications":
    show_skills()
elif choice == "Education":
    show_education()
elif choice == "Achievements":
    show_achievements()
elif choice == "Contact":
    show_contact()

