from typing import Callable, Dict

ConfirmNewPassword = Callable[[str, str], None]
FactoryEmailSender = Dict[str, ConfirmNewPassword]

def email_sender() -> FactoryEmailSender:

    def confirm_new_password(username: str, email: str) -> None:
        pass

    return {"confirm_new_password": confirm_new_password}
