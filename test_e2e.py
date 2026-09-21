import os
import sys

import django
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


load_dotenv()

USER_PASSWORD = os.getenv("E2E_USER_PASSWORD")
ADMIN_PASSWORD = os.getenv("E2E_ADMIN_PASSWORD")

if not USER_PASSWORD or not ADMIN_PASSWORD:
    sys.exit(
        "E2E_USER_PASSWORD dan E2E_ADMIN_PASSWORD "
        "belum diisi di berkas .env."
    )


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "portofolio.settings",
)

django.setup()

from django.contrib.auth.models import User


BASE_URL = "http://127.0.0.1:8000"


def setup_users():
    user, _ = User.objects.get_or_create(
        username="tutorial04_e2e_user"
    )

    user.set_password(USER_PASSWORD)
    user.is_superuser = False
    user.is_staff = False
    user.save()

    admin, _ = User.objects.get_or_create(
        username="tutorial04_e2e_admin"
    )

    admin.set_password(ADMIN_PASSWORD)
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()


def login_with(driver, wait, username, password):
    driver.get(
        f"{BASE_URL}/login/"
    )

    username_input = wait.until(
        EC.presence_of_element_located(
            (
                By.NAME,
                "username",
            )
        )
    )

    password_input = driver.find_element(
        By.NAME,
        "password",
    )

    username_input.clear()
    username_input.send_keys(
        username
    )

    password_input.clear()
    password_input.send_keys(
        password
    )

    driver.find_element(
        By.XPATH,
        "//button[@type='submit']",
    ).click()

    wait.until(
        EC.url_to_be(
            f"{BASE_URL}/"
        )
    )


def main():
    setup_users()

    options = webdriver.ChromeOptions()

    if "--headless" in sys.argv:
        options.add_argument(
            "--headless=new"
        )

        options.add_argument(
            "--window-size=1920,1080"
        )
    else:
        options.add_argument(
            "--start-maximized"
        )

    options.add_experimental_option(
        "excludeSwitches",
        ["enable-logging"],
    )

    driver = webdriver.Chrome(
        options=options
    )

    wait = WebDriverWait(
        driver,
        10,
    )

    try:
        # =========================================
        # 1. CEK SERVER DAN CSRF TOKEN
        # =========================================

        try:
            driver.get(
                f"{BASE_URL}/login/"
            )
        except WebDriverException:
            print(
                f"Server belum berjalan di {BASE_URL}."
            )

            print(
                "Jalankan 'python manage.py runserver' "
                "di terminal lain terlebih dahulu."
            )

            return

        wait.until(
            EC.presence_of_element_located(
                (
                    By.NAME,
                    "username",
                )
            )
        )

        csrf_token = driver.find_element(
            By.NAME,
            "csrfmiddlewaretoken",
        )

        assert csrf_token.get_attribute(
            "value"
        )

        print(
            "[PASS] CSRF token tersedia pada form login"
        )

        # =========================================
        # 2. LOGIN USER BIASA + CEK COOKIE
        # =========================================

        login_with(
            driver,
            wait,
            "tutorial04_e2e_user",
            USER_PASSWORD,
        )

        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(@href, '/logout/')]",
                )
            )
        )

        session_cookie = driver.get_cookie(
            "sessionid"
        )

        last_login_cookie = driver.get_cookie(
            "last_login"
        )

        assert session_cookie is not None
        assert last_login_cookie is not None

        print(
            "[PASS] Login user biasa berhasil"
        )

        print(
            "[PASS] Cookie sessionid berhasil dibuat"
        )

        print(
            "[PASS] Cookie last_login berhasil dibuat"
        )

        # =========================================
        # 3. USER BIASA TIDAK BOLEH TAMBAH PROJECT
        # =========================================

        driver.get(
            f"{BASE_URL}/create-project/"
        )

        wait.until(
            lambda current_driver:
            "403" in current_driver.title
            or "Forbidden"
            in current_driver.page_source
        )

        print(
            "[PASS] User biasa ditolak dari "
            "halaman tambah project (403)"
        )

        # =========================================
        # 4. LOGIN SEBAGAI SUPERUSER
        # =========================================

        driver.get(
            f"{BASE_URL}/logout/"
        )

        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(@href, '/login/')]",
                )
            )
        )

        login_with(
            driver,
            wait,
            "tutorial04_e2e_admin",
            ADMIN_PASSWORD,
        )

        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(@href, '/logout/')]",
                )
            )
        )

        driver.get(
            f"{BASE_URL}/create-project/"
        )

        wait.until(
            EC.presence_of_element_located(
                (
                    By.NAME,
                    "title",
                )
            )
        )

        assert driver.current_url == (
            f"{BASE_URL}/create-project/"
        )

        print(
            "[PASS] Superuser berhasil mengakses "
            "halaman tambah project"
        )

        # =========================================
        # 5. LOGOUT + CEK COOKIE
        # =========================================

        driver.get(
            f"{BASE_URL}/logout/"
        )

        wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//a[contains(@href, '/login/')]",
                )
            )
        )

        last_login_cookie = driver.get_cookie(
            "last_login"
        )

        assert (
            last_login_cookie is None
            or last_login_cookie["value"] == ""
        )

        print(
            "[PASS] Logout berhasil"
        )

        print(
            "[PASS] Cookie last_login berhasil dihapus"
        )

        print()
        print(
            "Semua pengujian E2E Tutorial 04 berhasil!"
        )

    finally:
        driver.quit()


if __name__ == "__main__":
    main()