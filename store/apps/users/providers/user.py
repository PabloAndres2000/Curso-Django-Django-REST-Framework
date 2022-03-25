# Typing
from typing import List, Optional, Union, Tuple

# Django
from django.db.models.query import QuerySet

# Models (Users)
from store.apps.users.models import User

# Lib
from store.apps.users.lib.exceptions.user import(
    CantCreateUser,
    CantUpdateUserStatus,
)

from datetime import datetime


def get_user_by_pk(pk: int) -> Optional[User]:
    """
    Method to obtain a user by pk
    - Returns: Optional[User]
    """
    try:
        user = User.objects.get(pk=pk)
        if not user:
            return None
        return user
    except User.DoesNotExist:
        return None


def get_user_by_identification_number(identification_number: str) -> Optional[User]:
    """
    Method to obtain a user by identification_number
    - Returns_ Optional[User]
    """
    try:
        user = User.objects.get(identification_number=identification_number)
        if not user:
            return None
        return user
    except User.DoesNotExist:
        return None


def get_user_by_email(email: str) -> Optional[User]:
    """
    Method to obtain a user by email
    - Returns_ Optional[User]
    """
    try:
        user = User.objects.get(email=email)
        if not user:
            return None
        return user
    except User.DoesNotExist:
        return None


def get_active_users() -> Union[QuerySet, List[User]]:
    """
    Method for get active users 
    - Returns: List[Users]
    """
    users = User.objects.filter(is_active=True).order_by("first_name")
    return users


def create_user(
    first_name: str,
    last_name: str,
    identification_number: str,
    email: str,
    phone_number: str,
    ip_address: str,
    password: str
) -> Optional[User]:
    """
    Method for create user
    - Returns: Optional[User]
    """
    try:
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            identification_number=identification_number,
            email=email,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save()
        add_ip_address_by_user(user=user, ip_address=ip_address)
        return user
    except CantCreateUser:
        return None


def add_ip_address_by_user(user: User, ip_address: str) -> None:
    if not user.ip_address.get(ip_address):
        user.ip_address[ip_address] = str(datetime.now())
        user.save(update_fields=["ip_address", "updated_at"])
