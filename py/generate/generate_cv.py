# Recreate the refined CV as a new document to ensure proper download link generation
from docx import Document

# Create a new document for the refined CV
doc = Document()

# Header
doc.add_paragraph('Wahidin Alambiyah', style='Title')
doc.add_paragraph('South Tangerang, Banten | +6285720046376 | wahidin.alambiyah@gmail.com')

# Professional Summary
doc.add_heading('Professional Summary', level=1)
doc.add_paragraph(
    "Experienced Java Backend Developer with over 9 years of expertise in building and optimizing scalable backend "
    "solutions. Demonstrated ability in leading full-stack development projects and collaborating with cross-functional teams. "
    "Proficient in Java, Spring Boot, microservices architecture, and cloud platforms. Skilled in handling complex systems, "
    "enhancing performance, and ensuring seamless system integration."
)

# Experience Section
doc.add_heading('Experience', level=1)

# PT Bumi Amartha Teknologi
doc.add_paragraph('Lead Backend Developer, PT Bumi Amartha Teknologi, Jakarta', style='Heading 2')
doc.add_paragraph('September 2023 – Present')
doc.add_paragraph(
    "Currently serving as a Lead Backend Developer at PT Bumi Amartha Teknologi, placed at Bank Sinarmas as a DevOps "
    "Engineer for the Risk Team ICE. Responsibilities include setting up new environments, maintaining existing systems, "
    "deploying applications, and supporting backend development. Collaborated with teams to establish CI/CD pipelines, "
    "configure Docker and Kubernetes, and upgrade Java environments."
)
doc.add_paragraph(
    "- Key Projects:\n"
    "  - Bank SINARMAS (MSME, Param Monitoring, Risk Decision Engine ICE MAIN) using Gitlab, Jenkins.\n"
    "  - SMMA (ICE MAIN) for Dev and UAT environments.\n"
    "  - Danamas (ICE LITE) using Docker for Dev, UAT, and Production, with ELK stack implementation.\n"
    "  - Migrated ICE MAIN from BSIM to SMMA using Gitlab, Gitlab Runner, and Kubernetes for UAT and Production."
)

# PT Tri Adi Bersama (AnterAja)
doc.add_paragraph('Backend Developer, PT Tri Adi Bersama (AnterAja)', style='Heading 2')
doc.add_paragraph('February 2019 – August 2023')
doc.add_paragraph(
    "Led backend development for high-impact projects, optimizing applications, and managing scalable solutions. "
    "Improved ticket resolution by 30% and optimized backend processing in various applications."
)
doc.add_paragraph(
    "- Key Projects:\n"
    "  - E-bill: Developed backend for billing, enhancing processing by 20%.\n"
    "  - FVP, PVS Applications: Managed pricing data through microservices.\n"
    "  - CRM - CMS (Ticketing): Reduced ticket resolution time by optimizing workflows.\n"
    "  - SF International ID (Freight Forwarding): Built secure and scalable logistics solutions."
)

# PT Indocyber Global Teknologi
doc.add_paragraph('Backend Developer / Fullstack Developer, PT Indocyber Global Teknologi', style='Heading 2')
doc.add_paragraph('March 2019 – February 2020')
doc.add_paragraph(
    "Maintained and enhanced backend systems for AnterAja HQ, ensuring smooth operations and database integration."
)

# PT Indo Copora Investama (Padiciti)
doc.add_paragraph('Java Developer / Fullstack Developer, PT Indo Copora Investama (Padiciti)', style='Heading 2')
doc.add_paragraph('February 2016 – March 2019')
doc.add_paragraph(
    "- Key Projects:\n"
    "  - Padipay.com: Increased transaction capacity by 40% through multi-gateway integration.\n"
    "  - Padiciti.com: Enhanced booking system with waitlist feature."
)

# PT Venturium System Indonesia
doc.add_paragraph('Java Developer / Fullstack Developer, PT Venturium System Indonesia', style='Heading 2')
doc.add_paragraph('October 2014 – February 2016')
doc.add_paragraph(
    "Managed full-cycle development for financial applications, including yearly updates for Swift Alliance Access integration."
)

# Education
doc.add_heading('Education', level=1)
doc.add_paragraph('INFORMATION MANAGEMENT, UNIVERSITAS NASIONAL PASIM', style='Heading 2')
doc.add_paragraph('Diploma (D3) | GPA: 3.85/4.00')

# Skills
doc.add_heading('Skills', level=1)
doc.add_paragraph(
    "- Languages & Frameworks: Java (Spring Boot, Spring MVC), JavaScript, TypeScript, Angular, Vue.js\n"
    "- Databases: MySQL, PostgreSQL, MongoDB, Redis, SQL Server\n"
    "- Tools & Technologies: Azure DevOps, Google Cloud Storage, Kafka, RabbitMQ, Docker, Kubernetes\n"
    "- CI/CD & Version Control: Git, Gitlab, Jenkins\n"
    "- Other Skills: Microservices, REST APIs, Scrum Master"
)

# Save the refined document
output_file_path = r'C:\Users\wahid\Downloads\Wahidin_Alambiyah_CV_Final.docx'
doc.save(output_file_path)

output_file_path
