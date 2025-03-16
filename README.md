# Joburi pentru Romani - Django Job Posting Website

This is a Django-based website for posting job listings, designed to be responsive and incorporate AdSense বিজ্ঞাপন locations. Only administrators can post new job listings, providing control over the content.

## Features

*   **Job Postings:** Allows posting and display of job listings with details like title, description, company, location, and posted date.
*   **Admin Controlled Posting:** Only superusers can create, edit, and publish job postings via the Django admin interface.
*   **Responsive Design:** Built with Bootstrap 4 to ensure responsiveness across various devices (desktops, tablets, and mobile phones).
*   **AdSense Ready:** Includes designated locations for AdSense বিজ্ঞাপন units in templates for easy integration.
*   **Modern UI/UX:** Features a clean and modern design with a focus on usability and readability.

## Setup for Development

1.  **Prerequisites:** Ensure you have Python and pip installed on your system.
2.  **Clone the repository:** (If applicable, if you were providing a git repository)
    ```bash
    git clone [repository-url]
    cd joburipentruromani.online
    ```
3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
6.  **Create a superuser (admin account):**
    ```bash
    python manage.py createsuperuser
    ```
7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The website will be accessible at `http://127.0.0.1:8000/`. Access the admin panel at `http://127.0.0.1:8000/admin/`.

## Deployment Instructions for Hostinger VPS (Ubuntu 24.04 with OpenLiteSpeed and Django)

1.  **VPS Setup:** Ensure Python 3.8+ and `pip` are installed on your Ubuntu 24.04 VPS.
2.  **Transfer Project Files:** Use `scp` or `rsync` to securely copy the `joburipentruromani.online` project directory to your VPS (e.g., to `/home/root/`).
    ```bash
    scp -r /path/to/your/local/project root@45.9.190.224:/home/root/
    ```
3.  **SSH into VPS:** `ssh root@45.9.190.224`
4.  **Navigate to Project Directory:** `cd /home/root/joburipentruromani.online`
5.  **Create Virtual Environment (Recommended):** `python3 -m venv venv && source venv/bin/activate`
6.  **Install Dependencies:** `pip install -r requirements.txt`
7.  **Apply Database Migrations:** `python manage.py migrate`
8.  **Collect Static Files:** `python manage.py collectstatic`
9.  **Set up WSGI Server (Gunicorn):** `pip install gunicorn`
10. **Configure OpenLiteSpeed:** Set up a virtual host, proxy settings to Gunicorn, and static files serving in your Hostinger control panel or OpenLiteSpeed configuration (refer to Hostinger documentation).
11. **DNS Configuration:** Point the A record for `joburipentruromani.online` to `45.9.190.224`.
12. **HTTPS Setup (Highly Recommended):** Use Let's Encrypt and configure OpenLiteSpeed for HTTPS.

## AdSense Integration

The website is designed to incorporate AdSense বিজ্ঞাপন units.

*   **Sitewide AdSense Code:**  The sitewide AdSense code (provided in `jobs/templates/jobs/base.html`) is placed in the `<head>` section of the base template and will be present on every page.
*   **Ad Locations:** Designated locations for AdSense units are included in:
    *   Header of the job list page (`jobs/templates/jobs/job_list.html`)
    *   Within each job listing card on the job list page (`jobs/templates/jobs/job_list.html`)
    *   Footer of the job list page (`jobs/templates/jobs/job_list.html`)
    *   Top of the job detail page (`jobs/templates/jobs/job_detail.html`)
    *   Bottom of the job detail page (`jobs/templates/jobs/job_detail.html`)

    You need to replace the placeholder AdSense code comments with your actual AdSense code snippets in the respective template files.

## Customization

*   **Templates:**  Customize the HTML templates in `jobs/templates/jobs/` to modify the website's appearance and layout.
*   **CSS:**  Modify the CSS styles in `jobs/templates/jobs/base.html` or create separate CSS files in `static/jobs/css/` to adjust the website's styling.
*   **Models:**  Extend the `Job` model in `jobs/models.py` to add more fields as needed for job postings.
*   **Views:**  Modify the views in `jobs/views.py` to alter the website's functionality and data handling.

---

Developed by Cline as per user request.
