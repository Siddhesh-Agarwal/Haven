import os
import string
from math import log2
from secrets import choice

import polars as pd


class UserExistsError(Exception):
    """Raised when a user already exists."""

    pass


class InvalidUsername(Exception):
    """Raised when an invalid username is entered."""

    pass


SPECIALS = "!@#$%^&*."


def new_password(
    length: int,
    lowercase: bool = False,
    uppercase: bool = False,
    numbers: bool = False,
    specials: bool = False,
    /,
) -> str:

    if any([lowercase, uppercase, numbers, specials]):
        allowed = ""
        if lowercase:
            allowed += string.ascii_lowercase
        if uppercase:
            allowed += string.ascii_uppercase
        if numbers:
            allowed += string.digits
        if specials:
            allowed += SPECIALS
        password = "".join(choice(allowed) for _ in range(length))
        return password
    ValueError("Please allow at least 1 type of character.")


def password_entropy(password: str) -> float:
    """Check the strength of a password."""
    digits, uppercase, lowercase, specials = False, False, False, False

    for i in password:
        if i.isdigit():
            digits = True
        elif i.isupper():
            uppercase = True
        elif i.islower():
            lowercase = True
        elif i in SPECIALS:
            specials = True
        else:
            raise ValueError("Invalid character in password")

    R = digits * 10 + uppercase * 26 + lowercase * 26 + specials * len(SPECIALS)
    L = len(password)
    E = L * log2(R)

    return round(E, 3)


def save_password(username: str, password: str, website: str) -> None:
    """Save the password in a file."""
    with open(f"db/users/{username.lower()}.csv", "a+") as f:
        f.write(f"{website},{password}\n")


def check_username(username: str) -> None:
    """Throws error if a username.csv file is present."""
    for char in username:
        if not any([char.isalnum(), char == "_", char == "-"]):
            raise InvalidUsername(
                "Username must contain only alphanumeric characters (A-Z, a-z, 0-9), _ and -"
            )
    if os.path.exists(f"db/{username.lower()}.csv"):
        raise UserExistsError(f"User {username} already exists")


def get_password(username: str, website: str = None):
    """Get the password from a file."""
    if website is None:
        df = pd.read_csv(f"db/{username.lower()}.csv")
        return df.to_pandas()
    else:
        df = pd.read_csv(f"db/{username.lower()}.csv")
        return df[df["website"] == website].to_pandas()


def generate_salt():
    """Generate a salt for password encryption."""
    return "".join(
        choice(string.ascii_letters + string.digits + SPECIALS) for _ in range(16)
    )
