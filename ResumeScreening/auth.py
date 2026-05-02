from database import add_user, check_user


def signup_user(username: str, password: str) -> tuple[bool, str]:
    if not username or not password:
        return False, "Username and password cannot be empty"

    success = add_user(username, password)

    if success:
        return True, "Signup successful"
    return False, "Username already exists"


def login_user(username: str, password: str) -> bool:
    if not username or not password:
        return False
    return check_user(username, password)

