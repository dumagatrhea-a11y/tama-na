from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Marivic Torrejas Patalan | Portfolio</title>

<style>
:root {
    --lilac: #C8A2C8;
    --light-lilac: #E6D5F7;
    --accent: #B57EDC;
    --background: #211B26;
    --card: #302638;
    --white: #FFFFFF;
    --muted: #D6C9DF;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    scroll-padding-top: 100px;
}

body {
    font-family: Arial, sans-serif;
    background: var(--background);
    color: var(--white);
    line-height: 1.7;
}

a {
    text-decoration: none;
    color: inherit;
}

.container {
    width: 90%;
    max-width: 1100px;
    margin: auto;
}

/* NAVIGATION */

header {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(33, 27, 38, 0.96);
    border-bottom: 1px solid rgba(230, 213, 247, 0.2);
    backdrop-filter: blur(12px);
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    gap: 20px;
}

.logo {
    font-size: 22px;
    font-weight: bold;
    white-space: nowrap;
}

.logo span {
    color: var(--lilac);
}

nav {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
    justify-content: center;
}

nav a {
    color: var(--muted);
    transition: color 0.3s ease;
    font-size: 14px;
}

nav a:hover {
    color: var(--light-lilac);
}

/* HOME SECTION */

.hero {
    min-height: 90vh;
    display: flex;
    align-items: center;
    padding: 70px 0;
}

.hero-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 50px;
}

.hero-text {
    flex: 1;
    animation: slideUp 1s ease;
}

.hero-text h1 {
    font-size: clamp(36px, 5vw, 60px);
    line-height: 1.2;
    margin: 20px 0;
    overflow-wrap: anywhere;
}

.hero-text h1 span {
    color: var(--lilac);
}

.hero-text p {
    color: var(--muted);
    font-size: 17px;
}

.tag {
    display: inline-block;
    padding: 7px 15px;
    border: 1px solid var(--lilac);
    border-radius: 30px;
    color: var(--light-lilac);
    letter-spacing: 1px;
    font-size: 13px;
}

.buttons {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 25px;
}

.btn {
    display: inline-block;
    padding: 12px 22px;
    border-radius: 10px;
    font-weight: bold;
    transition: 0.3s ease;
    text-align: center;
}

.btn-primary {
    background: var(--lilac);
    color: #211B26;
}

.btn-outline {
    border: 1px solid var(--lilac);
    color: var(--light-lilac);
}

.btn:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(181, 126, 220, 0.25);
}

/* PROFILE IMAGE */

.photo-container {
    flex: 0 0 320px;
    position: relative;
    animation: fadeIn 1.5s ease;
}

.photo-container img {
    display: block;
    width: 100%;
    height: 400px;
    object-fit: cover;
    object-position: center;
    border-radius: 25px;
    border: 3px solid var(--lilac);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
}

/* GENERAL SECTIONS */

section:not(.hero) {
    padding: 80px 0;
}

.section-title {
    text-align: center;
    margin-bottom: 40px;
}

.section-title p {
    color: var(--lilac);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 13px;
}

.section-title h2 {
    font-size: 36px;
    margin-top: 5px;
}

.section-title div {
    width: 60px;
    height: 4px;
    background: var(--lilac);
    margin: 15px auto;
    border-radius: 5px;
}

/* CARDS */

.grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 25px;
}

.card {
    background: var(--card);
    padding: 28px;
    border: 1px solid rgba(230, 213, 247, 0.15);
    border-radius: 18px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease, border-color 0.3s ease;
    min-width: 0;
}

.card:hover {
    transform: translateY(-5px);
    border-color: var(--lilac);
}

.card h3 {
    color: var(--light-lilac);
    margin-bottom: 12px;
}

.card p {
    color: var(--muted);
}

/* PERSONAL INFORMATION */

.info-row {
    display: grid;
    grid-template-columns: 130px minmax(0, 1fr);
    gap: 10px;
    padding: 9px 0;
    border-bottom: 1px solid rgba(230, 213, 247, 0.12);
}

.info-row:last-child {
    border-bottom: none;
}

.info-row strong {
    color: var(--light-lilac);
}

.info-row span {
    color: var(--muted);
    overflow-wrap: anywhere;
}

/* EDUCATION */

.education-list {
    max-width: 850px;
    margin: auto;
}

.education-item {
    margin-bottom: 20px;
    border-left: 4px solid var(--lilac);
}

.year {
    color: var(--lilac);
    font-weight: bold;
}

/* SKILLS AND SOCIAL MEDIA */

.skills-grid,
.social-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 20px;
}

.skill-card,
.social-card {
    text-align: center;
}

.skill-icon {
    font-size: 35px;
    margin-bottom: 10px;
}

.social-card a {
    color: var(--light-lilac);
    font-weight: bold;
    overflow-wrap: anywhere;
}

.social-card p {
    margin-bottom: 12px;
}

/* FEATURED PROJECT */

.project-card {
    max-width: 850px;
    margin: 0 auto;
    text-align: center;
}

.project-card .buttons {
    justify-content: center;
}

.project-note {
    margin-top: 18px;
    font-size: 13px;
    color: var(--muted);
}

/* CERTIFICATES */

.certificate-card {
    max-width: 850px;
    margin: 0 auto;
    text-align: center;
}

.certificate-image {
    display: block;
    width: 100%;
    height: auto;
    max-height: 650px;
    object-fit: contain;
    margin: 0 auto 20px;
    border-radius: 12px;
    border: 2px solid var(--lilac);
    background: #ffffff;
}

/* CONTACT */

.contact-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 25px;
}

.contact-link {
    display: block;
    color: var(--muted);
    margin-top: 12px;
    overflow-wrap: anywhere;
}

.contact-link strong {
    color: var(--light-lilac);
}

/* FOOTER */

footer {
    text-align: center;
    padding: 25px;
    border-top: 1px solid rgba(230, 213, 247, 0.2);
    color: var(--muted);
}

/* BACK TO TOP BUTTON */

#backToTop {
    position: fixed;
    right: 20px;
    bottom: 20px;
    width: 45px;
    height: 45px;
    border: none;
    border-radius: 50%;
    background: var(--lilac);
    color: var(--background);
    font-size: 22px;
    cursor: pointer;
    opacity: 0;
    pointer-events: none;
    transition: 0.3s;
    z-index: 999;
}

#backToTop.visible {
    opacity: 1;
    pointer-events: auto;
}

/* SCROLL ANIMATIONS */

.reveal {
    opacity: 0;
    transform: translateY(25px);
    transition: opacity 0.7s ease, transform 0.7s ease;
}

.reveal.show {
    opacity: 1;
    transform: translateY(0);
}

@keyframes slideUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scale(0.95);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* TABLET AND MOBILE */

@media (max-width: 900px) {
    .navbar {
        flex-direction: column;
        gap: 15px;
    }

    nav {
        gap: 12px;
    }

    .hero-content {
        gap: 30px;
    }

    .photo-container {
        flex: 0 0 280px;
    }
}

@media (max-width: 800px) {
    .hero-content {
        flex-direction: column;
        text-align: center;
    }

    .photo-container {
        flex: auto;
        width: min(300px, 100%);
    }

    .buttons {
        justify-content: center;
    }

    .grid,
    .contact-grid {
        grid-template-columns: 1fr;
    }

    .skills-grid,
    .social-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .hero {
        min-height: auto;
        padding: 70px 0;
    }
}

@media (max-width: 480px) {
    .skills-grid,
    .social-grid {
        grid-template-columns: 1fr;
    }

    .info-row {
        grid-template-columns: 1fr;
        gap: 0;
    }

    .section-title h2 {
        font-size: 29px;
    }

    .card {
        padding: 22px;
    }

    nav {
        gap: 10px;
    }

    nav a {
        font-size: 13px;
    }
}

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation: none !important;
        transition: none !important;
        scroll-behavior: auto !important;
    }

    .reveal {
        opacity: 1;
        transform: none;
    }
}
</style>
</head>

<body>

<!-- NAVIGATION -->

<header>
    <div class="container navbar">
        <a href="#home" class="logo">
            Marivic <span>Patalan.</span>
        </a>

        <nav>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#education">Education</a>
            <a href="#skills">Skills</a>
            <a href="#social">Social Media</a>
            <a href="#project">My Project</a>
            <a href="#certificate">Certificates</a>
            <a href="#contact">Contact</a>
        </nav>
    </div>
</header>

<main>

<!-- HOME -->

<section class="hero" id="home">
    <div class="container hero-content">

        <div class="hero-text">
            <span class="tag">PERSONAL PORTFOLIO</span>

            <h1>
                Hello, I'm<br>
                <span>Marivic Torrejas Patalan</span>
            </h1>

            <p>
                A student who enjoys reading, solving interesting problems,
                and continuously learning new things. Welcome to my personal
                portfolio.
            </p>

            <div class="buttons">
                <a href="#about" class="btn btn-primary">
                    Explore My Portfolio
                </a>

                <a href="#contact" class="btn btn-outline">
                    Contact Me
                </a>
            </div>
        </div>

        <div class="photo-container">
            <img
                src="{{ url_for('static', filename='images/patalan.jpg') }}"
                alt="Marivic Torrejas Patalan"
            >
        </div>

    </div>
</section>

<!-- ABOUT ME -->

<section id="about">
    <div class="container">

        <div class="section-title reveal">
            <p>Get to know me</p>
            <h2>About Me</h2>
            <div></div>
        </div>

        <div class="grid">

            <div class="card reveal">
                <h3>A Little About Me</h3>

                <p>
                    I am a student who values learning, creativity, and
                    personal growth. I enjoy reading and solving interesting
                    problems. I aim to continue improving my knowledge and
                    skills through practice and experience.
                </p>
            </div>

            <div class="card reveal">
                <h3>Personal Information</h3>

                <div class="info-row">
                    <strong>Full Name</strong>
                    <span>Marivic Torrejas Patalan</span>
                </div>

                <div class="info-row">
                    <strong>Gender</strong>
                    <span>Female</span>
                </div>

                <div class="info-row">
                    <strong>Age</strong>
                    <span>19 years old</span>
                </div>

                <div class="info-row">
                    <strong>Occupation</strong>
                    <span>Student</span>
                </div>

                <div class="info-row">
                    <strong>Interests</strong>
                    <span>Reading and solving interesting problems</span>
                </div>
            </div>

        </div>
    </div>
</section>

<!-- EDUCATION -->

<section id="education">
    <div class="container">

        <div class="section-title reveal">
            <p>My learning journey</p>
            <h2>Education</h2>
            <div></div>
        </div>

        <div class="education-list">

            <div class="card education-item reveal">
                <span class="year">2025 – 2029</span>
                <h3>Torres Capitol College, Inc.</h3>
                <p>College</p>
            </div>

            <div class="card education-item reveal">
                <span class="year">2019 – 2025</span>
                <h3>
                    Roman C. Villalon Memorial Colleges Foundation Incorporated
                </h3>
                <p>Secondary Education</p>
            </div>

            <div class="card education-item reveal">
                <span class="year">2013 – 2019</span>
                <h3>Kibawe Central Elementary School</h3>
                <p>Elementary Education</p>
            </div>

        </div>
    </div>
</section>

<!-- SKILLS -->

<section id="skills">
    <div class="container">

        <div class="section-title reveal">
            <p>What I can do</p>
            <h2>Skills & Strengths</h2>
            <div></div>
        </div>

        <div class="skills-grid">

            <div class="card skill-card reveal">
                <div class="skill-icon">💻</div>
                <h3>Python Programming</h3>
            </div>

            <div class="card skill-card reveal">
                <div class="skill-icon">🧩</div>
                <h3>Problem Solving</h3>
            </div>

            <div class="card skill-card reveal">
                <div class="skill-icon">🧠</div>
                <h3>Critical Thinking</h3>
            </div>

            <div class="card skill-card reveal">
                <div class="skill-icon">📚</div>
                <h3>Reading Comprehension</h3>
            </div>

            <div class="card skill-card reveal">
                <div class="skill-icon">🎨</div>
                <h3>UI/UX Design</h3>
            </div>

            <div class="card skill-card reveal">
                <div class="skill-icon">🪟</div>
                <h3>Tkinter Interface Design</h3>
            </div>

        </div>
    </div>
</section>

<!-- SOCIAL MEDIA -->

<section id="social">
    <div class="container">

        <div class="section-title reveal">
            <p>Connect with me</p>
            <h2>Social Media</h2>
            <div></div>
        </div>

        <div class="social-grid">

            <div class="card social-card reveal">
                <div class="skill-icon">ⓕ</div>
                <h3>Facebook</h3>
                <p>Visit my Facebook profile.</p>

                <a
                    href="https://www.facebook.com/mrvcbkyng"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Open Facebook ↗
                </a>
            </div>

            <div class="card social-card reveal">
                <div class="skill-icon">◎</div>
                <h3>Instagram</h3>
                <p>Visit my Instagram profile.</p>

                <a
                    href="https://www.instagram.com/_u/mrvc.bkyng/"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Open Instagram ↗
                </a>
            </div>

            <div class="card social-card reveal">
                <div class="skill-icon">♪</div>
                <h3>TikTok</h3>
                <p>Visit my TikTok profile.</p>

                <a
                    href="https://www.tiktok.com/@jhulian.claire.an"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Open TikTok ↗
                </a>
            </div>

        </div>
    </div>
</section>

<!-- AYAW SAYANG FOOD PROJECT -->

<section id="project">
    <div class="container">

        <div class="section-title reveal">
            <p>My work</p>
            <h2>Featured Project</h2>
            <div></div>
        </div>

        <div class="card reveal project-card">

            <div class="skill-icon">📄</div>

            <h3>Ayaw Sayang Food</h3>

            <p>
                Explore my Ayaw Sayang Food project by opening the Word
                document through the link below.
            </p>

            <div class="buttons">
                <a
                    class="btn btn-primary"
                    href="https://cdn.fbsbx.com/v/t59.2708-21/874879842_1861868535229969_3543984927741098407_n.docx/ayawsayangfood.docx?_nc_cat=105&amp;ccb=1-7&amp;_nc_sid=2b0e22&amp;_nc_eui2=AeHQrATT6Wpivwjs05dsYRRChmTJNuDGCneGZMk24MYKd6EQbebr9Cl_1teOPgEtQmwBSg1yi4Y9pyE-1V03HlL4&amp;_nc_ohc=OIvJkyqmWh0Q7kNvwFWg7U-&amp;_nc_oc=AdoghOSxNIhXBsj6QKm5sEIcSdNMJ0HrkFX19WqN3EwsNZjd-qe-1_5B1GBMCFKTFMc&amp;_nc_ad=z-m&amp;_nc_cid=0&amp;_nc_zt=7&amp;_nc_ht=cdn.fbsbx.com&amp;_nc_gid=_WJrwmRWKwknGlge2UGR9Q&amp;_nc_ss=7f22e&amp;oh=03_Q7cD6wFlUhYAsALaFsGrd8DCnQ2YG9B6_XQ85INOPXt3URSl0A&amp;oe=6AE51D0A&amp;dl=1"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Open / Download Document ↗
                </a>
            </div>

            <p class="project-note">
                This button uses the document link you provided. If the link
                expires or asks for permission, replace it with a permanent
                sharing link.
            </p>

        </div>
    </div>
</section>

<!-- CERTIFICATES -->

<section id="certificate">
    <div class="container">

        <div class="section-title reveal">
            <p>My achievements</p>
            <h2>Certificates</h2>
            <div></div>
        </div>

        <div class="card reveal certificate-card">

            <img
                src="{{ url_for('static', filename='images/gwapa.png') }}"
                alt="Certificate of achievement"
                class="certificate-image"
                loading="lazy"
            >

            <h3>My Certificate</h3>

            <p>
                A certificate showcasing my achievement.
            </p>

        </div>
    </div>
</section>

<!-- CONTACT -->

<section id="contact">
    <div class="container">

        <div class="section-title reveal">
            <p>Let's get in touch</p>
            <h2>Contact Me</h2>
            <div></div>
        </div>

        <div class="contact-grid">

            <div class="card reveal">
                <h3>Contact Information</h3>

                <a
                    class="contact-link"
                    href="mailto:marivicpatalan80@gmail.com"
                >
                    <strong>Email:</strong>
                    marivicpatalan80@gmail.com
                </a>

                <a
                    class="contact-link"
                    href="tel:09353946726"
                >
                    <strong>Phone:</strong>
                    09353946726
                </a>
            </div>

            <div class="card reveal">
                <h3>Thank You for Visiting!</h3>

                <p>
                    Thank you for taking the time to explore my portfolio.
                    Feel free to contact me using the information provided.
                </p>

                <div class="buttons">
                    <a
                        class="btn btn-primary"
                        href="mailto:marivicpatalan80@gmail.com"
                    >
                        Send an Email
                    </a>
                </div>
            </div>

        </div>
    </div>
</section>

</main>

<!-- FOOTER -->

<footer>
    <div class="container">
        © 2026 Marivic Torrejas Patalan. All rights reserved.
    </div>
</footer>

<!-- BACK TO TOP BUTTON -->

<button id="backToTop" aria-label="Back to top">
    ↑
</button>

<!-- JAVASCRIPT ANIMATIONS -->

<script>
/* Scroll reveal animation */

const revealObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                revealObserver.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.12 }
);

document.querySelectorAll(".reveal").forEach(element => {
    revealObserver.observe(element);
});

/* Back to top button */

const backToTop = document.getElementById("backToTop");

window.addEventListener("scroll", () => {
    backToTop.classList.toggle(
        "visible",
        window.scrollY > 400
    );
});

backToTop.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE)


if __name__ == "__main__":
    app.run(debug=True, port=8000)